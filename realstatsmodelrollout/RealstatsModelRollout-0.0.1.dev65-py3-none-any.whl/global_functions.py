from .settings import settings

class globalFunctions: 
    def __init__(self):
        self._id = "Development"

    ### get index location of char in string ###
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

        