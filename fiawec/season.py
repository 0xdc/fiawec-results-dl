#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
import requests
import requests_cache

from .event import Event, NBEvent

class Season():
    url = "http://fiawec.alkamelsystems.com/index.php?season={season}"

    def __init__(self, season):
        self.season = season

        self.url = self.url.format(season=season)

    def __str__(self):
        return self.season

    def pull(self):
        if not hasattr(self, "cache"):
            with requests_cache.disabled():
                self.cache = requests.get(self.url)
        return self.cache

    def events(self, response=None):
        if response is None:
            response = self.pull()

        soup = BS(response.text, "html.parser")
        self.events = soup.find("select", attrs={"name": "evvent"}).find_all("option")

        #return [ x.get("value") for x in options ]
        return self.events

    def sub(self, events=None):
        if events is None:
            events = self.events()

        return [ Event( x.get("value"), self ) for x in events ]

class NoticeBoard(Season):
    url = "http://fiawec.alkamelsystems.com/noticeBoard.php?season={season}"

    def sub(self, events=None):
        if events is None:
            events = self.events()

        return [ NBEvent( x.get("value"), self) for x in events ]
