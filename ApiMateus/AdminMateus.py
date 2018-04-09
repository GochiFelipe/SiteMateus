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
from Api.VideosApi import VideosApi
from Api.FotosApi import FotosApi
from Api.AcervoApi import AcervoApi


api.add_resource(AcervoApi, '/api/acervo', 
        '/api/acervo/<string:acervo>')
api.add_resource(ColecaoApi,'/api/acervo/<string:acervo>/colecao', 
        '/api/acervo/<string:acervo>/colecao/<string:tipo>')
api.add_resource(AlbumApi,'/api/acervo/<string:acervo>/colecao/<string:tipo>/album', 
        '/api/acervo/<string:acervo>/colecao/<string:tipo>/album/<string:id>')
api.add_resource(VideosApi, '/api/acervo/<string:acervo>/colecao/<string:tipo>/album/videos',
        '/api/acervo/<string:acervo>/colecao/<string:tipo>/album/<string:idAlbum>/video/<string:id>')
api.add_resource(FotosApi, '/api/acervo/<string:acervo>/colecao/<string:tipo>/album/fotos',
        '/api/acervo/<string:acervo>/colecao/<string:tipo>/album/<string:idAlbum>/foto/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)