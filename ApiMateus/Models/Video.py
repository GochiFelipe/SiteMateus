class Video(object):
    def __init__(self, Id, Url, Nome, Tipo, Album):
        self.Id = Id
        self.Nome = Nome
        self.Url = Url
        self.Tipo = Tipo
        self.Album = Album

    def videoHelper(self, itens):
        Videos = []
        for video in itens.get('Videos'):
            video = Video(str(video.get('_id')),
                            video.get('Url'),
                            video.get('Nome'),
                            video.get('Tipo'),
                            video.get('Nome_Album'))
            Videos.append(video.__dict__)
        return Videos