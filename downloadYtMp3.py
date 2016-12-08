from __future__ import unicode_literals
import urllib.request, urllib.error, urllib.parse,re,os,glob, urllib.error,bs4,youtube_dl,sys
from shutil import copyfile
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC

folder="C:\\Users\\Lorenzo\\Desktop\\Web Development\\Musica da yt\\"

def changeTitleAndArtist(filename,title,artist):
      try:
          tags = ID3(filename)
      except ID3NoHeaderError:
          print("Adding ID3 header;")
          tags = ID3()
      tags["TIT2"] = TIT2(encoding=3, text=title)
      tags["TPE1"] = TPE1(encoding=3, text=artist)
      directory=folder+"tagged\\";
      if not os.path.exists(directory):
            os.makedirs(directory)
      tags.save(directory+title+".mp3")

def findTitleAndArtist(filename):
      filename=filename.lower()
      index=min(filename.find("official"),filename.find("video"),len(filename))
      if index==-1:
          filename=filename[0:len(filename)]
      else:
          filename=filename[0:min(filename.find("official"),filename.find("video"))]
      print('filename='+filename)
      filename=re.sub('\.mp3$', '', filename)
      print('filename='+filename)
      site=urllib.request.urlopen("http://search.azlyrics.com/search.php?q="+filename).read().decode(encoding='utf-8',errors='ignore')
      m=site.find('href="http://www.azlyrics.com/lyrics/')
      h=site[m:m+1000]
      soup=bs4.BeautifulSoup(h,"html.parser")
      f=soup.findAll('b')
      if len(f)>1:
            song=f[0].string
            artist=f[1].string
            return(song.title(),artist.title())

def tag():
    os.chdir(folder)
    for filename in glob.glob("*.mp3"):
        print(filename)
        try:
            title,artist=findTitleAndArtist(filename)
            print((title+" by "+artist))
            copyfile(filename,folder+"tagged\\"+title+".mp3")
            changeTitleAndArtist(folder+filename,title,artist)
            os.remove(filename)
        except:
            print("fail")

def downloadFromYt(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def downloadFromFile(fileAddress):
    with open(fileAddress, 'r+') as myfile:
        myfile.seek(0)
        first_char=myfile.read(1)
        if not first_char:
            print("file is empty!")
        else:
            myfile.seek(0)
            songs=myfile.read().split('\n')
            for song in songs:
                try :
                    downloadFromYt(song)
                except:
                    pass
            myfile.seek(0)
            myfile.truncate()

downloadFromFile(folder+'LinksOfSongsToDl.txt')#to download songs from links listed in file
#downloadFromYt('https://www.youtube.com/watch?v=NsnSQtsdMJI')#to download song from url
tag()#tries to tag the mp3s of the downloaded songs
