from DJs import DJ
from Song import Song
#from Set import Set



def launch():
    exit_check = True
    while(exit_check):
        print("")
        print("")
        print("1) add a DJ")
        print("2) enter a set list")
        print("3) check sets")
        print("4) check a song's total play count")
        print("5) check how many times a DJ has played a song")
        print("type 'exit' to quit the program")
        print("")
        selection = input("Enter a number to choose an option")
        if selection == "1":
            add_new_DJ()
        elif selection == "2":
            create_a_set()
        elif selection == "3":
            check_set_lists()
        elif selection == "4":
            check_total_rinse()
        elif selection == "5":
            check_self_rinse()
        elif selection == "exit":
            exit_check = False
        else:
            print("invalid entry, try again")

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
    set_list = []
    while(select_dj):
        run_check = True
        i = 0
        track_list = []
        print("Please select a DJ from the list below or type 'back' to return to the previous menu")
        print("")
        for dj in DJ.all_DJs:
            print(f"{i+1}. {dj}")
            i+=1
        performing_dj = input("Enter a number to select a DJ")
        if performing_dj != "back":
            performing_dj = DJ.all_DJs[int(performing_dj)-1]
            while(run_check):
                print("")
                print("1) add a song")
                print("2) check song list")
                print("finish) finish entering tracks in the set return to DJ select")
                add_song = input("Please enter one of the commands above:")
                if add_song == "1":
                    print("")
                    title = input("Please enter the song's title:")
                    print("")
                    artist = input("Please enter the song's artist:")
                    if Song.all_songs == []:
                        track_list.append(Song(artist, title, {performing_dj.name : 1}))
                    else:
                        found_match = False
                        for song in Song.all_songs:
                            print(f"title variable: {title}")
                            print(f"artist variable: {artist}")
                            if song.title == title and song.artist == artist:
                                check_djs = song.play_info.keys()
                                if check_djs == []:
                                    if song in track_list:
                                        song.play_info[performing_dj.name] = 1
                                        found_match = True
                                        break
                                    elif song not in track_list:
                                        print("didn't find track in tracklist so added it")
                                        song.play_info[performing_dj.name] = 1
                                        track_list.append(song)
                                        found_match = True
                                        break
                                else:
                                    if performing_dj.name in check_djs:
                                        if song in track_list:
                                            print("incrementing a track play count if DJ matches")
                                            song.play_info[performing_dj.name] += 1
                                            found_match = True
                                            break
                                        elif song not in track_list:
                                            print("didn't find track in tracklist so added it")
                                            song.play_info[performing_dj.name] += 1
                                            track_list.append(song)
                                            found_match = True
                                            break
                        if found_match == False:
                            print("no matches so adding track")
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
                    #set_list.append(Set(performing_dj, track_list))
        else:
            return
            
def check_total_rinse():
    pass

def check_self_rinse():
    pass

def check_set_lists():
    pass

launch()