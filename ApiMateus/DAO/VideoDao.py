from Database.CreateDatabase import *
from Helper.VideoHelper.VideoHelper import VideoHelper
from bson import ObjectId


class VideoDao:

    class Busca:

        def buscaVideoTipoId(self, tipo, idAlbum, id):
            try:
                videos = Videos.find({"_id":ObjectId(id),"Tipo":tipo.lower()})
                return VideoHelper.montaVideos(self, videos)
            except:
                return ('Sem conexão com o Banco')
        
        def buscaVideoAlbum(self, album):
            try:
                videos = Videos.find({"Album":album})
                return VideoHelper.montaVideos(self, videos)
            except:
                return ('Sem conexão com o Banco')
            
    class Insere:
        
        def inserirVideo(self, objeto):
            try:
                post = objeto
                video = Videos.insert_one(post)
                return True
            except:
                return False