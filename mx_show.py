import requests
import cloudscraper
from bs4 import BeautifulSoup
import json
import re
import m3u8
import os
global a71
scraper = cloudscraper.create_scraper()
a14=input("Enter Mx player url here: ")
a111=x[6]
a1=scraper.get(a14).text
soup4=BeautifulSoup(a1,'html.parser')
inputs = soup4.find_all('episode-',type="webUrl")
print (inputs[0])
