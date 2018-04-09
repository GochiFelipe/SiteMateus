from Models.Colecao import Colecao
from DAO.AlbumDao import AlbumDao
class ColecaoHelper(Colecao):
    def montaColecaoAlbuns(self, objeto):
        for itens in objeto:
           return Colecao(str(itens.get('_id')), 
                                itens.get("Tipo"),
                                itens.get("Acervo"),
                                AlbumDao.Busca.buscaAlbumTipo(self, 
                                    itens.get('Tipo'))
            ).__dict__

    def montaListaColecoes(self, colecoes):
        Tipos = []
        for itens in colecoes:
            colecao = Colecao(
                str(itens.get('_id')),
                itens.get("Tipo"),
                itens.get("Acervo")
            )
            Tipos.append(colecao.Tipo)
        return Tipos

    