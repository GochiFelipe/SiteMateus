from Database.CreateDatabase import *
from Helper.FotoHelper.FotoHelper import FotoHelper
from bson import ObjectId


class FotoDao:

    class Busca:

        def buscaFotoTipoId(self, tipo, idAlbum, id):
            try:
                fotos = Fotos.find({"_id":ObjectId(id),"Tipo":tipo.lower()})
                return FotoHelper.montaFotos(self, fotos)
            except:
                return ('Sem conexão com o Banco')
        
        def buscaFotoAlbum(self, album):
            try:
                fotos = Fotos.find({"Album":album})
                return FotoHelper.montaFotos(self, fotos)
            except:
                return('Sem conexão com o Banco')
            
    class Insere:
        
        def inserirFoto(self, objeto):
            try:
                post = objeto
                foto = Fotos.insert_one(post)
                return True
            except:
                return False