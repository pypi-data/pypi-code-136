import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from clean_gml.namespace import namespaces
from clean_gml.utils import get_file_split
from clean_gml.find_meta import find_meta_file


class GmlBase:

    def __init__(self, file):
        self.file = file
        self.root = self.parse()

    def parse(self):
        mytree = ET.parse(self.file)
        myroot = mytree.getroot()
        for prefix, namespace in namespaces.items():
            ET.register_namespace(prefix, namespace)
        return myroot

    def prepare_save_path(self):
        new_dir = 'adjusted'

        base_dir = os.path.dirname(self.file)
        try:
            os.mkdir(os.path.join(base_dir, new_dir))
        except Exception:
            pass

        basename = os.path.basename(self.file)

        return os.path.join(base_dir, new_dir, basename)

    def _save_xml(self):

        _, _, extension = get_file_split(self.file)

        xmlstr = minidom.parseString(ET.tostring(self.root)).toprettyxml()

        if extension == '.gfs':
            xmlstr = xmlstr.replace('<?xml version="1.0" ?>', '')
            xmlstr = re.sub('^\s*\n', '', xmlstr)

        filename = self.prepare_save_path()

        with open(filename, "w") as f:
            f.write(xmlstr)
