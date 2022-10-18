import os
class File:
    def __init__(self, path, mode):
        self.path = path
        try:
            self.file = open(path, mode)
        except:
            print("Error with opening file!")
            self.path = ""
    def getFile(self):
        return self.file
    def getFilePath(self):
        return self.path
    def getFilePathName(self):
        return os.path.basename(self.path)
    def getFileName(self):
        base = os.path.basename(self.path).split(".")
        return base[0]
    def getFileExtension(self):
        base = os.path.basename(self.path).split(".")
        return base[1]
    