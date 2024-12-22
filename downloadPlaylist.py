from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress


download_path = 'D:\\0THALES\\musica'
playlist_url = 'https://www.youtube.com/watch?v=8bwBDImoniw&list=PLMjwKxlkmGEeGcEuqZBy08pgkc6JuFXHA'
playlist = Playlist(playlist_url)

for url in playlist:
    try:
        video = YouTube(url, on_progress_callback=on_progress)
        print(f"Baixando o áudio do vídeo: {video.title}")
        audio = video.streams.filter(only_audio=True, file_extension="mp4")
        audio_path = audio.get_audio_only().download(download_path)
    except:
        print(f"Falha ao baixar o aúdio do vídeo")
