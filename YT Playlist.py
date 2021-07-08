#imports for opening and parsing the site
from pytube import YouTube
from pytube import Playlist

#download the given video link
def download(video_link):
	try:
		yt=YouTube(video_link)
		print('Downloading: ',yt.title)
		video_to_download = yt.streams.filter(only_audio=True).first()
		video_to_download.download('YT Downloads')
	except:
		print(yt.title,' SKIPPED!!!!!!!')

input_playlist=input('Enter the youtube playlist link: ')
input_playlist_temp=input_playlist.split('&index')
play_list=Playlist(input_playlist_temp[0])

for video_link in play_list.video_urls:
	download(video_link)