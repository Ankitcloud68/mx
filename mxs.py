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
a1=scraper.get(a14).text
soup4=BeautifulSoup(a1,'html.parser')
with open('s86.txt','w',encoding='utf-8')as s4:
    for i in soup4.prettify():
        s4.write(i)
a11=soup4.find_all("div",{"class":"slide"})
print(a11)
outer=re.match("/show/",a11)
print(outer.group(0))
