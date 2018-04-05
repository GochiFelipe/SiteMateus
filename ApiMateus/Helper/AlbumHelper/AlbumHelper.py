from Models.Album import Album
from Helper.FotoHelper.FotoHelper import FotoHelper
from Helper.VideoHelper.VideoHelper import VideoHelper

class AlbumHelper(Album):

    def albumHelper(self, itens, identificador):
        Albuns = []
        for album in itens:
            a = Album(str(album.get('_id')), 
                            album.get('FotoCapa'),
                            album.get('Nome'), 
                            album.get('Tipo'),
                            VideoHelper.videoHelper(self, album.get('Videos')),
                            FotoHelper.fotosHelper(self, album.get('Fotos'))
            )
            Albuns.append(a.__dict__)
        if(identificador == 'colecao'):
            return Albuns
        else:
            return a.__dict__