from Song import Song
from DJs import DJ
import sqlite3
#import runme

def instantiate_db():
    djs = """
          CREATE TABLE IF NOT EXISTS DJs(
          ID int PRIMARY KEY,
          name text
          );
          """

    songs = """
          CREATE TABLE IF NOT EXISTS Songs(
          ID int PRIMARY KEY,
          title text,
          artist text,
          info text
          );
          """
    

    con = sqlite3.connect("./lib/db/test.db")
    cur = con.cursor()
    cur.execute(djs)
    cur.execute(songs)
    input("holding the function up until you input")


def clear_db():

    drop_songs = "DROP TABLE Songs;"
    drop_djs = "DROP TABLE DJs;"
    
    con = sqlite3.connect("./lib/db/test.db")
    cur = con.cursor()
    cur.execute(drop_songs)
    cur.execute(drop_djs)


instantiate_db()
clear_db()
# new_dj = DJ("DJ18TESTS")
# new_song = Song("test", "testing", new_dj)
# new_song2 = Song("test2", "testing", {"DJFRAGMAN": 2})
# print(new_song)
# print(new_song2)
# print(new_dj)
# print(Song.all_songs)

