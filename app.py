#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import requests
from bs4 import BeautifulSoup

def app():
	r = requests.get('https://foursquare.com/explore?mode=url&near=Taipei%2C%20Taiwan&nearGeoId=72057594039596277&q=Chinese')
	soup = BeautifulSoup(r.text, 'html.parser')

	foods = soup.find_all("div", "venueName")

	for food in foods:
		food_title = food.h2.a.string
		print(food_title)

def read_data():
	os.system("curl 'https://api.foursquare.com/v2/search/recommendations?locale=en&explicit-lang=false&v=20171012&m=foursquare&query=Chinese&limit=500&offset=0&sw=24.841580551445354%2C120.71090698242186&ne=25.0383270525352%2C122.35610961914062&wsid=BQDFMWFHKK4TVHV1125CCZIHXQJROK&oauth_token=QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ja;q=0.2,cy;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://api.foursquare.com/xdreceiver.html?parent=https%3A%2F%2Ffoursquare.com%2Fexplore%3Fmode%3Durl%26ne%3D25.115445%252C121.946182%26q%3DChinese%26sw%3D24.878962%252C121.123581' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: bbhive=BQDFMWFHKK4TVHV1125CCZIHXQJROK%3A%3A1570081406; fbm_86734274142=base_domain=.foursquare.com; __gads=ID=1aa7ca4fd6b74717:T=1507015338:S=ALNI_MYNWEGRmuh7OsuAQVQViCsUER8XKw; _ga=GA1.2.2028832632.1507009406; _gid=GA1.2.472143396.1507875219; __utma=51454142.2028832632.1507009406.1507715592.1507873035.4; __utmb=51454142.16.10.1507873035; __utmc=51454142; __utmz=51454142.1507873035.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); fbsr_86734274142=xqV0ZEvOLs_szMjoywUUM4vZjXuothFusbcY-yRwrmw.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURPbkFGM2tnV1h5dl9GNGpWWG1qX245MzQ1ejBMeTZ0NnBKcEE4cUFycDRST2g1S2I2dGJkNkJDTVlCLTJFN1h6ZWNrVEIyVDZMVXIwbnZXM2VtZ1JJTlc4cDk5Zy12NlNvWFBsUG43Mkl2U19sYWt5eGY5TzQ2NUlVTUJBTFliTVdLbUJPVkt2RDU3UXZubHJKZVpNdmNtb1YzQkxlbW1WeV9nMkNYalgzUVZteEt6Z2dKc09VTmtYeENSc1Z3WHFENDBoVHlVanBNLWZWOFlVODlENVZTOHNVdVJXRmUtTWttYUhqRFZsa1FzcVYtX2s0bkNvc3FVd2NhNEJTSks4dE0yTHdxcEpka0Y5cEdfWENtd3E4QV9EbnV1dmZCa2F2M0lVQ2o5Mk1nQlNTM21VU3FiR3JNRldyTU1hRE5IWlBOY3J1eXAzUGFRWkNKN2ZZYXUxSSIsImlzc3VlZF9hdCI6MTUwNzg3NTYxNCwidXNlcl9pZCI6IjgwNzI5NjY0NjA3MTU0NCJ9' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed -o results.json")
	with open('results.json', 'r+') as data_file:
		data = json.load(data_file)
		results = data["response"]["group"]["results"]
		dic = json.JSONEncoder(indent=4).encode({'results_test': results})
		data_file.seek(0)
		data_file.write(dic)
		data_file.truncate()

def read_data_justin():
	# you can use os.system to excute os's command
	os.system("curl 'https://api.foursquare.com/v2/search/recommendations?locale=en&explicit-lang=false&v=20171012&m=foursquare&query=Chinese&limit=500&offset=0&sw=24.841580551445354%2C120.71090698242186&ne=25.0383270525352%2C122.35610961914062&wsid=BQDFMWFHKK4TVHV1125CCZIHXQJROK&oauth_token=QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ja;q=0.2,cy;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://api.foursquare.com/xdreceiver.html?parent=https%3A%2F%2Ffoursquare.com%2Fexplore%3Fmode%3Durl%26ne%3D25.115445%252C121.946182%26q%3DChinese%26sw%3D24.878962%252C121.123581' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: bbhive=BQDFMWFHKK4TVHV1125CCZIHXQJROK%3A%3A1570081406; fbm_86734274142=base_domain=.foursquare.com; __gads=ID=1aa7ca4fd6b74717:T=1507015338:S=ALNI_MYNWEGRmuh7OsuAQVQViCsUER8XKw; _ga=GA1.2.2028832632.1507009406; _gid=GA1.2.472143396.1507875219; __utma=51454142.2028832632.1507009406.1507715592.1507873035.4; __utmb=51454142.16.10.1507873035; __utmc=51454142; __utmz=51454142.1507873035.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); fbsr_86734274142=xqV0ZEvOLs_szMjoywUUM4vZjXuothFusbcY-yRwrmw.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURPbkFGM2tnV1h5dl9GNGpWWG1qX245MzQ1ejBMeTZ0NnBKcEE4cUFycDRST2g1S2I2dGJkNkJDTVlCLTJFN1h6ZWNrVEIyVDZMVXIwbnZXM2VtZ1JJTlc4cDk5Zy12NlNvWFBsUG43Mkl2U19sYWt5eGY5TzQ2NUlVTUJBTFliTVdLbUJPVkt2RDU3UXZubHJKZVpNdmNtb1YzQkxlbW1WeV9nMkNYalgzUVZteEt6Z2dKc09VTmtYeENSc1Z3WHFENDBoVHlVanBNLWZWOFlVODlENVZTOHNVdVJXRmUtTWttYUhqRFZsa1FzcVYtX2s0bkNvc3FVd2NhNEJTSks4dE0yTHdxcEpka0Y5cEdfWENtd3E4QV9EbnV1dmZCa2F2M0lVQ2o5Mk1nQlNTM21VU3FiR3JNRldyTU1hRE5IWlBOY3J1eXAzUGFRWkNKN2ZZYXUxSSIsImlzc3VlZF9hdCI6MTUwNzg3NTYxNCwidXNlcl9pZCI6IjgwNzI5NjY0NjA3MTU0NCJ9' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed -o results.json")
	with open('results.json', 'r+') as data_file:
		data = json.load(data_file)
		results = data["response"]["group"]["results"]
		# let your file follow json's format and use utf-8 encode
		dic = json.dumps(results, indent=4, sort_keys=True).decode('unicode-escape').encode('utf8')
		# set file's current position to 0
		data_file.seek(0)
		data_file.write(dic)
		# truncate remaining file
		data_file.truncate()

if __name__ == "__main__":
    # execute only if run as a script
	# app()
    read_data()