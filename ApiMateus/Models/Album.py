from bson import ObjectId
from Models.Video import Video

class Album(object):
    def __init__(self,Id, Nome, FotoCapa, Tipo, Video = [], Fotos = []):
        self.Id = Id
        self.Nome = Nome
        self.Videos = Video
        self.Fotos = Fotos
        self.FotoCapa = FotoCapa
        self.Tipo = Tipo

    def recuperaAlbuns(self, itens):
        Albuns = []
        for album in itens.get('Album'):
            a = Album(str(album.get('_id')), 
                            album.get('FotoCapa'),
                            album.get('Nome'), 
                            album.get('Tipo'),
                            album.get(Video.videoHelper(self, album))
            )
            Albuns.append(a.__dict__)
        return Albuns

    def albumParser(objeto):
        Valores = {}
        for (nomes, valores) in objeto.items():
            Valores.update({nomes :valores})
            print(Valores)
        return Valores