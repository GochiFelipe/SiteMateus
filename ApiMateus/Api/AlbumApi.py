from flask_restful import Resource, reqparse
from DAO.AlbumDao import AlbumDao
from DAO.VideoDao import VideoDao
from DAO.FotoDao import FotoDao

class AlbumApi(Resource):
    def get(self, galeria, tipo, id = None):
        if id:
            try:
                return AlbumDao.Busca.buscaAlbumIdTipo(self, tipo, id)
            except:           
                return ('Não Existem Registros')
        else:
            try:
                return AlbumDao.Busca.buscaAlbumTipo(self, tipo)
            except:           
                return ('Não Existem Registros')

    def post(self, galeria, tipo, id = None):
        if id:
            pass
        else:
            try:
                parser = reqparse.RequestParser()
                parser.add_argument('Nome')
                parser.add_argument('Tipo')
                parser.add_argument('FotoCapa')
                args_principal = parser.parse_args()
                adicionaAlbum = AlbumDao.Insere.inserirAlbum(self, args_principal)
                return adicionaAlbum
            except:
                return('Objeto Incompleto')

    def put(self, galeria, tipo, id = None):
        if id:
            parser = reqparse.RequestParser()
            parser.add_argument('Id')
            parser.add_argument('Nome')
            parser.add_argument('FotoCapa')
            parser.add_argument('Tipo')
            args_principal = parser.parse_args()
            return AlbumDao.Atualiza.atualizaAlbum(self, args_principal)
        else:
            pass

    def delete(self, galeria, tipo, id):
        deletaAlbum = AlbumDao.Deleta.deletaAlbum(self, galeria, tipo, id)
        return deletaAlbum