from Models.Colecao import Colecao
from DAO.AlbumDao import AlbumDao
class ColecaoHelper(Colecao):
    def montaColecaoAlbuns(self, objeto, parametro):
        for itens in objeto:
           return Colecao(str(itens.get('_id')), 
                                itens.get("Tipo"),
                                AlbumDao.Busca.buscaAlbumTipo(self, 
                                    itens.get('Tipo')),
            ).__dict__

    def montaListaColecoes(self, colecoes):
        Tipos = []
        for itens in colecoes:
            colecao = Colecao(
                str(itens.get('_id')),
                itens.get("Tipo")
            )
            Tipos.append(colecao.Tipo)
        return Tipos

    