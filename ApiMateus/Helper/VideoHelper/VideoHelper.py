from Models.Video import Video

class VideoHelper(Video):
    def videoHelper(self, itens):
        Videos = []
        for video in itens:
            video = Video(str(video.get('_id')),
                            video.get('Url'),
                            video.get('Nome'),
                            video.get('Tipo'),
                            video.get('Nome_Album'))
            Videos.append(video.__dict__)
        return Videos