import urllib.request
import re
from bs4 import BeautifulSoup

#you need beautifulsoup4 installed: "pip install beautifulsoup4"
#images are saved to the same directory of this script

def getImagesFromUrl(url):
    website = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    c=0
    img=website.findAll('img')
    for i in img:
        urllib.request.urlretrieve(i.get('src'), "image"+str(c)+".jpg")
        c+=1
    print('finished')

getImagesFromUrl('http://cutepugpics.com/')
