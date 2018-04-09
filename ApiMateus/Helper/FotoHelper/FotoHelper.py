from Models.Foto import Foto

class FotoHelper(Foto):
    def montaFotos(self, itens):
        Fotos = []
        for foto in itens:
            fotos = Foto(
                str(foto.get('_id')),
                foto.get('Url'),
                foto.get('Tipo'),
                foto.get('Local'),
                foto.get('Album'),
                FotoHelper.montaTags(self, foto.get('Tag'))
            )
            Fotos.append(fotos.__dict__)
        return Fotos

    def montaTags(self, foto):
        Tag = []
        for tag in foto:
            Item_Tag = tag
            Tag.append(Item_Tag)
        return Tag