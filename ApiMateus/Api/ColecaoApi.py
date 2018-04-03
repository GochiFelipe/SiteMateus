from flask_restful import Resource, reqparse
from Models.Album import Album
from DAO.ColecaoDao import ColecaoDao

class ColecaoApi(Resource):
    def get(self, tipo):
        try:
            return ColecaoDao.Busca.buscaColecaoTipo(self, tipo)
        except:
            return ('Não Existem Registros')

    def post(self, tipo):
        try:
            parser_principal = reqparse.RequestParser()
            parser_principal.add_argument('Tipo')
            parser_principal.add_argument('Album', type = Album.albumParser, action='append')
            args_principal = parser_principal.parse_args()
            adicionaColecao = ColecaoDao.Insere.inserirColecao(self, args_principal)
            return adicionaColecao
        except:
            return('Objeto Incompleto')
    
'''
        parser_album = reqparse.RequestParser()
        print(parser_album)
        parser_album.add_argument('Nome',type = str, location=('Album',))
        args_album = parser_album.parse_args(req=parser_principal)
        print (args_album['Nome'])
        

        print (args_principal['Tipo'], args_principal['Album'])
'''
