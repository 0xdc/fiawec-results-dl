#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
import requests

from .event import Event

class Season():
    url = "http://fiawec.alkamelsystems.com/top.php?season={season}"

    def __init__(self, season):
        self.season = season

        self.url = self.url.format(season=season)

    def __str__(self):
        return self.season

    def pull(self):
        if not hasattr(self, "cache"):
            self.cache = requests.get(self.url)
        return self.cache

    def events(self, response=None):
        if response is None:
            response = self.pull()

        soup = BS(response.text, "html.parser")
        self.events = soup.find("select", class_="champSelect").find_all("option")

        #return [ x.get("value") for x in options ]
        return self.events

    def sub(self, events=None):
        if events is None:
            events = self.events()

        return [ Event( x.get("value"), self ) for x in events ]
