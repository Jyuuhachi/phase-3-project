from Song import Song
from DJs import DJ
from Set import Set
import sqlite3
import json
#import runme
database = "test"

def instantiate_db():
    djs = """
          CREATE TABLE IF NOT EXISTS djs(
          dj_id int,
          name text
          );
          """

    songs = """
          CREATE TABLE IF NOT EXISTS songs(
          song_id int,
          title text,
          artist text,
          info text
          );
          """
    sets = """
          CREATE TABLE IF NOT EXISTS sets(
          set_id int,
          dj int,
          track_list text
          );
          """
    

    con = sqlite3.connect("./lib/db/test.db")
    cur = con.cursor()
    cur.execute(djs)
    cur.execute(songs)
    cur.execute(sets)


def clear_db():

    drop_songs = "DROP TABLE songs;"
    drop_djs = "DROP TABLE djs;"
    drop_sets = "DROP TABLE sets;"
    
    con = sqlite3.connect("./lib/db/test.db")
    cur = con.cursor()
    cur.execute(drop_songs)
    cur.execute(drop_djs)
    cur.execute(drop_sets)


def add_to_db():
    test = 'DJ18TESTS'
    target = 'name'
    add_dj = "INSERT INTO djs VALUES(?,?);"

    con = sqlite3.connect("./lib/db/test.db")
    cur = con.cursor()
    cur.execute(add_dj, (1, test))
    con.commit()

def test_fetch():

    con = sqlite3.connect("./lib/db/test.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM djs;")
    shit = res.fetchall()
    print(shit)
    print(shit[0])
    print(shit[0][0])

def test_building_instances():
    con = sqlite3.connect(f"./lib/db/{database}.db")
    cur = con.cursor()
    dj_res = cur.execute("SELECT * FROM djs;")
    djs = dj_res.fetchall()
    print(f"checking djs {djs}")
    for dj in djs:
        DJ(dj[1], dj[0])
    print(f"checking all_djs in DJs {DJ.all_DJs}")
    song_res = cur.execute("SELECT * FROM songs;")
    songs = song_res.fetchall()
    for song in songs:
        Song(song[2], song[1], (json.loads(song[3])), song[0])
    set_res = cur.execute("SELECT * FROM sets;")
    sets = set_res.fetchall()
    for set in sets:
        Set(set[1], (json.loads(set[2])), set[0])
    
def print_instances():
    print("songs:")
    for song in Song.all_songs:
        print(song)
    print("")
    print("DJs:")
    for dj in DJ.all_DJs:
        print(dj)
    print("")
    print("Sets:")
    for set in Set.all_sets:
        print(set)

class Fuck:
    
    last_id = 0
    all_DJs = []

    def __init__(self, name, id=None):
        self.name = name
        if id == None:
            self.id = Fuck.last_id + 1
            Fuck.last_id += 1
        else:
            self.id = id
            Fuck.last_id = id
        self.all_DJs.append(self)

    def __str__(self):
        return f"DJ {self.name} ID: {self.id}"
    
    @classmethod
    def save(cls):
        add_dj = "INSERT INTO djs VALUES(?,?);"
        con = sqlite3.connect(f"./lib/db/{database}.db")
        cur = con.cursor()
        for dj in cls.all_DJs:
            cur.execute(add_dj, (dj.id, dj.name))
        con.commit()
        

def test_dict_search():
    find = input("type butts: ")
    test_dict = {"butts": 3, "ass": "tits"}
    test_fuck = Fuck(find, 2)
    check = test_dict.keys()
    print(test_fuck.name)
    if test_fuck.name in check:
        print("could find name in .keys list with class.name attribute")
    for key in check:
        print(key)
        if key == find:
            print("found string in .keys list by comparing in a for loop")
    if find in check:
        print("found string in .keys list")

# con = sqlite3.connect("./lib/db/test.db")
# cur = con.cursor()
# cur.execute("DROP TABLE DJs;")
# cur.execute("DROP TABLE Songs;")
#clear_db()
#instantiate_db()
#add_to_db()
#test_fetch()
#test_building_instances()
#print_instances()
test_dict_search()
input("input to force wait before clearing DB")
# new_dj = DJ("DJ18TESTS")
# new_song = Song("test", "testing", new_dj)
# new_song2 = Song("test2", "testing", {"DJFRAGMAN": 2})
# print(new_song)
# print(new_song2)
# print(new_dj)
# print(Song.all_songs)

