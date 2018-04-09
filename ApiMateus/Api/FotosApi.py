from flask_restful import Resource, reqparse
from DAO.FotoDao import FotoDao
from Helper.FotoHelper.FotoHelper import FotoHelper

class FotosApi(Resource):

    def get(self, tipo, idAlbum = None, id= None):
        if idAlbum and id:
            try:
                return FotoDao.Busca.buscaFotoTipoId(self, tipo,idAlbum, id)
            except:
                return ('Não Existem Registros')
        else:
            pass

    def post(self, tipo):
        parser = reqparse.RequestParser()
        parser.add_argument('Url')
        parser.add_argument('Tipo')
        parser.add_argument('Local')
        parser.add_argument('Album')
        parser.add_argument('Tag', action='append')
        args_principal = parser.parse_args()
        adicionaFoto = FotoDao.Insere.inserirFoto(self, args_principal)
        return adicionaFoto
