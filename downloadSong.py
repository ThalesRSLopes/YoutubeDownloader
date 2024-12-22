from pytubefix import YouTube
from pytubefix.cli import on_progress


video = YouTube("https://www.youtube.com/watch?v=-zdHJa5AKzs")
audio = video.streams.filter(only_audio=True).first()
audio.download("Downloads")
