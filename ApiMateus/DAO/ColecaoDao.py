from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *

class ColecaoDao:

    class Busca:

        def buscaColecaoTipo(self, tipo):
            colecoes = Colecoes.find({"Tipo":tipo.lower()})
            for itens in colecoes:
                pprint(itens)
                Id = str(itens.get('_id'))
                Albuns = Album.recuperaAlbuns(self, itens)
                Tipo = itens.get("Tipo")
                colecao = Colecao(Tipo, Albuns)
            return {'Id' : Id,
                    'Album' : Albuns }

    class Insere:
        def inserirColecao(self, objeto):
            try:    
                post = objeto
                colecao = Colecoes.insert_one(post)
                return True
            except:
                return False

    class Atualiza:
        pass
    
    class Deleta:
        pass