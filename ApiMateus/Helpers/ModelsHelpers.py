from bson import json_util, ObjectId

class ModelsHelpers():

    def RecuperaVideos(itens):
        Videos = []
        for video in itens.get('Videos'):
            Video_id = str(ObjectId())
            Nome_Video = video.get('Nome')
            Url_Video = video.get('Url')
            Tipo_Video = video.get('Tipo')
            v = {
                "IdVideo": Video_id,
                "NomeVideo": Nome_Video,
                "UrlVideo": Url_Video,
                "TipoVideo": Tipo_Video
            }
            Videos.append(v)
        return Videos

    def RecuperaFotos(itens):
        Fotos = []
        for foto in itens.get('Fotos'):
            Foto_id = str(ObjectId())
            Tipo_foto = foto.get('Tipo')
            Url_foto = foto.get('Url')
            Local_foto = foto.get('Local')
            f = {
                "IdFoto" : Foto_id,
                "TipoFoto" : Tipo_foto,
                "UrlFoto" : Url_foto,
                "LocalFoto" : Local_foto
            }
            Fotos.append(f)
        return Fotos
            