#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
import requests
import os
import urllib

class Event():
    url = "http://fiawec.alkamelsystems.com/tree.php?season={season}&event={event}"

    def __init__(self, event, season):
        self.event = event
        self.season = season

        self.url = self.url.format(season=season, event=event)

    def __str__(self):
        return "{}/{}".format(self.season, self.event)

    def pull(self):
        if not hasattr(self, "cache"):
            self.cache = requests.get(self.url)
        return self.cache

    def event_results(self, response=None):
        if response is None:
            response = self.pull()

        soup = BS(response.text, "html.parser")
        self.results = soup.find_all("a", target="mainFrame")

        #return [ x.get("value") for x in objects ]
        return self.results

    def all(self, results=None):
        if results is None:
            results = self.event_results()

        for result in results:
            href = urllib.parse.unquote(result.get("href"))
            basename = os.path.basename(href)
            dirname = os.path.dirname(href)
            try:
                os.makedirs(dirname)
            except FileExistsError:
                pass

            print(self, basename)
            if not os.path.exists(href):
                url = "http://fiawec.alkamelsystems.com/{}".format(result.get("href"))
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open(href, "wb") as f:
                        for chunk in r:
                            f.write(chunk)
