from Models.Acervo import Acervo
from DAO.ColecaoDao import ColecaoDao
class AcervoHelper(Acervo):
    def montaListaAcervo(self, acervo):
        Tipos = []
        for itens in acervo:
            acervo = Acervo(
                str(itens.get('_id')),
                itens.get('Acervo'),
            )
            Tipos.append(acervo.Acervo)
        return Tipos
    
    def montaAcervoColecao(self, objeto):
        for itens in objeto:
            return Acervo(str(itens.get('_id')),
                                itens.get('Acervo'), 
                                ColecaoDao.Busca.buscaColecaoAcervo(self, 
                                    itens.get('Acervo'))
            ).__dict__