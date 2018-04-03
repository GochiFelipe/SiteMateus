from flask_restful import Resource
from Database.CreateDatabase import Albuns
from bson import ObjectId
from Models.Album import Album
from Models.Video import *
from Models.Foto import *

class AlbumDao:

    class Busca:

        def buscaAlbumIdTipo(self, tipo, id):
            albuns = Albuns.find({"_id":ObjectId(id),"Tipo":tipo.lower()})
            for itens in albuns:
                Id = str(itens.get('_id'))
                Nome = itens.get('Nome')
                Videos = Video.recuperaVideos(self, itens)
                Fotos = Foto.recuperaFotos(self, itens)
                FotoCapa = itens.get('FotoCapa')
                Tipo = itens.get('Tipo')
                album = Album(Nome, FotoCapa,Tipo, Videos, Fotos)
            return {'Id' : Id,
                    'Nome': album.Nome, 
                    'Videos' : album.Videos, 
                    'Fotos' : album.Fotos,
                    'FotoCapa' : album.FotoCapa }
        
    class Insere:
        pass

    class Atualiza:
        pass
    
    class Deleta:
        pass
