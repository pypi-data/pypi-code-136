from dataclasses import dataclass
import math
from typing import Optional

from .loader import BufferedDataLoader
from .util import add_in_resize_array, BinaryParser


TWOBIT_MAGIC_LTH = 0x1A412743 # bigwig magic high to low
TWOBIT_MAGIC_HTL = 0x4327411A # bigwig magic low to high
BIGWIG_MAGIC_LTH = 0x888FFC26 # bigwig magic low to high
BIGWIG_MAGIC_HTL = 0x26FC8F88 # bigwig magic high to low
BIGBED_MAGIC_LTH = 0x8789F2EB # bigbed magic low to high
BIGBED_MAGIC_HTL = 0xEBF28987 # bigbed magic high to low
CHR_TREE_MAGIC = 0x78CA8C91 # chr tree magic number
BBFILE_HEADER_SIZE = 64


@dataclass
class CommonHeader:
    bw_version: int
    n_zoom_levels: int
    chr_tree_offset: int
    full_data_offset: int
    full_index_offset: int
    field_count: int
    defined_field_count: int
    auto_sql_offset: int
    total_summary_offset: int
    uncompress_buffer_size: int
    reserved: int


@dataclass
class ZoomLevelHeader:
    index: int
    reduction_level: int
    reserved: int
    data_offset: int
    index_offset: int


@dataclass
class BWTotalSummary:
    bases_covered: int
    min_value: float
    max_value: float
    sum_data: float
    sum_squares: float


@dataclass
class ChrTree:
    magic: int
    block_size: int
    key_size: int
    value_size: int
    item_count: int
    reserved: int
    chr_to_id: dict[str, int]
    chr_size: dict[str, int]
    id_to_chr: list[str]


@dataclass
class HeaderData:
    file_type: str
    little_endian: bool
    common: Optional[CommonHeader]
    zoom_level_headers: Optional[list[ZoomLevelHeader]]
    auto_sql: Optional[str]
    total_summary: Optional[BWTotalSummary]
    chr_tree: Optional[ChrTree] = None
    sequences: Optional[dict[str, int]] = None


def load_header_data(data_loader, must_be=None):
    """
    loads all header data including common headers, zoom headers and chromosome tree

    arguments:
        data_loader: provided class that deals with fetching data
        must_be: requested file type (bigwig, bigbed or twobit)
            can be None to accept any of those three
    """
    # load common headers
    header_data = data_loader.load(0, BBFILE_HEADER_SIZE)
    # try low to high or high to low
    file_type = None
    for little_endian in (True, False):
        binary_parser = BinaryParser(header_data, little_endian)
        magic = binary_parser.read_uint32()
        if magic == (BIGWIG_MAGIC_LTH if little_endian else BIGWIG_MAGIC_HTL):
            file_type = "bigwig"
            break
        elif magic == (BIGBED_MAGIC_LTH if little_endian else BIGBED_MAGIC_HTL):
            file_type = "bigbed"
            break
        elif magic == (TWOBIT_MAGIC_LTH if little_endian else TWOBIT_MAGIC_HTL):
            return load_twobit_header_data(data_loader, little_endian)
    # don't bother with the rest if we haven't figured out the file type
    if must_be is not None and (file_type is None or must_be != file_type):
        raise RuntimeError(f"not a {must_be} file: {data_loader.path}")
    if file_type is None:
        raise RuntimeError(f"not a bigwig, bigbed or twobit file: {data_loader.path}")
    common_header = CommonHeader(
        bw_version=binary_parser.read_uint16(),
        n_zoom_levels=binary_parser.read_uint16(),
        chr_tree_offset=binary_parser.read_int64(),
        full_data_offset=binary_parser.read_int64(),
        full_index_offset=binary_parser.read_int64(),
        field_count=binary_parser.read_uint16(),
        defined_field_count=binary_parser.read_uint16(),
        auto_sql_offset=binary_parser.read_int64(),
        total_summary_offset=binary_parser.read_int64(),
        uncompress_buffer_size=binary_parser.read_int32(),
        reserved=binary_parser.read_int64())
    # load zoom headers and chr tree
    xdata = data_loader.load(
        BBFILE_HEADER_SIZE,
        common_header.full_data_offset - BBFILE_HEADER_SIZE + 5)
    zoom_level_headers = []
    binary_parser = BinaryParser(xdata)
    for i in range(1, common_header.n_zoom_levels + 1):
        zoom_number = common_header.n_zoom_levels - i
        zoom_level_header = ZoomLevelHeader(
            index=zoom_number,
            reduction_level=binary_parser.read_int32(),
            reserved=binary_parser.read_int32(),
            data_offset=binary_parser.read_int64(),
            index_offset=binary_parser.read_int64())
        add_in_resize_array(zoom_level_headers, zoom_number, zoom_level_header)
    # load auto sql
    auto_sql = None
    if common_header.auto_sql_offset > 0:
        binary_parser.position = common_header.auto_sql_offset - BBFILE_HEADER_SIZE
        auto_sql = binary_parser.read_string()
    # load total summary
    total_summary = None
    if common_header.total_summary_offset > 0:
        binary_parser.position = common_header.total_summary_offset - BBFILE_HEADER_SIZE
        total_summary = BWTotalSummary(
            bases_covered=binary_parser.read_int64(),
            min_value=binary_parser.read_float64(),
            max_value=binary_parser.read_float64(),
            sum_data=binary_parser.read_float64(),
            sum_squares=binary_parser.read_float64())
    # load chr data index
    chr_tree = None
    if common_header.chr_tree_offset > 0:
        binary_parser.position = common_header.chr_tree_offset - BBFILE_HEADER_SIZE
        magic = binary_parser.read_uint32()
        if magic != CHR_TREE_MAGIC:
            raise RuntimeError("chromosome id b+ tree not found")
        chr_tree = ChrTree(
            magic=magic,
            block_size=binary_parser.read_int32(),
            key_size=binary_parser.read_int32(),
            value_size=binary_parser.read_int32(),
            item_count=binary_parser.read_int64(),
            reserved=binary_parser.read_int64(),
            chr_to_id={},
            chr_size={},
            id_to_chr=[])
        build_chr_tree(chr_tree, binary_parser)
    return HeaderData(
        file_type=file_type,
        little_endian=little_endian,
        common=common_header,
        zoom_level_headers=zoom_level_headers,
        auto_sql=auto_sql,
        total_summary=total_summary,
        chr_tree=chr_tree)


def build_chr_tree(chr_tree, binary_parser, offset=None):
    """
    recursively build our useful chr-index mapping data from the header's chr tree

    arguments:
        chr_tree: object that stores the data to be built
        binary_parser: binary data parser
        offset: current file offset
    """
    if offset != None:
        binary_parser.position = offset
    node_type = binary_parser.read_uint8()
    binary_parser.position += 1 # skip reserved space
    count = binary_parser.read_uint16()
    # if the node is a leaf
    if node_type == 1:
        for i in range(count):
            key = binary_parser.read_fixed_length_trimmed_string(chr_tree.key_size)
            chr_id = binary_parser.read_int32()
            chr_size = binary_parser.read_int32()
            chr_tree.chr_to_id[key] = chr_id
            add_in_resize_array(chr_tree.id_to_chr, chr_id, key)
            chr_tree.chr_size[key] = chr_size
    else:
        for i in range(count):
            key = binary_parser.read_fixed_length_trimmed_string(chr_tree.key_size)
            child_offset = binary_parser.read_int64()
            buffer_offset = child_offset - BBFILE_HEADER_SIZE
            current_offset = binary_parser.position
            build_chr_tree(chr_tree, binary_parser, buffer_offset)
            binary_parser.position = current_offset


# twobits section
# ---------------


HEADER_BUFFER_SIZE = 32768
BUFFER_SIZE = 3000000
TWOBIT_HEADER_SIZE = 16
LETTERS = {
    "A": [1, 0, 0, 0],
    "C": [0, 1, 0, 0],
    "G": [0, 0, 1, 0],
    "T": [0, 0, 0, 1],
    "N": [0, 0, 0, 0],
    "a": [1, 0, 0, 0],
    "c": [0, 1, 0, 0],
    "g": [0, 0, 1, 0],
    "t": [0, 0, 0, 1],
    "n": [0, 0, 0, 0]}

BASES = []
for i in range(256):
    BASES.append("TCAG"[i >> 6] + "TCAG"[(i >> 4) & 3] + "TCAG"[(i >> 2) & 3] + "TCAG"[i & 3])


@dataclass
class SequenceRecord:
    """
    contains the full sequence data for one reference sequence within the file
    """
    dna_size: int # number of bases in the sequence
    n_block_count: int # number of blocks of N's in the file
    n_block_starts: list[int] # array of start positions for the N blocks
    n_block_sizes: list[int] # array of lengths for the N blocks
    mask_block_count: int # number of masked (lower-case) sequence blocks
    mask_block_starts: list[int] # array of start positions for the masked blocks
    mask_block_sizes: list[int] # array of sizes for the masked blocks
    reserved: int
    offset: int


def load_twobit_header_data(data_loader_r, little_endian):
    """
    loads header data, including the twobit header and sequence indexes, from a twobit file

    arguments:
        data_loader_r: provided class that deals with fetching data
    """

    data_loader = BufferedDataLoader(data_loader_r, HEADER_BUFFER_SIZE)
    # load common headers
    header_data = data_loader.load(0, TWOBIT_HEADER_SIZE)
    # determine endianness
    binary_parser = BinaryParser(header_data, little_endian)
    magic = binary_parser.read_uint32()
    # read the rest of the header
    version = binary_parser.read_uint32()
    sequence_count = binary_parser.read_uint32()
    reserved = binary_parser.read_uint32()
    if version != 0 or reserved != 0:
        raise RuntimeError("failed to determine file type: invalid version or reserved header byte")
    header = HeaderData(
        sequences={},
        little_endian=little_endian,
        file_type="twobit")
    # load sequence index
    offset = TWOBIT_HEADER_SIZE
    for i in range(sequence_count):
        xdata = data_loader.load(offset, 4)
        binary_parser = BinaryParser(xdata, little_endian)
        size = binary_parser.read_uint8()
        offset += 1
        xdata = data_loader.load(offset, size + 4)
        binary_parser = BinaryParser(xdata, little_endian)
        header.sequences[binary_parser.read_string(size)] = binary_parser.read_uint32()
        offset += size + 4
    return header


def load_sequence_record(data_loader_r, header, sequence):
    """
    loads a sequence record from a twobit file

    arguments:
        data_loader_r: class which handles reading ranges from the file
        header: header data, read by load_header_data
        sequence: name of the chromosome or sequence from which to read
    """
    data_loader = BufferedDataLoader(data_loader_r, BUFFER_SIZE)
    if header.sequences[sequence] is None:
        raise RuntimeError(f"chromosome ${sequence} not found in file header chromosome tree")
    data = data_loader.load(header.sequences[sequence], 8)
    binary_parser = BinaryParser(data, header.little_endian)
    offset = header.sequences[sequence] + 8
    r = SequenceRecord(
        dna_size=binary_parser.read_uint32(),
        n_block_count=binary_parser.read_uint32(),
        n_block_starts=[],
        n_block_sizes=[],
        mask_block_count=0,
        mask_block_starts=[],
        mask_block_sizes=[],
        reserved=0,
        offset=0)
    data = data_loader.load(offset, r.n_block_count * 8 + 4)
    offset += r.n_block_count * 8 + 4
    binary_parser = BinaryParser(data, header.little_endian)
    for i in range(r.n_block_count):
        r.n_block_starts.append(binary_parser.read_uint32())
    for i in range(r.n_block_count):
        r.n_block_sizes.append(binary_parser.read_uint32())
    r.mask_block_count = binary_parser.read_uint32()
    data = data_loader.load(offset, r.mask_block_count * 8 + 4)
    offset += r.mask_block_count * 8 + 4
    binary_parser = BinaryParser(data, header.little_endian)
    for i in range(r.mask_block_count):
        r.mask_block_starts.append(binary_parser.read_uint32())
    for i in range(r.mask_block_count):
        r.mask_block_sizes.append(binary_parser.read_uint32())
    r.reserved = binary_parser.read_uint32()
    r.offset = offset
    return r


def load_one_hot_encoding_from_sequence(data_loader, header, sequence, start, end):
    seq = load_sequence(data_loader, header, sequence, start, end) 
    matrix = []
    for c in seq:
        matrix.append(LETTERS[c])
    return matrix


def load_sequence(data_loader, header, sequence, start, end):
    """
    loads sequence data from a two-bit file

    arguments:
        dataLdata_loaderoader: class which handles reading ranges from the file
        header: header data, read by load_header_data
        sequence: sequence record for the chromosome to read from
        start: start position on the chromsome, 0-based and inclusive
        end: end position on the chromosome, 0-based and not inclusive
    """
    interrupting_n_blocks = []
    interrupting_mask_blocks = []
    csequence = ""
    start = 0 if start - 1 < 0 else start - 1
    # find any interrupting blocks of N's
    for i in range(len(sequence.n_block_starts)):
        if sequence.n_block_starts[i] > end:
            break
        if sequence.n_block_starts[i] + sequence.n_block_sizes[i] < start:
            continue
        interrupting_n_blocks.append([sequence.n_block_starts[i], sequence.n_block_sizes[i]])
    # find any interrupting lower-case mask blocks
    for i in range(len(sequence.mask_block_starts)):
        if sequence.mask_block_starts[i] > end:
            break
        if sequence.mask_block_starts[i] + sequence.mask_block_starts[i] < start:
            continue
        interrupting_mask_blocks.append([sequence.mask_block_starts[i], sequence.mask_block_sizes[i]])
    n = math.ceil((end - start) / 4 + math.ceil((start % 4) / 4))
    data = data_loader.load(math.floor(start / 4) + sequence.offset, n)
    binary_parser = BinaryParser(data, header.little_endian)
    for j in range(n):
        csequence += BASES[binary_parser.get_uint8()]
    csequence = csequence[start % 4, start % 4 + end - start]
    # fill in N's
    for i, (block_start, block_size) in enumerate(interrupting_n_blocks):
        block_end = block_start + block_size
        if i == 0 and block_start <= start:
            csequence = \
                "N" * (block_end if block_end <= end else end) - start \
                + csequence[(block_end if block_end < end else end) - start:]
        else:
            csequence = \
                csequence[:block_start - start] \
                + "N" * (block_end if block_end <= end else end) - block_start \
                + csequence[(block_end if block_end < end else end) - start:]
    # set lower case
    for i, (block_start, block_size) in enumerate(interrupting_mask_blocks):
        block_end = block_start + block_size
        if i == 0 and block_start <= start:
            csequence = \
                csequence[:(block_end if block_end <= end else end) - start].lower() \
                + csequence[(block_end if block_end < end else end) - start:]
        else:
            csequence = \
                csequence[:block_start - start] \
                + csequence[block_start - start:(block_end if block_end <= end else end) - start].lower() \
                + csequence[(block_end if block_end < end else end) - start:]
    return csequence
