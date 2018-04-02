class Video:
    def __init__(self, Nome, Url, Tipo):
        self.Nome = Nome
        self.Url = Url
        self.Tipo = Tipo

    def RecuperaVideos(self, itens):
        Videos = []
        for videos in itens.get('Videos'):
            Video_id = str(videos.get('_id'))
            Nome_Video = videos.get('Nome')
            Url_Video = videos.get('Url')
            Tipo_Video = videos.get('Tipo')
            video = Video(Nome_Video, Url_Video, Tipo_Video)
            v = {
                "IdVideo": Video_id,
                "NomeVideo": video.Nome,
                "UrlVideo": video.Url,
                "TipoVideo": video.Tipo
            }
            Videos.append(v)
        return Videos