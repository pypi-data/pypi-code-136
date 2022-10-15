""" module:: uds.program_file
    :platform: Posix
    :synopsis: A class file for a program file / flash container
    moduleauthor:: Patrick Menschel (menschel.p@posteo.de)
    license:: GPL v3
"""
import pickle
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET
from zipfile import is_zipfile, ZipFile


class ProgrammingFileABC(ABC):

    def __init__(self, filepath: Path):
        self._filepath = None
        self._dictionary = None

        self._load_file(filepath=filepath)

    def get_blocks(self):
        return self._dictionary.get("blocks")

    def get_address_and_length_format_identifier(self):
        """
        A method that returns the address and length format identifier defined in the programming file.
        :return: A dictionary with values for various services.
        """
        return self._dictionary.get("uds_address_and_length_format_identifier")

    @abstractmethod
    def _load_file(self, filepath):
        """
        A method to load the ProgrammingFile
        :param filepath: The Filepath
        :return: Nothing
        """


class ExampleProgrammingFile(ProgrammingFileABC):

    def _load_file(self, filepath):
        """
        Load Blocks from pickle file (Testdata)
        :param filepath: The Filepath
        :return: Nothing
        """
        with open(filepath, "rb") as f:
            self._dictionary = pickle.load(f)
        self._filepath = filepath


def read_index_xml(index_file: str) -> dict:
    pass


def read_odx(odx_file: str) -> dict:
    pass


class OdxElement:

    def __init__(self,
                 tag: str,
                 id_: str,  # ID is identical to the full path of the element starting at some level
                 short_name: Optional[str] = None,
                 long_name: Optional[str] = None,
                 ):
        self.tag = tag
        self.id = id_
        self.short_name = short_name
        self.long_name = long_name

    @classmethod
    def from_element(cls, tree: ET.Element):
        tag = tree.tag
        id_ = tree.attrib.get("ID")
        if not (tag.lower().endswith("s")
                or tag.lower().endswith("-ref")):
            short_name = tree.find(".//SHORT-NAME").text
            long_name = tree.find(".//LONG-NAME").text
            return cls(tag=tag,
                       id_=id_,
                       short_name=short_name,
                       long_name=long_name)

    def to_element(self) -> ET.Element:
        root_node = ET.Element(self.tag, {"ID": self.id})
        if not (self.tag.lower().endswith("s")
                or self.tag.lower().endswith("-ref")):
            ET.SubElement(root_node, "SHORT-NAME").text = self.short_name
            ET.SubElement(root_node, "LONG-NAME").text = self.long_name
        return root_node


class FlashData(OdxElement):

    def __init__(self, id_: str, short_name: str, long_name: str,
                 dataformat: str,
                 encrypt_compress_method: str,
                 data: str,
                 ):
        super().__init__(tag="FLASH-DATA",
                         id_=id_,
                         short_name=short_name,
                         long_name=long_name)
        self.dataformat = dataformat
        self.encrypt_compress_method = encrypt_compress_method
        self.data = data

    @classmethod
    def from_element(cls, tree: ET.Element):
        id_ = tree.attrib.get("ID")
        short_name = tree.find(".//SHORT-NAME").text
        long_name = tree.find(".//LONG-NAME").text
        dataformat = tree.find(".//DATAFORMAT").get("SELECTION")
        encrypt_compress_method = tree.find(".//ENCRYPT-COMPRESS-METHOD").text
        data = tree.find(".//DATA").text
        return cls(id_=id_,
                   short_name=short_name,
                   long_name=long_name,
                   dataformat=dataformat,
                   encrypt_compress_method=encrypt_compress_method,
                   data=data,
                   )

    def to_element(self) -> ET.Element:
        root_node = super(FlashData, self).to_element()
        ET.SubElement(root_node, "DATAFORMAT", {"SELECTION": self.dataformat})
        ET.SubElement(root_node, "ENCRYPT-COMPRESS-METHOD", {"TYPE": "A_BYTEFIELD"}).text = self.encrypt_compress_method
        ET.SubElement(root_node, "DATA").text = self.data
        return root_node


# class OdxFile:
#
#     def __init__(self):
#         self.model_version = "2.0.1"
#         self.short_name = "SOME_NAME"
#         self.long_name = "Some name"
#         self.ecu_mems: Sequence[EcuMemElement] = []
#
#
#     @classmethod
#     def from_etree(cls, tree: ET.ElementTree):
#         pass
#
#     def to_etree(self) -> ET.ElementTree:
#         tree = ET.ElementTree()
#         root_node = tree.getroot()
#         root_node.tag = "ODX"
#         root_node.attrib = {"xsi:noNamespaceSchemaLocation": "odx.xsd", "MODEL-VERSION": self.model_version}
#         flash_node = ET.Element(tag="FLASH", attrib={"ID": self.short_name})
#         root_node.append(flash_node)
#         for tag, text in {"SHORT-NAME": self.short_name,
#                           "LONG-NAME": self.long_name}.items():
#             elem = ET.Element(tag=tag)
#             elem.text = text
#             flash_node.append(elem)
#
#         ecu_mems_node = ET.Element(tag="ECU-MEMS")
#         for ecu_mem in self.ecu_mems:
#             ecu_mems_node.append(ecu_mem.to_element())
#
#
#
#         return tree


class PdxFile(ProgrammingFileABC):

    def _load_file(self, filepath: Path):
        """
        Load a Pdx file
        :param filepath: The Filepath
        :type filepath: Path
        :return: Nothing
        """
        index_file_name = "index.xml"
        if not is_zipfile(filename=filepath) or (filepath.suffix != ".pdx"):
            raise ValueError("Not a PdxFile {0}".format(filepath))
        with ZipFile(file=filepath) as zfp:
            filenames_in_zip = [info.filename for info in zfp.infolist()]
            is_flash_container = index_file_name in filenames_in_zip
            is_bootloader_dataset = (len(filenames_in_zip) == 1) and filenames_in_zip[0].endswith("odx")
            if is_flash_container:
                pass
                # index_file_dict = read_index_xml(zfp.open(index_file_name).read().decode())
                odx_files_in_zip = [filename for filename in filenames_in_zip if (filename.endswith("odx")
                                                                                  or filename.endswith("odx-f"))]
                assert len(odx_files_in_zip) == 1
                pass
                # odx_file = odx_files_in_zip[0]
                # odx_file_dict = read_odx(zfp.open(odx_file).read().decode())

            elif is_bootloader_dataset:
                pass
                # odx_file_dict = read_odx(zfp.open(filenames_in_zip[0]).read().decode())

            else:
                raise NotImplementedError("Unknown pdx variant")

        self._filepath = filepath


FILE_EXT_TO_PROGRAMMING_FILE_MAPPING = {".pkl": ExampleProgrammingFile,
                                        ".pdx": PdxFile,
                                        }


def read_programming_file(filepath: Path) -> ProgrammingFileABC:
    """
    Read a programming file and return a suitable class object.

    :param filepath: The Path to the file.
    :type filepath: Path
    :return: A programming file object.
    :rtype: ProgrammingFileABC
    :raise ValueError: If not successful.
    """
    if not filepath.exists():
        raise ValueError("Filepath does not exist. {0}".format(filepath))
    if filepath.suffix not in FILE_EXT_TO_PROGRAMMING_FILE_MAPPING:
        raise ValueError("No suitable programming file class for extention {0}".format(filepath.suffix))
    programming_file_class = FILE_EXT_TO_PROGRAMMING_FILE_MAPPING.get(filepath.suffix)
    return programming_file_class(filepath=filepath)
