import logging as log
import pytube

from pytube.exceptions import PytubeError, VideoUnavailable
from os import rename



# logging.basicConfig(filename="../downloaded.log")
# logging.basicConfig(format='%(asctime)s-%(levelname)s: %(message)s', level=logging.INFO)
log.basicConfig(filename="../downloaded.log", level=log.INFO,
                format='%(asctime)s-%(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')

print("-"*20)
log.info("-"*20)
log.info("Running: {0}".format(__file__))



def check_url(url):
    return True


def download_vid(input_url, locatie='../downloads'):  # arg: stream
    print(input_url)

    if (check_url(input_url) == False):
        # TODO check for valid url
        print("Invalid")
        # todo new file excactly the same
    else:
        try:  # TODO try: except
            yt_ob = pytube.YouTube(input_url)
            yt_download = yt_ob.streams.get_audio_only()  # audio stream met de hoogste bitrate
            # .filter(file_extension='mp4' / only_audio=True) | misch. geen .mp4 en moet dus wel .wav gebruiken

            print(yt_ob.title + "\n" + url + "\n")
            log.info("Title: {0}".format(yt_ob.title))

            print("Best bitrate stream:")
            print(yt_download)
            log.info("Stream: {0}".format(yt_download))

            yt_download.download(locatie)
            log.info("Downloading: {0}".format(input_url))

            # correct file metadata
            rename(locatie+"/"+yt_ob.title+".mp4", locatie+"/"+yt_ob.title+".mp3")
            # pytube only gives .mp4 so this converts it



        except VideoUnavailable as err:
            print(f'Video {url} is unavaialable, skipping.')
            log.error(f"{err}")
        except PytubeError as err:
            print(f"Generic error: \n{err}")
            log.error(f"{err}")
        except OSError as err:  # except FileExistsError:
            print(f"Can't open file: \n{err}")
            log.error(f"{err}")
    print("Done!\n---")
    log.info("---")




url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
# https://www.youtube.com/watch?v=13xLipyk2xA

'''
yt_ob = pytube.YouTube('https://www.youtube.com/watch?v=YDJZlPTFol8&list=PLIuMnu__lJkHs-FeeTvhx-T6Gs15-kfgc&index=2')
yt_download = yt_ob.streams.get_audio_only()
yt_download.download('../downloads')
'''
'''
if not invalid
    download
else
    skip
---
if video
    1x download
elif playlist
    ?x download
else
    ???
'''

download_vid(url)

# input("Press Enter to continue...")
