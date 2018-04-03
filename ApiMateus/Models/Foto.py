class Foto:
    def __init__(self, Tipo, Url, Local, Tag = []):
        self.Tipo = Tipo
        self.Url = Url
        self.Local = Local
        self.Tag = Tag

    def recuperaFotos(self, itens):
        Fotos = []
        for fotos in itens.get('Fotos'):
            Foto_id = str(fotos.get('_id'))
            Tipo_foto = fotos.get('Tipo')
            Url_foto = fotos.get('Url')
            Tag_Foto = Foto.RecuperaTagFoto(self, fotos)
            Local_foto = fotos.get('Local')
            foto = Foto(Tipo_foto, Url_foto, Local_foto, Tag_Foto)
            f = {
                "IdFoto" : Foto_id,
                "TipoFoto" : foto.Tipo,
                "UrlFoto" : foto.Url,
                "LocalFoto" : foto.Local,
                "Tags" : foto.Tag
            }
            Fotos.append(f)
        return Fotos
    
    def RecuperaTagFoto(self, fotos):
        Tag = []
        for tag in fotos.get('Tags'):
            Item_Tag = tag
            Tag.append(Item_Tag)
        return Tag