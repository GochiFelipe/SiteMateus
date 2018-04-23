from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *
from Models.Galeria import Galeria
from Helper.GaleriaHelper import GaleriaHelper
from DAO.ColecaoDao import ColecaoDao

class GaleriaDao:
    
    class Busca:

        def buscaGaleria(self):
            try: 
                galerias = Galerias.find({},{"Galeria": 1, "_id": 0})
                return GaleriaHelper.montaListaGaleria(self, galerias)
            except:
                return ('Sem conexão com o Banco')

        def buscaGaleriaColecao(self, galeria):
            try:
                galerias = Galerias.find({"Galeria": galeria.lower()})
                return GaleriaHelper.montaGaleriaColecao(self, galerias)
            except:
                return ('Sem conexão com o Banco')

        def buscaGaleriaId(self, id):
            galerias = Galerias.find({"_id":ObjectId(id)})
            return GaleriaHelper.montaGaleriaColecao(self, galerias)
                
    class Insere:

        def inserirGaleria(self, objeto):
            try:
                galeria = Galerias.insert_one(objeto)
                return True
            except:
                return False

    class Atualiza:

        def atualizaGaleria(self, objeto):
            try:
                put = objeto
                galeria = Galeria(put.get('Id'), 
                                    put.get('Galeria'))
                Galerias.update_one(
                    {'_id':ObjectId(galeria.Id)},
                    {
                        "$set":{
                            "Galeria": str(galeria.Galeria)
                        }
                    }
                )
                return True
            except:
                return False

    class Deleta:

        def deletaGaleria(self, objeto):
            try:
                Galerias.delete_one({
                    "Galeria": objeto
                })
                return True
            except:
                return False