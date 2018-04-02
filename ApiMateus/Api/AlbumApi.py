from flask_restful import Resource
from Database.CreateDatabase import *
from pprint import pprint
from bson import json_util, ObjectId
from Models.Album import Album
from Models.Video import *
from Models.Foto import *


class AlbumApi(Resource):
    def get(self, tipo, id):
        try:
            albuns = Albuns.find({"_id":ObjectId(id),"Tipo":tipo.lower()})
            for itens in albuns:
                Id = str(itens.get('_id'))
                Nome = itens.get('Nome')
                Videos = Video.RecuperaVideos(self, itens)
                Fotos = Foto.RecuperaFotos(self, itens)
                FotoCapa = itens.get('FotoCapa')
                Tipo = itens.get('Tipo')
                album = Album(Nome, FotoCapa,Tipo, Videos, Fotos)
            return {'Id' : Id,
                    'Nome': album.Nome, 
                    'Videos' : album.Videos, 
                    'Fotos' : album.Fotos,
                    'FotoCapa' : album.FotoCapa }
        except:           
            return ('Não Existem Registros')

    def post(self, Tipo, Nome):
        pass