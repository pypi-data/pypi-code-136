from . gml_base import GmlBase
from clean_gml.utils import get_file_split


floats = ['xsd:float', 'xsd:decimal', 'double', 'Real']


class GmlSchema(GmlBase):
    """
    Helper class to load the xml schema
    """

    def __init__(self, file):
        super().__init__(file)

    def datatype_changes(self, changes: dict = None):
        if changes is None:
            return None

        if not isinstance(changes, dict):
            raise TypeError('changes must be a dictionary')

        for k, v in changes.items():
            for child in self.root.iter():
                if 'element' in child.tag and child.attrib['name'] == k:
                    child.attrib['type'] = v
                break

    def get_parameters_floats_xsd(self):
        return [child.attrib['name'] for child in self.root.iter() if 'element' in child.tag and child.attrib['type'] in floats]

    def get_parameters_floats(self):
        _, _, extension = get_file_split(self.file)

        params = None

        if extension == '.xsd':
            params = self.get_parameters_floats_xsd()
        elif extension == '.gfs':
            params = self.get_parameters_floats_gfs()

        return params

    def get_parameters_floats_gfs(self):
        names = []
        for name in self.root.findall('.//Name'):
            names.append({'name': name.text})

        # removes properties at top
        names.pop(0)

        types = []
        for name in self.root.findall('.//Type'):
            types.append({'type': name.text})

        c = []
        for name, type_ in zip(names, types):
            temp = {**name, **type_}
            c.append(temp)

        return [item for item in c if item['type'] in floats]

    def save(self):
        super()._save_xml()

