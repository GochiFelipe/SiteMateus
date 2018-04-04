class Foto(object):
    def __init__(self, Id, Url, Tipo, Local, Album, Tag = []):
        self.Id = Id
        self.Url = Url
        self. Tipo = Tipo
        self.Local = Local
        self.Tag = Tag

    def recuperaFotos(self, itens):
        for foto in itens.get('Fotos'):
            foto = Foto(
                str(foto.get('_id')),
                foto.get('Url'),
                foto.get('Tipo'),
                foto.get('Local'),
                foto.get('Album'),
                Foto.RecuperaTagFoto(self, foto)
            )
        return foto.__dict__
    
    def RecuperaTagFoto(self, foto):
        Tag = []
        for tag in foto.get('Tags'):
            Item_Tag = tag
            Tag.append(Item_Tag)
        return Tag