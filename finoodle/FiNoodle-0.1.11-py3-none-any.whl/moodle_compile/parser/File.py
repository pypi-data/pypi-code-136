class File:
    def __init__(self, name, path, encoding, contents):
        self.name = name
        self.path = path
        self.encoding = encoding
        self.content = content

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.encoding = 'base64'
        self.content = None

    def setContent(self, newContent):
        self.content = newContent.decode("utf-8") 
