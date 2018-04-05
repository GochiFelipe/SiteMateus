from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *

class ColecaoDao:

    class Busca:

        def buscaVideoTipo(self, tipo):
            #try:
                videos = Videos.find({"Tipo":tipo.lower()})
                return VideoDao.montaObjeto(self, videos)
        
            #except:
            #    return ('Sem conexão com o Banco')

    def montaObjeto(self, objeto):
        for itens in objeto:
            pprint(itens)
            Id = str(itens.get('_id'))
            Videos = Video.recuperaVideos(self, itens)
            Tipo = itens.get("Tipo")
            colecao = Colecao(Tipo, Albuns)
            return {'Id' : Id,
                    'Tipo' : Tipo,
                    'Album' : colecao.Album }