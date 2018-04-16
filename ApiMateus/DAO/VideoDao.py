from Database.CreateDatabase import *
from Helper.VideoHelper import VideoHelper
from bson import ObjectId
from Models.Video import Video

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
            
        def buscaVideoId(self, id):
            videos = Videos.find({"_id": ObjectId(id)})
            return VideoHelper.montaVideos(self, videos, id)

    class Insere:
        
        def inserirVideo(self, objeto):
            try:
                post = objeto
                video = Videos.insert_one(post)
                return True
            except:
                return False

    class Atualiza:

        def atualizaVideo(self, objeto):
            put = objeto
            video = Video(put.get('Id'),
                            put.get('Nome'),
                            put.get('Url'),
                            put.get('Tipo'),
                            put.get('Album'))
            alteracao = VideoDao.Busca.buscaVideoId(self, video.Id)
            Retorno = VideoDao.Atualiza.verificaAtualizacao(self, video, alteracao)
            if Retorno == "Não existem alterações":
                return "Não existem alterações"
            if Retorno == "Alterado com sucesso":
                return True
            else:
                return False
            
        def atualizaVideoUrl(self, video):
            Videos.update_one(
                {'_id': ObjectId(video.Id)},
                {
                    "$set":{
                        "Url" : video.Url
                    }
                }
            )

        def atualizaVideoTipo(self, video):
            Videos.update_one(
                {'_id': ObjectId(video.Id)},
                {
                    "$set":{
                        "Tipo" : video.Tipo
                    }
                }
            )

        def atualizaVideoNome(self, video):
            Videos.update_one(
                {'_id': ObjectId(video.Id)},
                {
                    "$set":{
                        "Nome" : video.Nome
                    }
                }
            )
        
        def atualizaVideoAlbum(self, video):
            Videos.update_one(
                {'_id': ObjectId(video.Id)},
                {
                    "$set":{
                        "Album" : video.Album
                    }
                }
            )

            
        def verificaAtualizacao(self, video, alteracao):
            if video.Url != alteracao['Url']:
                VideoDao.Atualiza.atualizavideoUrl(self, video)

            if video.Tipo != alteracao['Tipo']:
                VideoDao.Atualiza.atualizavideoTipo(self, video)

            if video.Nome != alteracao['Nome']:
                VideoDao.Atualiza.atualizavideoNome(self, video)
            
            if video.Album != alteracao['Album']:
                VideoDao.Atualiza.atualizavideoAlbum(self, video)
            
            else:
                return ('Não existem alterações')
            
            return ('Alterado com sucesso')