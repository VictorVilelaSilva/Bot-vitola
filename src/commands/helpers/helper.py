import os
from pytubefix import YouTube
from commands.helpers.pathUtils import get_audio_path

def download_video(link):
    try:
        yt = YouTube(link)
        yt_title = yt.title
        ys = yt.streams.get_highest_resolution()
        ys = yt.streams.filter(only_audio=True).first()

        # Começa o download
        arquivo = ys.download(output_path=get_audio_path(""))
        thumbnail = yt.thumbnail_url

        # troca o nome do arquivo para mp3
        base, ext = os.path.splitext(arquivo)
        novo_arquivo = base + ".mp3"
        if os.path.exists(novo_arquivo):
            return novo_arquivo, yt_title
        os.rename(arquivo, novo_arquivo)
        dest_path = get_audio_path(os.path.basename(novo_arquivo))

        print(f"\nDownload concluído! {dest_path}")

        return dest_path, yt_title, thumbnail
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        exit()

def get_yt_title(link):
    return YouTube(link).title

def get_yt_thumbnail(link):
    return YouTube(link).thumbnail_url

def write_error_log(error):
    with open("assets/error_log.txt", "a") as f:
        f.write(f"{error}\n")
        f.close()