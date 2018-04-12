from Models.Album import Album
from DAO.VideoDao import VideoDao
from DAO.FotoDao import FotoDao
from bson import ObjectId

class AlbumHelper(Album):

    def montaAlbum(self, itens, parametro = None):
        Albuns = []
        for album in itens:
            a = Album(str(album.get('_id')), 
                            album.get('Nome'), 
                            album.get('FotoCapa'),
                            album.get('Tipo'),
                            VideoDao.Busca.buscaVideoAlbum(self, album.get('Nome')),
                            FotoDao.Busca.buscaFotoAlbum(self, album.get('Nome')),
            )
            Albuns.append(a.__dict__)
        if parametro:
            return a.__dict__
        else:
            return Albuns
