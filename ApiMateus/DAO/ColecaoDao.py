from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *

from Helper.ColecaoHelper.ColecaoHelper import ColecaoHelper

class ColecaoDao:

    class Busca:

        def buscaColecaoTipo(self, tipo, parametro = None):
            try:
                colecoes = Colecoes.find({"Tipo":tipo.lower()})
                return ColecaoHelper.montaColecaoAlbuns(self, colecoes, parametro)
        
            except:
                return ('Sem conexão com o Banco')
            
        def buscasColecoes(self):
            colecoes = Colecoes.find({},{"Tipo":1, "_id": 0})
            return ColecaoHelper.montaListaColecoes(self, colecoes)


        #def buscaColecaoId(self, id):
        #    try:
        #        colecoes = Colecoes.find({"_id":ObjectId(id)})
        #        return ColecaoHelper.montaColecaoAlbuns(self, colecoes, None)
        #
        #    except:
        #        return ('Sem conexão com o Banco')

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
        #def atualizaColecao(self, objeto, id):
        #    put = objeto
        #    objetoAlterar = ColecaoDao.Busca.buscaColecaoId(self, id)
        #    colecaoAtualizada = Colecoes.replace_one(put, objetoAlterar)
        #    print(colecaoAtualizada)
        #    print (colecaoAtualizada.matched_count)
        #    return objetoAlterar
    
    class Deleta:
        pass