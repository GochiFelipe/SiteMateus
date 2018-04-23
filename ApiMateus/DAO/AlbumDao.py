from flask_restful import Resource
from Database.CreateDatabase import Albuns
from bson import ObjectId
from Models.Album import Album
from Models.Video import *
from Models.Foto import *

from Helper.AlbumHelper import AlbumHelper

class AlbumDao:

    class Busca:

        def buscaAlbumIdTipo(self, tipo, id):
            albuns = Albuns.find({"_id":ObjectId(id),"Tipo":tipo.lower()})
            return AlbumHelper.montaAlbum(self, albuns, id)

        def buscaAlbumTipo(self, tipo):
            albuns = Albuns.find({"Tipo" : tipo})
            return AlbumHelper.montaAlbum(self, albuns)
        
        def buscaAlbumId(self, id):
            albuns = Albuns.find({"_id":ObjectId(id)})
            return AlbumHelper.montaAlbum(self, albuns, id)
        
    class Insere:

        def inserirAlbum (self, objeto):
            try:
                post = objeto
                album = Albuns.insert_one(post)
                return True
            except:
                return False

    class Atualiza:
        def atualizaAlbum(self, objeto):
            put = objeto
            album = Album(put.get('Id'),
                            put.get('Nome'),
                            put.get('FotoCapa'),
                            put.get('Tipo')
                        )
            alteracao = AlbumDao.Busca.buscaAlbumId(self, album.Id)
            Retorno = AlbumDao.Atualiza.verificaAlteracao(self, album, alteracao)
            print(Retorno)
            if Retorno == 'Não existe alterações' :
                return 'Não existe alterações'
            if Retorno == 'Alterado Com Sucesso':
                return True
            else:
                return False

        def atualizaAlbumNome(self, album):
            Albuns.update_one(
                    {'_id': ObjectId(album.Id)},
                    {
                        "$set":{
                            "Nome" : album.Nome
                        }
                    }
                )
        def atualizaAlbumTipo(self, album):
            Albuns.update_one(
                    {'_id': ObjectId(album.Id)},
                    {
                        "$set":{
                            "Tipo" : album.Tipo
                        }
                    }
                )
        def atualizaAlbumFotoCapa(self, album):
            Albuns.update_one(
                    {'_id': ObjectId(album.Id)},
                    {
                        "$set":{
                            "FotoCapa" : album.FotoCapa
                        }
                    }
                )

        def verificaAlteracao(self, album, alteracao):
            try:
                if album.Nome != alteracao['Nome']:
                    AlbumDao.Atualiza.atualizaAlbumNome(self, album)

                if album.Tipo != alteracao['Tipo']:
                    AlbumDao.Atualiza.atualizaAlbumTipo(self, album)
                
                if album.FotoCapa != alteracao['FotoCapa']:
                    AlbumDao.Atualiza.atualizaAlbumFotoCapa(self, album)

                else:
                    return ('Não existem alterações')

                return ('Alterado Com Sucesso')
                
            except:
                return False
    
    class Deleta:

        def deletaAlbum(self, galeria, tipo, id):
            try:
                Albuns.delete_one({
                    "Tipo": tipo,
                    "_id": ObjectId(id)                
                })
                return True
            except:
                return False