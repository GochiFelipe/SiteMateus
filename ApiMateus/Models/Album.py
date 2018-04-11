class Album(object):
    def __init__(self,Id, Nome, FotoCapa, Tipo, Video = [], Fotos = []):
        self.Id = Id
        self.Nome = Nome
        self.Videos = Video
        self.Fotos = Fotos
        self.FotoCapa = FotoCapa
        self.Tipo = Tipo