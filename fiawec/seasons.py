#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
import requests
import requests_cache

from .season import Season

def get_seasons():
    url = "http://fiawec.alkamelsystems.com/index.php"

    top = requests.get(url)
    soup = BS(top.text, "html.parser")

    options = soup.find("select", attrs={"name": "season"}).find_all("option")

    return [ x.get("value") for x in options ]

def sub(seasons=None):
    if seasons is None:
        seasons = get_seasons()

    return [ Season(x) for x in seasons ]
