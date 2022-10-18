from io import BytesIO


class InMemoryFile:
    def __init__(self, name: str, initial_content: bytes):
        self.file_like: BytesIO = BytesIO(initial_content)
        self.file_like.name = name
