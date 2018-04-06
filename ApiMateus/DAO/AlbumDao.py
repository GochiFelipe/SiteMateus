from flask_restful import Resource
from Database.CreateDatabase import Albuns
from bson import ObjectId
from Models.Album import Album
from Models.Video import *
from Models.Foto import *

from Helper.AlbumHelper.AlbumHelper import AlbumHelper

class AlbumDao:

    class Busca:

        def buscaAlbumIdTipo(self, tipo, id):
            albuns = Albuns.find({"_id":ObjectId(id),"Tipo":tipo.lower()})
            return AlbumHelper.albumHelper(self, albuns, id)
        
    class Insere:

        def inserirAlbum (self, objeto):
            try:
                post = objeto
                album = Albuns.insert_one(post)
                return True
            except:
                return False

    class Atualiza:
        pass
    
    class Deleta:
        pass
