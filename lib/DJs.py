import sqlite3
database = "test"
class DJ:
    
    last_id = 0
    all_DJs = []

    def __init__(self, name, id=None):
        self.name = name
        if id == None:
            self.id = DJ.last_id + 1
            DJ.last_id += 1
        else:
            self.id = id
            DJ.last_id = id
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
        

