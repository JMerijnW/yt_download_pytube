import requests
from pytube import YouTube

# 'https://i.ytimg.com/vi/dQw4w9WgXcQ/sddefault.jpg'



yt_url = 'https://www.youtube.com/watch?v=8dGZsyV8WgU'

yt_ob = YouTube(yt_url)

url = yt_ob.thumbnail_url



r = requests.get(url, allow_redirects=True)

open(f'C:\\Users\\Merijn Willemsen\\Desktop\\{yt_ob.title}.png', 'wb').write(r.content)
