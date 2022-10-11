

class MD5AnyErrorCode(Exception):
    def __init__(self, msg):
        Exception.__init__(self, "Error: " + msg)