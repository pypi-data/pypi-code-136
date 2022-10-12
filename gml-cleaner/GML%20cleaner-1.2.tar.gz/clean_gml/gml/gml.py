from . gml_base import GmlBase
from . gml_schema import GmlSchema
from .. namespace import namespaces
from .. find_meta import find_meta_file


class Gml(GmlBase):
    """
    Class for reading a gml data file as xml data.

    """
    # xsd namespace

    def __init__(self, file):
        super().__init__(file)

        schema_file = find_meta_file(self.file)
        self.schema = GmlSchema(schema_file)

    def datatype_changes(self, changes: dict = None):
        self.schema.datatype_changes(changes=changes)

    def replace_commas(self, ndigits: int = 2):

        g = namespaces.get('g')
        params = [f'{{{g}}}{p}' for p in self.schema.get_parameters_floats()]

        for n in self.root.iter(f'{{{g}}}PROPERTIES'):
            for item in n.iter():
                if item.tag in params:
                    try:
                        item.text = str(round(float(item.text.replace(',', '.')), ndigits))
                    except Exception:
                        print(f'no tag found for item {item}')
                        continue

    def save(self):
        super()._save_xml()
        self.schema.save()




