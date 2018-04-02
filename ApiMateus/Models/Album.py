class Album:
    def __init__(self, Nome, FotoCapa, Tipo, Video = [], Fotos = []):
        self.Nome = Nome
        self.Videos = Video
        self.Fotos = Fotos
        self.FotoCapa = FotoCapa
        self.Tipo = Tipo

    def RecuperaAlbunsId(self, itens):
        Albuns = []
        for album in itens.get('Album'):
            Album_id = str(album.get('_id'))
            Nome_Album = album.get('Nome')
            Tipo_Album = album.get('Tipo')
            Foto_Capa = album.get('FotoCapa')
            album = Album(Nome_Album, Foto_Capa, Tipo_Album)
            a= {'Id' :Album_id,
                'Nome': album.Nome, 
                'FotoCapa': album.FotoCapa
            }
            Albuns.append(a)
        return Albuns