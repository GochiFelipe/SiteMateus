from flask_restful import Resource
from Database.CreateDatabase import *
from pprint import pprint
from bson import json_util, ObjectId
from Helpers.ModelsHelpers import ModelsHelpers


class AlbumApi(Resource):
    def get(self, tipo):
        try:
            albuns = Albuns.find({"Tipo":tipo})
            for itens in albuns:
                pprint(itens)
                Id = str(ObjectId())
                Nome = itens.get('Nome')
                Videos = ModelsHelpers.RecuperaVideos(itens)
                Fotos = ModelsHelpers.RecuperaFotos(itens)
            return {'Id' : Id,
                    'Nome': Nome, 
                    'Videos' : Videos, 
                    'Fotos' : Fotos }
        except:
            return ("Não existe buscas com esse tipo")