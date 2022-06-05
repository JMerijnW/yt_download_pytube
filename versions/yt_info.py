import pytube
#from pytube import YouTube


video_url = 'https://www.youtube.com/watch?v=FHhZPp08s74'#'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
youtube_ob = pytube.YouTube(video_url)

print("Title:")
print(youtube_ob.title)
print("Video id:")
print(youtube_ob.video_id)
print("Description: ")
print(youtube_ob.description)
print("Length:")
print(youtube_ob.length)
print("Thumbnail url:")
print(youtube_ob.thumbnail_url)
print("Views:")
print(youtube_ob.views)
print("Ratings:")
print(youtube_ob.rating)
print("Age Resticted:")
print(youtube_ob.age_restricted)
print("Author:")
print(youtube_ob.author)
print("metadata:")
print(youtube_ob.metadata)
print("div")
print(youtube_ob.channel_url)
print(youtube_ob.publish_date)

'''
info to write as metadata
youtube_ob.title
youtube_ob.video_id ????
youtube_ob.length ?????
youtube_ob.thumbnail_url Mee Bezig
youtube_ob.author


'''



# google blijft de API vernaderen.
# the regex problem again
# search and change it again.

streams = youtube_ob.streams
#for i in streams:
    #print(i)



#for i in streams.filter(only_audio=True).filter(file_extension='mp4'):
 #   print(i)
print(streams.get_audio_only())


#print(streams.filter(only_audio=True, file_extension='mp4', abr=True))


#i.download(r"C:\Users\Merijn Willemsen\Desktop")


#stream_2 = youtube_ob.streams.get_by_itag(22)
#stream_2.download()

#electra heart
#https://www.youtube.com/playlist?list=OLAK5uy_lqWJL-WRi98XnHg3y0h82BtIeQfypvaBQ


video = youtube_ob.streams.first()
video.download(r"C:\Users\Merijn Willemsen\Desktop") # './yt_download')
