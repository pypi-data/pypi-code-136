from dataclasses import dataclass
from typing import Optional
import zlib

from .bigwig_header import load_header_data, load_sequence_record, load_sequence, load_one_hot_encoding_from_sequence
from .loader import BufferedDataLoader
from .util import BinaryParser


IDX_MAGIC = 0x2468ACE0
RPTREE_HEADER_SIZE = 48
RPTREE_NODE_LEAF_ITEM_SIZE = 32
RPTREE_NODE_CHILD_ITEM_SIZE = 24
DEFAULT_BUFFER_SIZE = 512000


@dataclass
class BigwigData:
    chr_id: str
    start: int
    end: int
    value: float


@dataclass
class BigbedExon:
    start: int
    end: int


@dataclass
class BigbedData:
    chr_id: str
    start: int
    end: int
    name: Optional[str] = None
    score: Optional[float] = None
    strand: Optional[str] = None
    cd_start: Optional[int] = None
    cd_end: Optional[int] = None
    color: Optional[str] = None
    exons: Optional[list[BigbedExon]] = None


@dataclass
class BigZoomData:
    chr_id: str
    start: int
    end: int
    valid_count: int
    min_value: float
    max_value: float
    sum_data: float
    sum_squares: float


@dataclass
class RPLeafNode:
    start_chr: int
    start_base: int
    end_chr: int
    end_base: int
    data_offset: int
    data_size: int


class BigwigReader:
    """
    main class for dealing with reading bigwig and bigbed files
    """

    def __init__(self, data_loader, buffer_size=DEFAULT_BUFFER_SIZE, must_be=None):
        """
        arguments:
            data_loader: provided class that deals with fetching data
            must_be: requested file type (bigwig, bigbed or twobit)
                can be None to accept any of those three
            buffer_size: size of the buffer used for fetching data,
                used to optimistically read more data than is needed
                for each read of the tree that stores data to avoid
                round trips, the trade-off is potentially reading more
                data than you need to vs making more round trips
        """
        self.cached_header = None
        self.cached_sequence_records = {}
        self.data_loader = data_loader
        self.buffer_size = buffer_size
        self.must_be = must_be
        self._header = None
        self._sequence_records = None

    @property
    def header(self):
        """
        method for getting all header data for data loader's file,
        data is loaded on demand and cached for subsequent requests
        """
        if not self._header:
            self._header = load_header_data(self.data_loader, must_be=self.must_be)
        return self._header

    def get_sequence_record(self, chr_id):
        """
        method for getting a sequence record from a 2bit sequence file,
        this method is not valid for bigwig or bigbed files

        arguments:
            chr_id: name of the chromosome or other sequence to retrieve
        """
        if self.header.file_type != "twobit":
            raise RuntimeError(f"get_sequence_record is not valid on {self.header.file_type} files")
        if not self.cached_sequence_records[chr_id]:
            self.cached_sequence_records[chr_id] = load_sequence_record(self.data_loader, self.header, chr_id)
        return self.cached_sequence_records[chr_id]

    def read_bigwig_data(self, start_chr, start_base, end_chr, end_base):
        """
        method for reading unzoomed wig data from bigwig files
        """
        return self.read_data(
            start_chr, start_base, end_chr, end_base,
            self.header.common.full_index_offset,
            decode_wig_data)

    def read_bigbed_data(self, start_chr, start_base, end_chr, end_base, rest_parser=None):
        """
        method for reading unzoomed bed data from bigbed files
        """
        return self.read_data(
            start_chr, start_base, end_chr, end_base,
            self.header.common.full_index_offset,
            decode_bed_data(rest_parser or parse_bigbed))

    def read_twobit_data(self, chr_id, start_base, end_base):
        """
        method for reading two bit sequence data from twobit files
        """
        sequence = self.get_sequence_record(chr_id)
        return load_sequence(
            self.data_loader, self.header,
            sequence, start_base, end_base)
        
    def read_twobit_data(self, chr_id, start_base, end_base):
        """
        method for reading two bit matrix data from twobit files
        """
        sequence = self.get_sequence_record(chr_id)
        return load_one_hot_encoding_from_sequence(
            self.data_loader, self.header,
            sequence, start_base, end_base)

    def read_zoom_data(self, start_chr, start_base, end_chr, end_base, zoom_level_index):
        """
        method for reading zoomed data from bigwig and bigbed files
        """
        if self.header.zoom_level_headers is None or zoom_level_index not in self.header.zoom_level_headers:
            raise RuntimeError("given zoom_level_index not found in zoom level headers")
        tree_offset = self.header.zoom_level_headers[zoom_level_index].index_offset
        return self.read_data(start_chr, start_base, end_chr, end_base, tree_offset, decode_zoom_data)

    def read_data(self, start_chr, start_base, end_chr, end_base, tree_offset, decode_function):
        """
        method containing all the shared functionality for reading bigwig and bigbed files

        arguments:
            start_chr, start_base, end_chr, end_base: starting or ending chromosome or base pair
            tree_offset: location of the r+ tree that stores the data we're interested
        """
        if self.header.chr_tree is None:
            raise RuntimeError("no chromosome tree found in file header")
        start_chr_index = self.header.chr_tree.chr_to_id[start_chr]
        if start_chr_index is None:
            raise RuntimeError(f"chromosome ${start_chr} not found in file header chromosome tree")
        end_chr_index = self.header.chr_tree.chr_to_id[end_chr]
        if end_chr_index is None:
            raise RuntimeError(f"chromosome ${end_chr} not found in file header chromosome tree")
        # load all leaf nodes within given chr / base bounds for the r+ tree used for actually storing the data
        buffered_loader = BufferedDataLoader(self.data_loader, self.buffer_size)
        magic = BinaryParser(buffered_loader.load(tree_offset, RPTREE_HEADER_SIZE)).read_uint32()
        if magic != IDX_MAGIC:
            raise RuntimeError(f"r+ tree not found at offset ${tree_offset}")
        root_node_offset = tree_offset + RPTREE_HEADER_SIZE
        leaf_nodes = load_leaf_nodes_for_rp_node(
            buffered_loader, self.header.little_endian, root_node_offset,
            start_chr_index, start_base, end_chr_index, end_base)
        # iterate through filtered leaf nodes, load the data, and decode it
        for leaf_node in leaf_nodes:
            leaf_data = buffered_loader.load(leaf_node.data_offset, leaf_node.data_size)
            if self.header.common.uncompress_buffer_size > 0:
                leaf_data = zlib.decompress(leaf_data)
            leaf_decoded_data = decode_function(leaf_data, start_chr_index, start_base, end_chr_index, end_base, self.header.chr_tree.id_to_chr)
            yield from leaf_decoded_data


def load_leaf_nodes_for_rp_node(buffered_loader, little_endian, rp_node_offset, start_chr_index, start_base, end_chr_index, end_base):
    """
    recursively load a list of r+ tree leaf nodes for the given node (by file offset) within given chr / base bounds

    arguments:
        buffered_loader: buffered data loader used to load the node data
        rp_node_offset: offset for the start of the r+ tree node
        start_chr_index: starting chromosome index used for filtering
        start_base: starting base used for filtering
        end_chr_index: ending chromosome index used for filtering
        end_base: ending base used for filtering
    
    yeilds list of simple representations of leaf nodes for the given node offset
    """
    node_header_data = buffered_loader.load(rp_node_offset, 4)
    node_header_parser = BinaryParser(node_header_data, little_endian)
    is_leaf = 1 == node_header_parser.read_uint8()
    node_header_parser.position += 1 # skip reserved space
    count = node_header_parser.read_uint16()
    node_data_offset = rp_node_offset + 4
    bytes_required = count * (RPTREE_NODE_LEAF_ITEM_SIZE if is_leaf else RPTREE_NODE_CHILD_ITEM_SIZE)
    node_data = buffered_loader.load(node_data_offset, bytes_required)
    node_data_parser = BinaryParser(node_data, little_endian)
    for i in range(count):
        node_start_chr = node_data_parser.read_int32()
        node_start_base = node_data_parser.read_int32()
        node_end_chr = node_data_parser.read_int32()
        node_end_base = node_data_parser.read_int32()
        # if this node overlaps with the chr / base range provided
        overlaps = \
            ((end_chr_index > node_start_chr) or (end_chr_index == node_start_chr and end_base >= node_start_base)) and \
            ((start_chr_index < node_end_chr) or (start_chr_index == node_end_chr and start_base <= node_end_base))
        if is_leaf:
            leaf_node = RPLeafNode(
                start_chr=node_start_chr,
                start_base=node_start_base,
                end_chr=node_end_chr,
                end_base=node_end_base,
                data_offset=node_data_parser.read_int64(),
                data_size=node_data_parser.read_int64())
            if overlaps:
                yield leaf_node
        else:
            child_offset = node_data_parser.read_int64()
            if overlaps:
                yield from load_leaf_nodes_for_rp_node(
                    buffered_loader, little_endian, child_offset,
                    start_chr_index, start_base, end_chr_index, end_base)


def parse_bigbed(chr_id, start_base, end_base, rest):
    """
    extract useful data from sections of raw big binary bed data
    """
    entry = BigbedData(
        chr_id=chr_id,
        start=start_base,
        end=end_base)
    tokens = rest.split("\t")
    token_count = len(tokens)
    if token_count > 0:
        entry.name = tokens[0]
    if token_count > 1:
        entry.score = float(tokens[1])
    if token_count > 2:
        entry.strand = tokens[2]
    if token_count > 3:
        entry.cd_start = int(tokens[3])
    if token_count > 4:
        entry.cd_end = int(tokens[4])
    if token_count > 5 and tokens[5] != "." and tokens[5] != "0":
        if "," in tokens[5]:
            color = tokens[5] if tokens[5].startswith("rgb") else f"rgb({tokens[5]})"
        else:
            color = tokens[5]
        entry.color = color
    if token_count > 8:
        exon_count = int(tokens[6])
        exon_sizes = tokens[7].split(",")
        exon_starts = tokens[8].split(",")
        exons = []
        for size, start in zip(exon_sizes, exon_starts):
            exon_start = start_base + int(start)
            exon_end = exon_start + int(size)
            exons.append(dict(start=exon_start, end=exon_end))
        entry.exons = exons
    return entry


def decode_bed_data(rest_parser):
    """
    extract useful data from sections of raw big binary bed data

    arguments:
        rest_parser: parser for reading big bed data
    
    inner arguments:
        data: raw bed data
        filter_start_chr_index: starting chromosome index used for filtering
        filter_start_base: starting base used for filtering
        filter_end_chr_index: ending chromosome index used for filtering
        filter_end_base: ending base used for filtering
        chr_dict: dictionary of indices used by the file to chromosome names, conveniently stored as an array
    """
    def inner(data, filter_start_chr_index, filter_start_base, filter_end_chr_index, filter_end_base, chr_dict):
        binary_parser = BinaryParser(data)
        min_size = 3 * 4 + 1 # minimum number of bytes required for a bed record
        while binary_parser.remaining_length >= min_size:
            chr_index = binary_parser.read_int32()
            chr_id = chr_dict[chr_index];
            start_base = binary_parser.read_int32()
            end_base = binary_parser.read_int32()
            rest = binary_parser.read_string()
            if chr_index < filter_start_chr_index or (chr_index == filter_start_chr_index and end_base < filter_start_base):
                continue
            elif chr_index > filter_end_chr_index or (chr_index == filter_end_chr_index and start_base >= filter_end_base):
                break
            yield rest_parser(chr_id, start_base, end_base, rest)
    return inner


def decode_wig_data(data, filter_start_chr_index, filter_start_base, filter_end_chr_index, filter_end_base, chr_dict):
    """
    extract useful data from sections of raw big binary unzoomed wig data

    arguments:
        data: raw bed data
        filter_start_chr_index: starting chromosome index used for filtering
        filter_start_base: starting base used for filtering
        filter_end_chr_index: ending chromosome index used for filtering
        filter_end_base: ending base used for filtering
        chr_dict: dictionary of indices used by the file to chromosome names, conveniently stored as an array
    """
    decoded_data = []
    binary_parser = BinaryParser(data)
    chr_index = binary_parser.read_int32()
    chr_id = chr_dict[chr_index]
    start_base = binary_parser.read_int32()
    end_base = binary_parser.read_int32()
    item_step = binary_parser.read_int32()
    item_span = binary_parser.read_int32()
    format_type = binary_parser.read_uint8()
    reserved = binary_parser.read_uint8()
    item_count = binary_parser.read_uint16()
    if chr_index < filter_start_chr_index or chr_index > filter_end_base:
        item_count = 0
    while item_count > 0:
        if format_type == 1: # data is stored in bedgraph format
            start_base = binary_parser.read_int32()
            end_base = binary_parser.read_int32()
            value = binary_parser.read_float32()
        elif format_type == 2: # data is stored in variable step format
            start_base = binary_parser.read_int32()
            value = binary_parser.read_float32()
            end_base = start_base + item_span;
        else: # data is stored in fixed step format
            value = binary_parser.read_float32()
            end_base = start_base + item_span
        if chr_index > filter_end_chr_index or (chr_index == filter_end_chr_index and start_base >= filter_end_base):
            # past the end of the range, exit
            break
        elif not (chr_index < filter_start_chr_index or (chr_index == filter_start_chr_index and end_base < filter_start_base)):
            # this is within the range (i.e. not before the first requested base), add this data point
            yield BigwigData(
                chr_id=chr_id,
                start=start_base,
                end=end_base,
                value=value)
        if format_type != 1 and format_type != 2:
            # data is stored in fixed step format, only increment the start base once the last entry has been appended
            start_base += item_step
        item_count -= 1


def decode_zoom_data(data, filter_start_chr_index, filter_start_base, filter_end_chr_index, filter_end_base, chr_dict):
    """
    extract useful data from sections of raw big binary zoom data

    arguments:
        data: raw bed data
        filter_start_chr_index: starting chromosome index used for filtering
        filter_start_base: starting base used for filtering
        filter_end_chr_index: ending chromosome index used for filtering
        filter_end_base: ending base used for filtering
        chr_dict: dictionary of indices used by the file to chromosome names, conveniently stored as an array
    """
    binary_parser = BinaryParser(data)
    min_size = 8 * 4 # minimum # of bytes required for a zoom record
    while binary_parser.remaining_length > min_size:
        chr_index = binary_parser.read_int32()
        decoded_zoom_data = BigZoomData(
            chr_id=chr_dict[chr_index],
            start=binary_parser.read_int32(),
            end=binary_parser.read_int32(),
            valid_count=binary_parser.read_int32(),
            min_value=binary_parser.read_float32(),
            max_value=binary_parser.read_float32(),
            sum_data=binary_parser.read_float32(),
            sum_squares=binary_parser.read_float32())
        if chr_index < filter_start_chr_index or (chr_index == filter_start_chr_index and decoded_zoom_data.end < filter_start_base):
            continue
        elif chr_index > filter_end_chr_index or (chr_index == filter_end_chr_index and decoded_zoom_data.start >= filter_end_base):
            break
        yield decoded_zoom_data
