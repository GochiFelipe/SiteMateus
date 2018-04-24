from flask import Flask
from flask_restful import Api
import os
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


from Database import CreateDatabase

from Views import Index
from Views import Adicionar
from AdminMateus import app
from Api.ColecaoApi import ColecaoApi
from Api.AlbumApi import AlbumApi
from Api.VideosApi import VideosApi
from Api.FotosApi import FotosApi
from Api.GaleriaApi import GaleriaApi


api.add_resource(GaleriaApi, '/api/galeria', 
        '/api/galeria/<string:galeria>')
api.add_resource(ColecaoApi,'/api/galeria/<string:galeria>/colecao', 
        '/api/galeria/<string:galeria>/colecao/<string:tipo>')
api.add_resource(AlbumApi,'/api/galeria/<string:galeria>/colecao/<string:tipo>/album', 
        '/api/galeria/<string:galeria>/colecao/<string:tipo>/album/<string:id>')
api.add_resource(VideosApi, '/api/galeria/<string:galeria>/colecao/<string:tipo>/album/videos',
        '/api/galeria/<string:galeria>/colecao/<string:tipo>/album/<string:idAlbum>/video/<string:id>')
api.add_resource(FotosApi, '/api/galeria/<string:galeria>/colecao/<string:tipo>/album/fotos',
        '/api/galeria/<string:galeria>/colecao/<string:tipo>/album/<string:idAlbum>/foto/<string:id>')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()