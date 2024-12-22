from pydub import AudioSegment, utils
import os


#download_path = 'D:\\0THALES\\musica'
download_path = 'Downloads'

arquivos = os.listdir(download_path)

for arquivo in arquivos:
    try:
        if not arquivo.__contains__("mp3"):
            caminho = os.path.join(download_path, arquivo)
            novo_nome = os.path.splitext(caminho)[0] + '.mp3'

            if os.path.isfile(novo_nome):
                os.remove(novo_nome)

            converted_audio = AudioSegment.from_file(caminho)
            converted_audio.export(novo_nome, format='mp3')

            os.remove(caminho)
    except:
        print("")
