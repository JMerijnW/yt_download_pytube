from os import rename
import pytube
from re import sub as substitute_char

from mutagen.id3 import ID3NoHeaderError, ID3
#from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK
from mutagen import File


# https://www.youtube.com/c/AdrianvonZiegler/videos
# 'https://www.youtube.com/playlist?list=OLAK5uy_nOec1NsdiJMuvFg83NmyAULE2qhXkEl6E'


url = 'https://www.youtube.com/playlist?list=OLAK5uy_lqWJL-WRi98XnHg3y0h82BtIeQfypvaBQ'#'https://www.youtube.com/playlist?list=OLAK5uy_n_8iG8RL4K8n1vr-yEoFrIAO_ZOuCe79U'
locatie = r"C:\Users\Merijn Willemsen\Desktop"



playlist = pytube.Playlist(url)
print('Number of videos in playlist: %s' % len(playlist.video_urls))



for vid in playlist:
    yt_ob = pytube.YouTube(vid)
    stream = yt_ob.streams.get_audio_only()

    file_name = substitute_char("[<>:\*\?\\\/\|\"\.]", "□", yt_ob.title)
    # /\ vervangen door ~
    file_location = locatie + "\\" + file_name


    #
    print(f'url: {vid}\n'
          f'title: {yt_ob.title}\n'
          f'filename: {file_name}\n'
          f'stream: {stream}')
    stream.download(locatie, filename=file_name+".mp3")
    print("downloaded")

    try:
        print("renamed")
    except FileExistsError:
        print(f"{file_name} bestaat al")
    # TODO adding metadata
    print('---')

'''
    try:
        meta = ID3(audio_file)
    except ID3NoHeaderError:
        meta = File(audio_file, easy=True)
        print(meta)
        meta.add_tags()
        meta.save()
        print(meta)
'''

#MARINA AND THE DIAMONDS - PRIMADONNA [Official Music Video]  ♡ ELECTRA HEART PART 411 ♡

#mp4
#MARINA AND THE DIAMONDS - PRIMADONNA [Official Music Video] | ♡ ELECTRA HEART PART 411 ♡

#mp3
#MARINA AND THE DIAMONDS - PRIMADONNA [Official Music Video] | ♡ ELECTRA HEART PART 411 ♡
