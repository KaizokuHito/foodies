#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def app():
	r = requests.get('https://foursquare.com/explore?mode=url&near=Taipei%2C%20Taiwan&nearGeoId=72057594039596277&q=Chinese')
	soup = BeautifulSoup(r.text, 'html.parser')

	foods = soup.find_all("div", "venueName")

	for food in foods:
		food_title = food.h2.a.string
		print(food_title)
		
if __name__ == "__main__":
    # execute only if run as a script
    app()