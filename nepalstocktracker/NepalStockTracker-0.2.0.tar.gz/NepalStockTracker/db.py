import json


class DB:
    def __init__(self):
        self.file = 'db.json'

    def ReadJSON(self):
        '''
        Get contents from db.json file
        '''

        try:
            with open(self.file, 'r') as f:
                contents = json.load(f)

        except FileNotFoundError:
            with open(self.file, 'w'):
                contents = {}

        except json.decoder.JSONDecodeError:
            contents = {}

        return contents

    def WriteJSON(self, contents):
        '''
        Storing data to the db.json file
        '''

        with open(self.file, 'w') as f:
            json.dump(contents, f, indent=4)
