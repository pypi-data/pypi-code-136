from unicodedata import normalize
import json
import os


def encode_to_ascii(name):
    ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")
    return ascii_name.upper()


class BrazilNamesGender:
    def __init__(self):
        this_dir, this_filename = os.path.split(__file__)
        json_path = os.path.join(this_dir, "gender_by_name.json")
        self._gender_dict = json.load(open(json_path))

    def get_gender(self, name):
        gender = 'Unk'
        name_info = self._gender_dict.get(encode_to_ascii(name), None)
        if name_info is not None:
            gender = name_info['gender']
        return gender

    def get_gender_by_majority(self, name):
        gender = 'Unk'
        name_info = self._gender_dict.get(encode_to_ascii(name), None)
        if name_info is not None:
            gender = name_info['gender_by_majority']
        return gender


br_gender_info = BrazilNamesGender()
