class DictClass:
    def __init__(self, dict_data):
        for key, value in dict_data.items():
            if type(value) == dict:
                setattr(self, key, DictClass(value))
            else:
                setattr(self, key, value)