from Models.Colecao import Colecao
from DAO.AlbumDao import AlbumDao
from bson import ObjectId

class ColecaoHelper(Colecao):
    def montaColecaoAlbuns(self, objeto):
        for itens in objeto:
           return Colecao(str(itens.get('_id')), 
                                itens.get("Tipo"),
                                itens.get("Galeria"),
                                AlbumDao.Busca.buscaAlbumTipo(self, 
                                    itens.get('Tipo'))
            ).__dict__

    def montaListaColecoes(self, colecoes):
        Tipos = []
        for itens in colecoes:
            colecao = Colecao(
                str(itens.get('_id')),
                itens.get("Tipo"),
                itens.get("Galeria")
            )
            Tipos.append(colecao.Tipo)
        return Tipos

    def verificaAlteracao(self, colecao, Colecoes):
        try:
            buscas = Colecoes.find({'_id': ObjectId(colecao.Id)})
            for itens in buscas:
                colecaoBusca = Colecao(itens.get('_id'),
                                        itens.get('Tipo'),
                                        itens.get('Galeria')
                )
                if colecao.Galeria != colecaoBusca.Galeria:
                    Colecoes.update_one(
                        {'_id': ObjectId(colecao.Id)},
                        {
                            "$set":{
                                "Galeria" : colecao.Galeria
                            }
                        }
                    )
                if colecao.Tipo != colecaoBusca.Tipo:
                    Colecoes.update_one(
                        {'_id': ObjectId(colecao.Id)},
                        {
                            "$set":{
                                "Tipo" : colecao.Tipo
                            }
                        }
                    )
                else:
                    return ('Não existe alterações')
            return ('Alterado Com Sucesso')
        except:
            return False