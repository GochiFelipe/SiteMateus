from Models.Album import Album
from DAO.VideoDao import VideoDao
from DAO.FotoDao import FotoDao
from bson import ObjectId

class AlbumHelper(Album):

    def montaAlbum(self, itens, parametro = None):
        Albuns = []
        for album in itens:
            a = Album(str(album.get('_id')), 
                            album.get('Nome'), 
                            album.get('FotoCapa'),
                            album.get('Tipo'),
                            VideoDao.Busca.buscaVideoAlbum(self, album.get('Nome')),
                            FotoDao.Busca.buscaFotoAlbum(self, album.get('Nome')),
            )
            Albuns.append(a.__dict__)
        if parametro:
            return a.__dict__
        else:
            return Albuns

    def verificaAlteracao(self, album, Albuns):
        buscas = Albuns.find({'_id': ObjectId(album.Id)})
        for itens in buscas:
            albumBusca = Album(itens.get('_id'),
                            itens.get('Nome'),
                            itens.get('FotoCapa'),
                            itens.get('Tipo')
            )
            if album.Nome != albumBusca.Nome:
                Albuns.update_one(
                    {'_id': ObjectId(album.Id)},
                    {
                        "$set":{
                            "Nome" : album.Nome
                        }
                    }
                )
            if album.Tipo != albumBusca.Tipo:
                Albuns.update_one(
                    {'_id': ObjectId(album.Id)},
                    {
                        "$set":{
                            "Tipo" : album.Tipo
                        }
                    }
                )
            if album.FotoCapa != albumBusca.FotoCapa:
                Albuns.update_one(
                    {'_id': ObjectId(album.Id)},
                    {
                        "$set":{
                            "FotoCapa" : album.FotoCapa
                        }
                    }
                )
            else:
                return ('Não existem alterações')
        return ('Alterado Com Sucesso')