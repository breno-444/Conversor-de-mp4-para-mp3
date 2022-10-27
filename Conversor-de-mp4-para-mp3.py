'''
  bibliotecas para serem instaladas
  pip install moviepy
  pip install glob
'''
from unittest import result
from pytube import YouTube
import os
from moviepy.editor import *
import glob

link = input('Cole aqui a URL---- 👉 ')
path = ('C:\Videos')
yt = YouTube(link)
result = {
    "Titulo": yt.title,
    "Tamanho do video": yt.length
}
print(result)
print("Baixando.....")

ys = yt.streams.get_highest_resolution()
ys.download(path)

print('Download concluido')

"""---------------------------------------------------------------"""
print('-'*20)

lista_mp4 = glob.glob('C:\Videos\*.mp4')
for video in lista_mp4:
  print('Lendo arquivo mp4')
  print('-'*20)
  mp4 = VideoFileClip(os.path.join(video))
  nome_mp3 = video[:-4]+'.mp3'
  print('Convertendo para mp3')
  mp4.audio.write_audiofile(os.path.join(nome_mp3))
  print('-'*20)
  print('Converteu mp4 ' + video + ' para mp3 ' + nome_mp3)
  print("Tudo Certo 👍")