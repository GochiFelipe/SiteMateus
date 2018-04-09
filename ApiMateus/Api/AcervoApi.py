from flask_restful import Resource, reqparse
from Models.Album import Album
from DAO.AcervoDao import AcervoDao

class AcervoApi(Resource):
    def get(self, acervo = None):
        if acervo:
            try:
                return AcervoDao.Busca.buscaAcervoColecao(self, acervo)
            except:
                return ('Não Existem Registros')
        else:
            try:
                return AcervoDao.Busca.buscaAcervo(self)
            except:
                return ('Não Existem Registros')
    
    def post(self, acervo = None):
        if acervo:
            pass
        else:
            try:
                parser = reqparse.RequestParser()
                parser.add_argument('Acervo')
                args_principal = parser.parse_args()
                adicionaColecao = AcervoDao.Insere.inserirAcervo(self, args_principal)
                return adicionaColecao
            except:
                return('Objeto Incompleto') 