from flask_restful import Resource, reqparse
from DAO.AlbumDao import AlbumDao
from DAO.VideoDao import VideoDao
from DAO.FotoDao import FotoDao

class AlbumApi(Resource):
    def get(self, acervo, tipo, id = None):
        if id:
            try:
                return AlbumDao.Busca.buscaAlbumIdTipo(self, tipo, id)
            except:           
                return ('Não Existem Registros')
        else:
            pass

    def post(self, acervo, tipo, id = None):
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