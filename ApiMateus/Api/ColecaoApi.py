from flask_restful import Resource, reqparse
from Models.Album import Album
from DAO.ColecaoDao import ColecaoDao

class ColecaoApi(Resource):
    def get(self, tipo):
        #try:
            return ColecaoDao.Busca.buscaColecaoTipo(self, tipo)
        #except:
        #    return ('Não Existem Registros')

    def post(self, tipo):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('Tipo')
            parser.add_argument('Album', type = Album.albumParser, action='append')
            args_principal = parser.parse_args()
            adicionaColecao = ColecaoDao.Insere.inserirColecao(self, args_principal)
            return adicionaColecao
        except:
            return('Objeto Incompleto')
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('_id')
        parser.add_argument('Tipo')
        parser.add_argument('Album', type = Album.albumParser, action='append')
        args_principal = parser.parse_args()
        return ColecaoDao.Atualiza.atualizaColecao(self, args_principal, id)