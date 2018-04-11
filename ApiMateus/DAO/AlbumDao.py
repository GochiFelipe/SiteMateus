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
            album = Album(put.get('_id'),
                            put.get('Nome'),
                            put.get('FotoCapa'),
                            put.get('Tipo')
                        )
            Retorno = AlbumHelper.verificaAlteracao(self, album, Albuns)
            if Retorno == 'Não existe alterações' :
                return 'Não existe alterações'
            if Retorno == 'Alterado Com Sucesso':
                return True
            else:
                return False
    
    class Deleta:
        pass
