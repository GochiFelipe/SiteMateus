class Foto(object):
    def __init__(self, Id, Url, Tipo, Local, Album, Tags = []):
        self.Id = Id
        self.Url = Url
        self.Tipo = Tipo
        self.Local = Local
        self.Album = Album
        self.Tags = Tags