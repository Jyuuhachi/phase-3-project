from DJs import DJ
from Song import Song
from Set import Set
import sqlite3
import json
database = "data"


def launch():
    instantiate()
    exit_check = True
    while(exit_check):
        print("")
        print("")
        print("1) enter a set list")
        print("2) check sets")
        print("3) check a song's total play count")
        print("4) check how many times a DJ has played a song")
        print("type 'exit' to quit the program")
        print("")
        selection = input("Enter a number to choose an option: ")
        if selection == "1":
            create_a_set()
        elif selection == "2":
            check_set_lists()
        elif selection == "3":
            check_total_rinse()
        elif selection == "4":
            check_self_rinse()
        elif selection == "djs":
            test_DJs()
        elif selection == "songs":
            test_songs()
        elif selection == "sets":
            test_sets()
        elif selection == "exit":
            exit_check = False
        else:
            print("invalid entry, try again")
    save_everything()
    exit()

def test_sets():
    for set in Set.all_sets:
        print(set)
        print("")

def test_DJs():
    for dj in DJ.all_DJs:
        print(dj)
        print("")

def test_songs():
    for song in Song.all_songs:
        print(song)
        print("")

def add_new_DJ():
    name = input("Please enter the DJ's name here: ")
    DJ(name)

def add_new_song():
    title = input("Please enter the song title here: ")
    print("")
    artist = input("Please enter the song's artist here: ")
    Song()

def create_a_set():
    select_dj = True
    while(select_dj):
        run_check = True
        track_list = []
        print("Please enter a DJ name or type 'back' to return to the previous menu")
        print("")
        performing_dj_name = input("Enter DJ's name: ")
        if performing_dj_name != "back":
            performing_dj = DJ(performing_dj_name)
            while(run_check):
                print("")
                print("1) add a song")
                print("2) check song list")
                print("finish) finish entering tracks in the set return to DJ select")
                add_song = input("Please enter one of the commands above: ")
                if add_song == "1":
                    print("")
                    title = input("Please enter the song's title: ")
                    print("")
                    artist = input("Please enter the song's artist: ")
                    if Song.all_songs == []:
                        track_list.append(Song(artist, title, {performing_dj.name : 1}))
                    else:
                        found_match = False
                        for song in Song.all_songs:
                            if song.title == title and song.artist == artist:
                                check_djs = song.play_info.keys()
                                print(check_djs)
                                print(performing_dj)
                                if check_djs == []:
                                    print("gets to the track_list for loop")
                                    for track in track_list:
                                        if song.title == track.title and song.artist == track.artist:
                                            print("song found in track_list where play info has no DJs")
                                            song.play_info[performing_dj.name] = 1
                                            track_list.append(song)
                                            found_match = True
                                            break
                                    track_list.append(song)
                                else:
                                    if performing_dj.name in check_djs:
                                        print("gets to the track_list for loop")
                                        for track in track_list:
                                            if song.title == track.title and song.artist == track.artist:
                                                print("found song in track_list and found DJ in songs play info")
                                                song.play_info[performing_dj.name] += 1
                                                found_match = True
                                                track_list.append(song)
                                                break
                                        track_list.append(song)
                                    else:
                                        song.play_info[performing_dj.name] = 1
                                        found_match = True
                                        track_list.append(song)
                        if found_match == False:
                            print("found_match == False triggering")
                            track_list.append(Song(artist, title, {performing_dj.name : 1}))
                                
                elif add_song == "2":
                    i = 1
                    print(f"{len(track_list)} Tracks")
                    for song in track_list:
                        print("")
                        print(f"track #{i}")
                        print(f"{song}")
                        i+=1
                elif add_song == "finish":
                    run_check = False
                    finalized_dj = performing_dj.id
                    finalized_track_list = [item.id for item in track_list]
                    Set(finalized_dj, finalized_track_list)
        else:
            return
            
def check_total_rinse():
    print("")
    title = input("Please enter the song's title: ")
    print("")
    artist = input("Please enter the song's artist: ")
    for song in Song.all_songs:
        if song.artist == artist and song.title == title:
            all_plays = song.play_info.values()
            total_plays = sum(all_plays)
            print(f"{title} by {artist} has been played {total_plays} times by everyone")
            return
    print("Could not find a matching song. Returning to main menu")


def check_self_rinse():
    print("")
    name = input("Please enter a DJ's name: ")
    for dj in DJ.all_DJs:
        if dj.name == name:
            print("")
            title = input("Please enter the song's title: ")
            print("")
            artist = input("Please enter the song's artist: ")
            for song in Song.all_songs:
                if song.artist == artist and song.title == title:
                    total_plays = song.play_info[name]
                    print(f"{title} by {artist} has been played {total_plays} times by DJ{name}")
                    return
            print("Could not find matching song. Returning to main menu")
            return
    print("DJ name not found. Try again")

def check_set_lists():
    i=1
    for set in Set.all_sets:
        print("")
        print(f"Set #{i} mixed by {DJ.all_DJs[(set.dj - 1)]}")
        i+=1
        for song in set.track_list:
            print(f"Track {Song.all_songs[(song - 1)].title} by {Song.all_songs[(song - 1)].artist}")

def save_everything():
    con = sqlite3.connect(f"./lib/db/{database}.db")
    cur = con.cursor()
    cur.execute("DROP TABLE songs;")
    cur.execute("DROP TABLE djs;")
    cur.execute("DROP TABLE sets;")
    create_db()
    Song.save()
    Set.save()
    DJ.save()

def create_db():
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
    con = sqlite3.connect(f"./lib/db/{database}.db")
    cur = con.cursor()
    cur.execute(djs)
    cur.execute(songs)
    cur.execute(sets)

def instantiate():
    con = sqlite3.connect(f"./lib/db/{database}.db")
    cur = con.cursor()
    dj_res = cur.execute("SELECT * FROM djs;")
    djs = dj_res.fetchall()
    for dj in djs:
        DJ(dj[1], dj[0])
    song_res = cur.execute("SELECT * FROM songs;")
    songs = song_res.fetchall()
    for song in songs:
        Song(song[2], song[1], (json.loads(song[3])), song[0])
    set_res = cur.execute("SELECT * FROM sets;")
    sets = set_res.fetchall()
    for set in sets:
        Set(set[1], (json.loads(set[2])), set[0])
    
if __name__ == '__main__':
    launch()
