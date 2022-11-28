```Script to download Youtube playlistto local environment'''
from pytube import YouTube
from pytube import Playlist
import re

DOWNLOAD_DIR = '/Users/sri/Downloads/'
playlist = Playlist('PLAYLIST_URL')
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
for url in playlist.video_urls:
    print(url)
    yt = YouTube(url)
    str=yt.streams.filter(res="720p",file_extension='mp4').first()
    str.download('/Users/srr/Downloads/')
