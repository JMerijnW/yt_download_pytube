import pytube  
#from pytube import YouTube


video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
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


stream = youtube_ob.streams.filter(only_audio=True)#file_extension='mp4') 
for i in stream:  
    print(i)


#stream_2 = youtube_ob.streams.get_by_itag(22)
#stream_2.download()

#video = youtube_ob.streams.first()  
#video.download('./yt_download') 
