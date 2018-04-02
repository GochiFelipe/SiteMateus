from flask_restful import Resource
from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *

class ColecoesApi(Resource):
    def get(self):
        try:
            colecoes = Colecoes.find({},{"Tipo":1, "_id": 0})
            Tipos = []
            for itens in colecoes:
                pprint(itens)
                Tipo = itens.get("Tipo")
                Tipos.append(Tipo)
            return { "Tipos" : Tipos }
        except:
            return ('Não Existem Registros')

    def post(self, Tipo, Nome):
        pass