from DJs import DJ
import sqlite3
import json
database = "test"

class Song:
    
    last_id = 0
    all_songs = []
    
    def __init__(self, artist, title, play_info, id=None):
        self.artist = artist
        self.title = title
        self.play_info = play_info
        if id == None:
            self.id = Song.last_id + 1
            Song.last_id += 1
        else:
            self.id = id
            Song.last_id = id
        self.all_songs.append(self)
    def __str__(self):
        return f"Song Title: {self.title} By: {self.artist} Play Info: {self.play_info} ID: {self.id}"
    

    @property
    def play_info(self):
        return self._play_info
    
    @play_info.setter
    def play_info(self, value):
        if type(value) == dict:
            self._play_info = value
        elif type(value) == DJ:
            self._play_info = {value.name : 1}

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

    @classmethod
    def save(cls):
        add_songs = "INSERT INTO songs VALUES(?,?,?,?);"
        con = sqlite3.connect(f"./lib/db/{database}.db")
        cur = con.cursor()
        for song in cls.all_songs:
            cur.execute(add_songs, (song.id, song.title, song.artist, (json.dumps(song.play_info))))
        con.commit()