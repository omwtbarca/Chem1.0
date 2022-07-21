'''
import requests
from bs4 import BeautifulSoup
import re
#input("链接，兄弟")
r = requests.get('http://www.kugou.com/share/1QQNZ43y3V3.html?id=1QQNZ43y3V3#hash=7503F5CCEC10F070CD7A9FC434666D75&album_id=35318328')
soup = BeautifulSoup(r.text, 'html.parser')

with requests.Session() as req:
    for item in soup.select("#playlist"):
        for href in item.findAll("a"):
            href = href.get("href")
            name = re.search(r"([^\/]+$)", href).group()
            if '.' not in name[-4]:
                name = name[:-3] + '.mp3'
            else:
                pass
            print(f"Downloading File {name}")
            download = req.get(href)
            if download.status_code == 200:
                with open(name, 'wb') as f:
                    f.write(download.content)
            else:
                print(f"Download Failed For File {name}")
 
'''        
# importing packages
from pytube import YouTube
import os
  
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")