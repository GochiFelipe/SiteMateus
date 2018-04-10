from Models.Galeria import Galeria
from DAO.ColecaoDao import ColecaoDao
class GaleriaHelper(Galeria):
    def montaListaGaleria(self, galeria):
        Tipos = []
        for itens in galeria:
            galeria = Galeria(
                str(itens.get('_id')),
                itens.get('Galeria'),
            )
            Tipos.append(galeria.Galeria)
        return Tipos
    
    def montaGaleriaColecao(self, objeto):
        for itens in objeto:
            return Galeria(str(itens.get('_id')),
                                itens.get('Galeria'), 
                                ColecaoDao.Busca.buscaColecaoGaleria(self, 
                                    itens.get('Galeria'))
            ).__dict__