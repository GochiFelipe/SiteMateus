from flask import Flask
from flask_restful import Api
import os

app = Flask(__name__)
api = Api(app)


from Database import CreateDatabase

from Views import Index
from Views import Adicionar
from AdminMateus import app
from ModelsApi.Album import AlbumApi

api.add_resource(AlbumApi, '/api/album/<string:tipo>')

if __name__ == '__main__':
    app.run(debug=True)