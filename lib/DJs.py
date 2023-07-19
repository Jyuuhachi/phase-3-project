

class DJ:
    
    all_DJs = []

    def __init__(self, name):
        self.name = name
        self.all_DJs.append(self)

    def __str__(self):
        return f"DJ {self.name}"

