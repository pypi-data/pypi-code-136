from dataclasses import dataclass

from .util import BinaryParser, decompress_bgzf


BAM_MAGIC = 0x014d4142


@dataclass
class BamHeader:
    text: str
    chr_to_id: dict[str, int]
    id_to_chr: list[str]
    chr_lengths: dict[str, int]


class BamHeaderReader:

    def __init__(self, loader, fetch_size=None):
        self.loader = loader
        self.fetch_size = fetch_size or 65536
        self.parser = None
        self.raw_loaded_data = None
    
    def read(self):
        magic = self.read_uint32()
        if magic != BAM_MAGIC:
            raise RuntimeError(f"not a bam file: {self.loader.path}")
        text_length = self.read_int32()
        header_text = self.read_string(text_length)
        ref_count = self.read_int32()
        header = BamHeader(header_text, {}, [], {})
        for ref_id in range(ref_count):
            name_length = self.read_int32()
            ref_name = self.read_string(name_length)
            chr_length = self.read_int32()
            header.chr_to_id[ref_name] = ref_id
            header.id_to_chr.append(ref_name)
            header.chr_lengths[ref_name] = chr_length
        return header
    
    def read_int32(self):
        self.load_if_needed(4)
        return self.parser.read_int32()

    def read_uint32(self):
        self.load_if_needed(4)
        return self.parser.read_uint32()

    def read_string(self, length):
        self.load_if_needed(length)
        return self.parser.read_string(length)
    
    def load_if_needed(self, bytes_needed):
        if self.parser is not None and self.parser.remaining_length >= bytes_needed:
            return
        start = 0 if self.raw_loaded_data is None else len(self.raw_loaded_data)
        new_header_data = self.loader.load(start, self.fetch_size)
        self.raw_loaded_data = \
            new_header_data \
            if self.raw_loaded_data is None \
            else self.raw_loaded_data + new_header_data
        uncompressed_header_data = decompress_bgzf(self.raw_loaded_data)
        current_parser_position = 0 if self.parser is None else self.parser.position
        self.parser = BinaryParser(uncompressed_header_data)
        self.parser.position = current_parser_position

def read_bam_header(loader, fetch_size=None):
    return BamHeaderReader(loader, fetch_size).read()
