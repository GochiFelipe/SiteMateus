from flask_restful import Resource
from DAO.AlbumDao import AlbumDao

class AlbumApi(Resource):
    def get(self, tipo, id):
        try:
            return AlbumDao.Busca.buscaAlbumIdTipo(self, tipo, id)
        except:           
            return ('Não Existem Registros')

    def post(self, Tipo, Nome):
        pass