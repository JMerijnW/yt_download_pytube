from re import match as match_str
#from pytube import YouTube

# examples
'''
'https://www.youtube.com/playlist?'
'https://www.youtube.com/watch?'
'https://www.youtube.com/watch?v=pAzEY1MfXrQ'
'https://www.youtube.com/watch?v=pAzEY1MfXrQ&list=PLIuMnu__lJkHs-FeeTvhx-T6Gs15-kfgc&index=3'
'''

link = 'https://www.youtube.com/watch?v=pAzEY1MfXrQ'
pattern = ''
valid_url_regex = ("((http|https)://)(www.)?" +
                   "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                   "{2,256}\\.[a-z]" +
                   "{2,6}\\b([-a-zA-Z0-9@:%" +
                   "._\\+~#?&//=]*)")

match_str(valid_url_regex, link)


with open('../links.txt', 'r') as link_file:
    print(f"Link file: {link_file.name}\nContains: ")
    # print(link_file.readline()[:-1])  # .readline()[:-1] & .readlines() repr(link_file.read())

    for line in link_file:
        print(line)
        print(link_file.readline())
        print("\n---")




# Playlist object is a list with links
vid_list = Playlist('https://www.youtube.com/playlist?list=PLIuMnu__lJkHs-FeeTvhx-T6Gs15-kfgc')
# audio = vid_list.streams.only_audio()

'https://www.youtube.com/playlist?'
'https://www.youtube.com/watch?'
'https://www.youtube.com/watch?v=pAzEY1MfXrQ'


print(f'Playlist: {vid_list.title}\nInhoud:')

print(vid_list)


# TODO changelist
