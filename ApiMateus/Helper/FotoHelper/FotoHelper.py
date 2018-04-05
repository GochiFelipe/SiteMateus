from Models.Foto import Foto

class FotoHelper(Foto):
    def fotosHelper(self, itens):
        Fotos = []
        for foto in itens:
            fotos = Foto(
                str(foto.get('_id')),
                foto.get('Url'),
                foto.get('Tipo'),
                foto.get('Local'),
                foto.get('Album'),
                FotoHelper.tagFotoHelper(self, foto)
            )
            Fotos.append(fotos.__dict__)
        return Fotos

    def tagFotoHelper(self, foto):
        Tag = []
        for tag in foto.get('Tags'):
            Item_Tag = tag
            Tag.append(Item_Tag)
        return Tag