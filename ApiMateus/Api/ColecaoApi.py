from flask_restful import Resource, reqparse
from Models.Album import Album
from DAO.ColecaoDao import ColecaoDao
from DAO.AlbumDao import AlbumDao
class ColecaoApi(Resource):
    def get(self, galeria, tipo = None):
        if tipo:
            try:
                return ColecaoDao.Busca.buscaColecaoTipo(self, tipo)
            except:
                return ('Não Existem Registros')
        else:
            try:
                return ColecaoDao.Busca.buscasColecoes(self)
            except:
                return ('Não Existem Registros')

    def post(self,galeria, tipo = None):
        if tipo:
            pass
        else:
            try:
                parser = reqparse.RequestParser()
                parser.add_argument('Galeria')
                parser.add_argument('Tipo')
                args_principal = parser.parse_args()
                adicionaColecao = ColecaoDao.Insere.inserirColecao(self, args_principal)
                return adicionaColecao
            except:
                return('Objeto Incompleto')

    def put(self, galeria, tipo = None):
        if tipo:
            parser = reqparse.RequestParser()
            parser.add_argument('Id')
            parser.add_argument('Tipo')
            parser.add_argument('Galeria')
            args_principal = parser.parse_args()
            return ColecaoDao.Atualiza.atualizaColecao(self, args_principal)
        else:
            pass

    def delete(self, galeria, tipo = None):
        if galeria and tipo:
            deletaColecao = ColecaoDao.Deleta.deletaColecao(self, galeria, tipo)
            return deletaColecao
        else:
            pass