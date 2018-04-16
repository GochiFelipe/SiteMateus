from flask_restful import Resource, reqparse
from DAO.VideoDao import VideoDao

class VideosApi(Resource):

    def get(self, galeria, tipo, idAlbum = None, id= None):
        if idAlbum and id:
            try:
                return VideoDao.Busca.buscaVideoTipoId(self, tipo,idAlbum, id)
            except:
                return ('Não Existem Registros')
        else:
            pass

    def post(self, galeria, tipo):
        parser = reqparse.RequestParser()
        parser.add_argument('Nome')
        parser.add_argument('Url')
        parser.add_argument('Tipo')
        parser.add_argument('Album')
        args_principal = parser.parse_args()
        adicionaVideo = VideoDao.Insere.inserirVideo(self, args_principal)
        return adicionaVideo

    def put(self, galeria, tipo, idAlbum = None, id = None):
        if idAlbum and id:
            parser = reqparse.RequestParser()
            parser.add_argument('Id')
            parser.add_argument('Nome')
            parser.add_argument('Url')
            parser.add_argument('Tipo')
            parser.add_argument('Album')
            args_principal = parser.parse_args()
            return VideoDao.Atualiza.atualizaVideo(self, args_principal)
        else:
            pass
