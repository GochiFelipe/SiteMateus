from flask_restful import Resource, reqparse
from flask import Flask, jsonify, request
from Database.CreateDatabase import *
from pprint import pprint
from bson import ObjectId
from Models.Album import *
from Models.Colecao import *

class ColecaoApi(Resource):
    def get(self, tipo):
        try:
            colecoes = Colecoes.find({"Tipo":tipo.lower()})
            for itens in colecoes:
                pprint(itens)
                Id = str(itens.get('_id'))
                Albuns = Album.RecuperaAlbunsId(self, itens)
                Tipo = itens.get("Tipo")
                colecao = Colecao(Tipo, Albuns)
            return {'Id' : Id,
                    'Album' : Albuns }
        except:
            return ('Não Existem Registros')

    def post(self, tipo):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()
        print (args['username'], args['password'])
        return ({"Username": args['username'], "Password": args['password']})