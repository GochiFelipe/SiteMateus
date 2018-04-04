from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *

class ColecaoDao:

    class Busca:

        def buscaColecaoTipo(self, tipo):
            try:
                colecoes = Colecoes.find({"Tipo":tipo.lower()})

                for itens in colecoes:
                    pprint(itens)
                    Id = str(itens.get('_id'))
                    Albuns = Album.recuperaAlbuns(self, itens)
                    Tipo = itens.get("Tipo")
                    colecao = Colecao(Tipo, Albuns)
                return {'Id' : Id,
                        'Tipo' : Tipo,
                        'Album' : colecao.Album }
        
            except:
                return ('Sem conexão com o Banco')

        def buscaColecaoId(self, id):
            try:
                colecoes = Colecoes.find({"_id":ObjectId(id)})
                for itens in colecoes:
                    pprint(itens)
                    Id = str(itens.get('_id'))
                    Albuns = Album.recuperaAlbuns(self, itens)
                    Tipo = itens.get("Tipo")
                    colecao = Colecao(Tipo, Albuns)
                return {'Id' : Id,
                        'Tipo' : Tipo,
                        'Album' : colecao.Album }
        
            except:
                return ('Sem conexão com o Banco')

    class Insere:

        def inserirColecao(self, objeto):
            try:
                post = objeto
                colecao = Colecoes.insert_one(post)
                return True
            except:
                return False

    class Atualiza:
        def atualizaColecao(self, objeto, id):
            put = objeto
            objetoAlterar = ColecaoDao.Busca.buscaColecaoId(self, id)
            colecaoAtualizada = Colecoes.replace_one(objetoAlterar, put)
            print (colecaoAtualizada.matched_count)
            return True
    
    class Deleta:
        pass