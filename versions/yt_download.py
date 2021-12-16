import logging as log
import pytube

from pytube.exceptions import PytubeError
from os import rename
#os.mkdir("newdir")
#os.remove(file_name)
#os.rmdir('dirname') delete folder
#os.rename(current_file_name, new_file_name)
#os.getcwd() current workiing dir
#os.listdir(path) lijst bestanden



# logging.basicConfig(filename="../downloaded.log")
# logging.basicConfig(format='%(asctime)s-%(levelname)s: %(message)s', level=logging.INFO)



log.basicConfig(filename="../downloaded.log", level=log.INFO,
                format='%(asctime)s-%(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
log.info("Running: {0}".format(__file__))


def download_vid(input_url, locatie='../downloads'):  # arg: stream
    # TODO check for valid url
    link = input_url
    '''
    if (check_url(input_url)):
        link = input_url
    else:
        print("Invalid") '''
    try:
        yt_ob = pytube.YouTube(link)
        yt_download = yt_ob.streams.get_audio_only()  # alle audio streams
        # .filter(file_extension='mp4' / only_audio=True) | misch. geen .mp4 en moet dus wel .wav gebruiken

        print(yt_ob.title + "\n" + url + "\n")
        log.info("Title: {0}".format(yt_ob.title))

        print("Best bitrate stream:")
        print(yt_download)
        log.info("Stream: {0}".format(yt_download))

        yt_download.download(locatie)
        log.info("Downloading: {0}".format(link))
        # TODO rename .mp4 to .mp3
        #  rename(current_file_name, new_file_name)
    except PytubeError as err:
        print(f"Generic error: {err}")
        log.error(f"{err}")
    except OSError as err:
        print(f"Can't open file: {err}")
        log.error(f"{err}")
    finally:
        print("????????")



# TODO try: except

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# https://www.youtube.com/watch?v=dQw4w9WgXcQ | https://www.youtube.com/watch?v=13xLipyk2xA

'''
yt_ob = pytube.YouTube('https://www.youtube.com/watch?v=YDJZlPTFol8&list=PLIuMnu__lJkHs-FeeTvhx-T6Gs15-kfgc&index=2')
yt_download = yt_ob.streams.get_audio_only()
yt_download.download('../downloads')
'''


download_vid(url)

# input("Press Enter to continue...")
