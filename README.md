Esse projeto é uma aplicação em Python, que serve para fazer o download de um video do YouTube e converter ele para MP3.
Nesse projeto está três arquivos, download(faz o download de um video através de um link do youtube), conversor(que passa de mp4 para mp3), conversor-de-mp4-para-mp3(é a junção dos dois codigos, ele faz o download e converte automaticamente).

Para executar o codigo abra o arquivo "Conversor-de-mp4-para-mp3.py",  coloque no "path" e no "lista_mp4" o caminho da pasta que ficara o video (crie uma pasta no disco local C:\ para evitar bugs).


#exemplo
"path = ('C:\Videos')"
"lista_mp4 = glob.glob('C:\Videos\*.mp4')"


Após fazer esse passos basta executar e colocar a URL do video.