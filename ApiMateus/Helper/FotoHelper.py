from Models.Foto import Foto

class FotoHelper(Foto):
    def montaFotos(self, itens, id = None):

        Fotos = []
        for foto in itens:
            fotos = Foto(
                str(foto.get('_id')),
                foto.get('Url'),
                foto.get('Tipo'),
                foto.get('Local'),
                foto.get('Album'),
                FotoHelper.montaTags(self, foto.get('Tags'))
            )
            Fotos.append(fotos.__dict__)
        if id:
            return fotos.__dict__
        else:
            return Fotos

    def montaTags(self, foto):
        Tags = []
        for tag in foto:
            Item_Tag = tag
            Tags.append(Item_Tag)
        return Tags