from flask_restful import Resource, reqparse
from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *
from DAO.ColecaoDao import ColecaoDao
from json import JSONEncoder
class Obj(object):
    def __init__(self):
        self.nome = 'Ricardo'
        self.sobrenome = 'Alcantara'

class ColecoesApi(Resource):
    def get(self):
        try:
            colecoes = Colecoes.find({},{"Tipo":1, "_id": 0})
            Tipos = []
            for itens in colecoes:
                pprint(itens)
                Tipo = itens.get("Tipo")
                Tipos.append(Tipo)
            #return { "Tipos" : Tipos }
            obj = Obj()
            return obj.__dict__
        except:
            return ('Não Existem Registros')

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('Tipo')
            parser.add_argument('Album', type = Album.albumParser, action='append')
            args_principal = parser.parse_args()
            adicionaColecao = ColecaoDao.Insere.inserirColecao(self, args_principal)
            return adicionaColecao
        except:
            return('Objeto Incompleto')