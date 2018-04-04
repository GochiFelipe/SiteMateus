from flask import Flask
from flask_restful import Api
import os

app = Flask(__name__)
api = Api(app)


from Database import CreateDatabase

from Views import Index
from Views import Adicionar
from AdminMateus import app
from Api.ColecaoApi import ColecaoApi
from Api.AlbumApi import AlbumApi
from Api.ColecoesApi import ColecoesApi

api.add_resource(ColecoesApi, '/api/colecao')
api.add_resource(ColecaoApi, '/api/colecao/<string:tipo>')
api.add_resource(AlbumApi, '/api/colecao/<string:tipo>/album/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)