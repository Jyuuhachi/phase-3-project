from DJs import DJ

class Song:
    
    all_songs = []
    
    def __init__(self, artist, title, play_info):
        self.artist = artist
        self.title = title
        self.play_info = play_info

    def __str__(self):
        return f"Song Title: {self.title} By: {self.artist} Play Info: {self.play_info}"
    

    @property
    def play_info(self):
        return self._play_info
    
    @play_info.setter
    def play_info(self, value):
        if type(value) == dict:
            self._play_info = value
        elif type(value) == DJ:
            self._play_info = {value.name : 1}
        if self.all_songs == []:
            self.all_songs.append(self)
        elif len(self.all_songs) > 0:
            for song in self.all_songs:
                if self.title == song.title and self.artist == song.artist:
                    pass
                else:
                    self.all_songs.append(self)

    def total_plays(self):
        played_by_list = self.play_info.keys()
        total_plays = 0
        for dj in played_by_list:
            total_plays += self.play_info[dj]
        return total_plays
    
    def one_DJs_plays(self, DJ):
        played_by_list = self.play_info.keys()
        total_plays = 0
        for dj in played_by_list:
            if dj == DJ.name:
                total_plays += self.play_info[dj]
        return total_plays
