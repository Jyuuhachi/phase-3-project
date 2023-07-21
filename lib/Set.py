import sqlite3
import json
database = "test"

class Set:

    last_id = 0
    all_sets = []

    def __init__(self, dj, track_list, id=None):
        self.dj = dj
        self.track_list = track_list
        if id == None:
            self.id = Set.last_id + 1
            Set.last_id += 1
        else:
            self.id = id
            Set.last_id = id
        self.all_sets.append(self)

    @classmethod
    def save(cls):
        add_set = "INSERT INTO sets VALUES(?,?,?);"
        con = sqlite3.connect(f"./lib/db/{database}.db")
        cur = con.cursor()
        for set in cls.all_sets:
            cur.execute(add_set, (set.id, set.dj, (json.dumps(set.track_list))))
            con.commit()