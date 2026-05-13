from album import AlbumPanini
from jugadores import abrir_sobre, Estampa

album = AlbumPanini("Miguel", "Pasta blanda")
estampas = abrir_sobre()
for i in estampas:
    album.pegar_estampa(i)
for i in estampas:
    album.pegar_estampa(i)
