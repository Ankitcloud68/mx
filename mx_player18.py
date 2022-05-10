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
s11=input("""1.144P
2.180P
3.216P
4.270P
5.360P
6.480
7.720P
8.1080P
""")
a111=input("Enter file name: ")
a1=scraper.get(a14).text
soup4=BeautifulSoup(a1,'html.parser')
#print(soup4.prettify())
with open('s86.txt','w',encoding='utf-8')as s4:
    for i in soup4.prettify():
        s4.write(i)

'''count=0
with open('a84.m3u8','r',encoding='utf-8')as s4:
    for i in s4:
        if i.startswith('#'):
            continue
        count+=1'''

def video(s11):
    global a71
    global outer
    global a11
    a11=soup4.find_all("script",type="application/ld+json")
#contentUrl
    outer = re.compile("https://llvod.mxplay.com/video/(.*.m3u8)")
#print(outer.search(str(a11)))
    a82=outer.search(str(a11))
    a41=a82.group(0)
    s41=requests.get(a41)
    m3u8_4=m3u8.loads(s41.text)
    #print(a41[0:68]+m3u8_4.data['playlists'][0]['uri'])
    #a71=a41[0:68]+m3u8_4.data['playlists'][0]['uri']
    #a71=a41[0:68]+'h264_720_high_3000k.m3u8'
    #print(a71)
    if s11=='1':
          a71=a41[0:68]+'h264_144_high_60k.m3u8'
    elif s11=='2':
        a71=a41[0:68]+'h264_144_high_60k.m3u8'
    elif s11=='3':
        a71=a41[0:68]+'h264_216_high_375k.m3u8'
    elif s11=='4':
       a71=a41[0:68]+'h264_270_high_500k.m3u8'
    elif s11=='5':
        a71=a41[0:68]+'h264_360_high_750k.m3u8'
    elif s11=='6':
       a71=a41[0:68]+'h264_480_high_1750k.m3u8'
    elif s11=='7':
        a71=a41[0:68]+'h264_720_high_3000k.m3u8'
    elif s11=='8':
        a71=a41[0:68]+'h264_1080_high_5800k.m3u8'
    else:
        print('Here wrong input Bro check this')




def audio():
    global a81
    a82=outer.search(str(a11))
    a41=a82.group(0)
    a81=a41[0:68]+'iframe_h264_high_h264_high_audio_128000_0_64.m3u8'
    print(a81)


video(s11)
audio()
os.system('ffmpeg -i %s -i %s -c:v copy -c:a aac %s.mp4'%(a71,a81,a111))

    








