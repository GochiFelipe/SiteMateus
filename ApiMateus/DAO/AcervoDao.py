from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *
from Helper.AcervoHelper.AcervoHelper import AcervoHelper

class AcervoDao:
    
    class Busca:

        def buscaAcervo(self):
            try: 
                acervo = Acervos.find({},{"Acervo": 1, "_id": 0})
                return AcervoHelper.montaListaAcervo(self, acervo)
            except:
                return ('Sem conexão com o Banco')

        def buscaAcervoColecao(self, acervo):
            try:
                acervos = Acervos.find({"Acervo": acervo.lower()})
                return AcervoHelper.montaAcervoColecao(self, acervos)
            except:
                return ('Sem conexão com o Banco')
                
    class Insere:

        def inserirAcervo(self, objeto):
            try:
                post = objeto
                colecao = Colecoes.insert_one(post)
                return True
            except:
                return False