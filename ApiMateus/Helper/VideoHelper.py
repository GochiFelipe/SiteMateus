from Models.Video import Video

class VideoHelper(Video):
    def montaVideos(self, itens, parametro = None):
        Videos = []
        for video in itens:
            video = Video(str(video.get('_id')),
                            video.get('Url'),
                            video.get('Nome'),
                            video.get('Tipo'),
                            video.get('Album'))
            Videos.append(video.__dict__)
        if parametro:
            return video.__dict__
        else:
            return Videos