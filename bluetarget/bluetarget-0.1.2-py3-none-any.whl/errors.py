class FileNotFound(Exception):

    file: str

    def __init__(self, file: str):
        self.file = file

    def __str__(self):
        return f'File {self.file} not found'


class ModelClassNotFound(Exception):

    class_name: str

    def __init__(self, class_name: str):
        self.class_name = class_name

    def __str__(self):
        return f'Class {self.class_name} not found'


class EntityNotFound(Exception):

    entity: str
    id: str

    def __init__(self, entity: str, id: str):
        self.entity = entity
        self.id = id

    def __str__(self):
        return f'{self.entity} {self.id} not found'


class AuthorizationError(Exception):

    def __str__(self):
        return f'Api key not found'


class ServerValidationException(Exception):
    code: str
    description: str

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description

    def __str__(self):
        return f'${self.code}'
