from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *
from Helper.GaleriaHelper.GaleriaHelper import GaleriaHelper

class GaleriaDao:
    
    class Busca:

        def buscaGaleria(self):
            try: 
                galerias = Galeria.find({},{"Galeria": 1, "_id": 0})
                return GaleriaHelper.montaListaGaleria(self, galerias)
            except:
                return ('Sem conexão com o Banco')

        def buscaGaleriaColecao(self, galeria):
            #try:
                galerias = Galeria.find({"Galeria": galeria.lower()})
                return GaleriaHelper.montaGaleriaColecao(self, galerias)
            #except:
            #    return ('Sem conexão com o Banco')
                
    class Insere:

        def inserirGaleria(self, objeto):
            try:
                post = objeto
                colecao = Colecoes.insert_one(post)
                return True
            except:
                return False