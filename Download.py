
from unittest import result
from pytube import YouTube

link = input('----Cole aqui a URL---- 👉 ')
path = ('C:\Videos')
yt = YouTube(link)
result = {
    "Titulo": yt.title,
    "Numero de views": yt.views,
    "Tamanho do video": yt.length
}
print(result)
print("Baixando.....")

ys = yt.streams.get_highest_resolution()
ys.download(path)

print('Download concluido')