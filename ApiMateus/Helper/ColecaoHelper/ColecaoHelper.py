from Models.Colecao import Colecao
from Helper.AlbumHelper.AlbumHelper import AlbumHelper

class ColecaoHelper(Colecao):
    def colecaoHelper(self, objeto):
        for itens in objeto:
            colecao = Colecao(str(itens.get('_id')), 
                                itens.get("Tipo"),
                                AlbumHelper.albumHelper(self, 
                                    itens.get('Album'), 'colecao'),
            )
        return colecao.__dict__