from flask_restful import Resource, reqparse
from Models.Album import Album
from DAO.GaleriaDao import GaleriaDao

class GaleriaApi(Resource):
    def get(self, galeria = None):
        if galeria:
            #try:
                return GaleriaDao.Busca.buscaGaleriaColecao(self, galeria)
            #except:
            #    return ('Não Existem Registros')
        else:
            try:
                return GaleriaDao.Busca.buscaGaleria(self)
            except:
                return ('Não Existem Registros')
    
    def post(self, galeria = None):
        if galeria:
            pass
        else:
            try:
                parser = reqparse.RequestParser()
                parser.add_argument('galeria')
                args_principal = parser.parse_args()
                adicionaGaleria = GaleriaDao.Insere.inserirGaleria(self, args_principal)
                return adicionaGaleria
            except:
                return('Objeto Incompleto') 