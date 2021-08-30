#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
import requests
import requests_cache

from .season import Season, NoticeBoard as NBEvent
from .event import Committee as CommitteeEv

class TopLevel():
    url = "http://fiawec.alkamelsystems.com/"

    def __init__(self, page, cls):
        self.url = self.url + page
        self.cls = cls

    def get_seasons(self):
        top = requests.get(self.url)
        soup = BS(top.text, "html.parser")

        options = soup.find("select", attrs={"name": "season"}).find_all("option")

        return [ x.get("value") for x in options ]

    def sub(self, seasons=None):
        if seasons is None:
            seasons = self.get_seasons()

        return [ self.cls(x) for x in seasons ]


Seasons = TopLevel("index.php", Season)
NoticeBoard = TopLevel("noticeBoard.php", NBEvent)
Committee = TopLevel("committe.php", CommitteeEv)
