import urllib.request
import re
import time
from bs4 import BeautifulSoup
from random import randrange

#you need beautifulsoup4 installed: "pip install beautifulsoup4"
#images are saved to the same directory of this script

#globals
d=0
urlList=['http://sexieststockings.com/','http://www.superstockings.com/','http://fuckingnylon.com/','http://www.glamourimages.net/','https://www.instagram.com/suicide.dolls/',
             'https://www.instagram.com/gillerm/','https://www.instagram.com/belasmusas/','https://www.instagram.com/belas_brasileiras2018/','https://www.instagram.com/sublimely_stunning/',
             'https://www.instagram.com/enticing.top.models/','https://www.instagram.com/covershout/','https://www.instagram.com/babespty/','https://www.instagram.com/divulga_babes/',
             'https://www.instagram.com/mad__shouts/','https://www.instagram.com/divulgando_brasil11/','https://www.instagram.com/oz_0/']

def saveNImagesFromUrl(url,n):
    print(url)
    global d
    website = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    if 'instagram' in url:
        site=str(urllib.request.urlopen(url).read())
        soup = BeautifulSoup(site,"html.parser")
        c=0
        skip=4
        for a,b in [(m.start(0), m.end(0)) for m in re.finditer(r'https://scontent-mxp1-1.cdninstagram.com/', site)]:
            c+=1
            if (c<skip or c&1):
                continue
            i=b
            while (site[i]!=' '):
                i+=1
            src=site[a:i-1]
            urllib.request.urlretrieve(src, time.strftime("%d_%m_%Y")+"_image"+str(d)+".jpg")
            d+=1
            if (d>n):
                break;
        if d<n:
            print('not enough images, starting again')
            figaTime(n-d)
    else:
        img=website.findAll('img')
        skip=5
        n+=skip
        for i in img:
            d+=1
            if (d<skip):
                continue
            urllib.request.urlretrieve(url+i.get('src'), time.strftime("%d_%m_%Y")+"_image"+str(d)+".jpg")
            if (d>=n):
                break;
    print('finished')

def figaTime(n):
    #todo: scheduler, send in whatsapp
    #saving 10 images from random site
    random_index = randrange(0,len(urlList))
    saveNImagesFromUrl(urlList[random_index],n)
    #todo: send in whatsapp
    
figaTime(10)
