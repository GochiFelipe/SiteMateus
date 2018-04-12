from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Colecao import Colecao

from Helper.ColecaoHelper import ColecaoHelper

class ColecaoDao:

    class Busca:

        def buscaColecaoTipo(self, tipo, parametro = None):
            try:
                colecoes = Colecoes.find({"Tipo":tipo.lower()})
                return ColecaoHelper.montaColecaoAlbuns(self, colecoes)

            except:
                return ('Sem conexão com o Banco')
            
        def buscasColecoes(self):
            try:
                colecoes = Colecoes.find({},{"Tipo":1, "_id": 0})
                return ColecaoHelper.montaListaColecoes(self, colecoes)
            except:
                return ('Sem conexão com o Banco')

        def buscaColecaoGaleria(self, galeria):
            try:
                colecoes = Colecoes.find({"Galeria": galeria.lower()})
                return ColecaoHelper.montaColecaoAlbuns(self, colecoes)
            except:
                return('Sem conexão com o Banco')

        def buscaColecaoId(self, id):
            try:
                colecoes = Colecoes.find({"_id":ObjectId(id)})
                return ColecaoHelper.montaColecaoAlbuns(self, colecoes)
        
            except:
                return ('Sem conexão com o Banco')

    class Insere:

        def inserirColecao(self, objeto):
            try:
                post = objeto
                Colecoes.insert_one(post)
                return True
            except:
                return False

    class Atualiza:
        def atualizaColecao(self, objeto):
            try:
                put = objeto
                print(put.get('Tipo'))
                print(put.get('Galeria'))
                colecao = Colecao(put.get('Id'),
                                    put.get('Tipo'),
                                    put.get('Galeria')
                                )
                alteracao = ColecaoDao.Busca.buscaColecaoId(self, colecao.Id)
                Retorno = ColecaoDao.Atualiza.verificaAlteracao(self, colecao, alteracao)
                if Retorno == 'Não existe alterações' :
                    return 'Não existe alterações'
                if Retorno == 'Alterado Com Sucesso':
                    return True
                else:
                    return False
            except:
                return False
            
        def atualizaColecaoTipo(self, colecao):
            Colecoes.update_one(
                {'_id': ObjectId(colecao.Id)},
                {
                    "$set":{
                        "Tipo" : colecao.Tipo
                    }
                }
            )

        def atualizaColecaoGaleria(self, colecao):
            Colecoes.update_one(
                {'_id': ObjectId(colecao.Id)},
                {
                    "$set":{
                        "Galeria" : colecao.Galeria
                    }
                }
            )
            
        def verificaAlteracao(self, colecao, alteracao):
            try:
                if colecao.Galeria != alteracao['Galeria']:
                    ColecaoDao.Atualiza.atualizaColecaoGaleria(self, colecao)

                if colecao.Tipo != alteracao['Tipo']:
                    ColecaoDao.Atualiza.atualizaColecaoTipo(self, colecao)

                else:
                    return ('Não existe alterações')

                return ('Alterado Com Sucesso')

            except:
                return False

    
    class Deleta:
        pass