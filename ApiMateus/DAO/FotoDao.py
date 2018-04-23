from Database.CreateDatabase import *
from Helper.FotoHelper import FotoHelper
from bson import ObjectId
from Models.Foto import Foto


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

        def buscaFotoId(self, id):
            fotos = Fotos.find({"_id": ObjectId(id)})
            return FotoHelper.montaFotos(self, fotos, id)
            
    class Insere:
        
        def inserirFoto(self, objeto):
            try:
                post = objeto
                foto = Fotos.insert_one(post)
                return True
            except:
                return False

    class Atualiza:

        def atualizaFoto(self, objeto):
            put = objeto
            foto = Foto(put.get('Id'),
                            put.get('Url'),
                            put.get('Tipo'),
                            put.get('Local'),
                            put.get('Album'),
                            put.get('Tags'))
            alteracao = FotoDao.Busca.buscaFotoId(self, foto.Id)
            Retorno = FotoDao.Atualiza.verificaAlteracao(self, foto, alteracao)

            if Retorno == "Não existem alterações":
                return "Não existem alterações"
            if Retorno == "Alterado com sucesso":
                return True
            else:
                return False

        def atualizaFotoUrl(self, foto):
            Fotos.update_one(
                {'_id': ObjectId(foto.Id)},
                {
                    "$set":{
                        "Url" : foto.Url
                    }
                }
            )

        def atualizaFotoTipo(self, foto):
            Fotos.update_one(
                {'_id': ObjectId(foto.Id)},
                {
                    "$set":{
                        "Tipo" : foto.Tipo
                    }
                }
            )

        def atualizaFotoLocal(self, foto):
            Fotos.update_one(
                {'_id': ObjectId(foto.Id)},
                {
                    "$set":{
                        "Local" : foto.Local
                    }
                }
            )
        
        def atualizaFotoAlbum(self, foto):
            Fotos.update_one(
                {'_id': ObjectId(foto.Id)},
                {
                    "$set":{
                        "Album" : foto.Album
                    }
                }
            )
        
        def atualizaFotoTags(self, foto):
            Fotos.update_one(
                {'_id': ObjectId(foto.Id)},
                {
                    "$set":{
                        "Tags" : foto.Tags
                    }
                }
            )

        def verificaAlteracao(self, foto, alteracao):
            if foto.Url != alteracao['Url']:
                FotoDao.Atualiza.atualizaFotoUrl(self, foto)

            if foto.Tipo != alteracao['Tipo']:
                FotoDao.Atualiza.atualizaFotoTipo(self, foto)

            if foto.Local != alteracao['Local']:
                FotoDao.Atualiza.atualizaFotoLocal(self, foto)
            
            if foto.Album != alteracao['Album']:
                FotoDao.Atualiza.atualizaFotoAlbum(self, foto)
            
            if foto.Tags != alteracao['Tags']:
                FotoDao.Atualiza.atualizaFotoTags(self,foto)
            
            else:
                return ('Não existem alterações')
            
            return ('Alterado com sucesso')
    
    class Deleta:
        def deletaFoto(self, galeria, tipo, idAlbum, id):
            try:
                Fotos.delete_one({
                    "Tipo":tipo,
                    "_id": ObjectId(id)
                })
                return True
            except:
                return False