import requests
import cloudscraper
from bs4 import BeautifulSoup
import json
import re

scraper = cloudscraper.create_scraper(debug=True)
a14=input("Enter Mx player url here: ")
a1=scraper.get(a14).text
soup4=BeautifulSoup(a1,'html.parser')
a11=soup4.find_all("div",{"class":"slide"})
print("\n",a11)
a123=re.compile('/show/[-\w]+/[-\w]+/[-\w]+-[-\w]+')
for i in a11:
 j=str(i)
 x=a123.findall(j)
 print(x)
