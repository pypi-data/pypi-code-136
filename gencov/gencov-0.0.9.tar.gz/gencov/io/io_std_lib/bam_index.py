from dataclasses import dataclass
from functools import cmp_to_key

from .util import BinaryParser


BAI_MAGIC = 21578050
PSEUDO_BIN_MAGIC = 37450


@dataclass
class VirtualOffset:
    block_position: int # offset of the compressed data block
    data_position: int # offset into the uncompressed data


@dataclass
class RawChunk:
    start: list[int]
    end: list[int]


@dataclass
class Chunk:
    start: VirtualOffset
    end: VirtualOffset


@dataclass
class BamIndexRefData:
    bin_index: dict[str, list[RawChunk]]
    linear_index: list[list[int]]


@dataclass
class BamIndexData: # top level representation of parsed index
    ref_data: list[BamIndexRefData] # array of index data per reference id, where reference id is array index


def blocks_for_range(index_data, start, end):
    """
    given index data and a range return all possible regions matching alignments could be in
    """
    overlapping_bins = reg_to_bins(start, end)
    bin_index = index_data.bin_index
    linear_index = index_data.linear_index
    # get all chunks for overlapping bins
    all_chunks = []
    for bin in bin_index:
        if bin not in overlapping_bins:
            continue
        inflated_chunks = [inflate_chunk(raw_chunk) for raw_chunk in bin_index[bin]]
        all_chunks.extend(inflated_chunks)
    # use the linear index to find minimum file position of chunks that could contain alignments in the region
    lowest = None
    min_lin = min(start >> 14, len(linear_index) - 1)
    max_lin = max(end >> 14, len(linear_index) - 1)
    for i in range(min_lin, max_lin + 1):
        offset = inflate_virtual_offset(linear_index[i])
        if offset is None:
            continue
        if lowest is None or is_vo_less_than(offset, lowest):
            lowest = offset
    return optimize_chunks(all_chunks, lowest)


def is_vo_less_than(first, second):
    return \
        first.block_position < second.block_position or \
        (first.block_position == second.block_position and first.data_position < second.data_position)


def optimize_chunks(chunks, lowest=None):
    if len(chunks) == 0:
        return []
    chunks.sort(key=optimize_chunks_sort_cmp_key)
    merged_chunks = []
    current_merged_chunk = None
    for chunk in chunks:
        if lowest is not None and is_vo_less_than(chunk.end, lowest):
            continue
        if current_merged_chunk is None:
            current_merged_chunk = chunk
            merged_chunks.append(current_merged_chunk)
        # merge chunks that are withing 65000 of each other
        if (chunk.start.block_position - current_merged_chunk.end.block_position) < 65000:
            if is_vo_less_than(current_merged_chunk.end, chunk.end):
                current_merged_chunk.end = chunk.end
        else:
            current_merged_chunk = chunk
            merged_chunks.append(current_merged_chunk)
    return merged_chunks

def optimize_chunks_sort_cmp(c0, c1):
    diff = c0.start.block_position - c1.start.block_position
    return diff or c0.start.data_position - c1.start.data_position

optimize_chunks_sort_cmp_key = cmp_to_key(optimize_chunks_sort_cmp)


def read_bam_index(index_data_loader):
    """
    read the bam index for the given loader
    """
    return read_bam_index_data(index_data_loader)


def read_bam_index_ref(index_data_loader, ref_id):
    """
    read the bam index for the given loader, only returning data for a single reference id (found in header)

    arguments:
        index_data_loader: loader for bam index file
        ref_id: reference id to provide data for
    """
    return read_bam_index_data(index_data_loader, ref_id).ref_data[ref_id]


def read_bam_index_data(index_data_loader, ref_id=None):
    index_data = index_data_loader.load(0)
    parser = BinaryParser(index_data)
    magic = parser.read_int32()
    if magic != BAI_MAGIC:
        raise RuntimeError(f"not a bai file: {index_data_loader.path}")
    ref_data = []
    num_refs = parser.read_int32() # number of reference sequences
    for ref in range(num_refs):
        if ref_id is None or ref_id == ref:
            ref_id_data = parse_ref_id_data(parser)
            ref_data.append(ref_id_data)
        else:
            skip_ref_id_data(parser)
    return BamIndexData(ref_data=ref_data)


def parse_ref_id_data(parser):
    bin_index = {}
    linear_index = []
    num_bins = parser.read_int32() # number of distinct bins in reference index
    for bin in range(num_bins):
        bin_number = parser.read_int32()
        # we don't care about the metadata in pseudo-bins, so just skip in parser
        if bin_number == PSEUDO_BIN_MAGIC:
            parser.position += 36 # increment by space for 1 int32 and 4 uint64
            continue
        bin_chunks = []
        num_chunks = parser.read_int32()
        for chunk in range(num_chunks):
            chunk_start = read_virtual_offset(parser)
            chunk_end = read_virtual_offset(parser)
            bin_chunks.append(RawChunk(start=chunk_start, end=chunk_end))
        bin_index[bin_number] = bin_chunks
    # add to linear index
    num_intervals = parser.read_int32()
    for interval in range(num_intervals):
        linear_index.append(read_virtual_offset(parser))
    return BamIndexRefData(bin_index=bin_index, linear_index=linear_index)


def skip_ref_id_data(parser):
    num_bins = parser.read_int32() # number of distinct bins in reference index
    for bin in range(num_bins):
        bin_number = parser.read_uint32()
        # we don't care about the metadata in pseudo-bins, so just skip in parser
        if bin_number == PSEUDO_BIN_MAGIC:
            parser.position += 36 # increment by space for 1 int32 and 4 uint64
            continue
        num_chunks = parser.read_int32()
        for chunk in range(num_chunks):
            parser.position += 16 # increment by space for 2 virtual offsets
    num_intervals = parser.read_int32()
    for interval in range(num_intervals):
        parser.position += 8


def stream_raw_bam_index(index_data_loader, ref_id):
    """
    reads an entire bam index and returns a stream of raw index data for only one reference id
    """
    raise NotImplementedError("stream")


def parse_raw_index_ref_data(data):
    """
    parse raw index data from a single reference id
    """
    return parse_ref_id_data(BinaryParser(data))


def read_virtual_offset(parser):
    raw_vo = bytes(parser.read_uint8() for _ in range(8))
    return raw_vo


def inflate_virtual_offset(raw):
    data_position = raw[1] << 8 | raw[0]
    block_position = \
        raw[7] * 0x10000000000 + \
        raw[6] * 0x100000000 + \
        raw[5] * 0x1000000 + \
        raw[4] * 0x10000 + \
        raw[3] * 0x100 + \
        raw[2]
    return VirtualOffset(block_position=block_position, data_position=data_position)


def inflate_chunk(raw):
    return Chunk(
        start=inflate_virtual_offset(raw.start),
        end=inflate_virtual_offset(raw.end))


def reg_to_bins(start, end):
    """
    compute the list of bins that overlap with region [start, end]
    """
    list = [0]
    if end >= 1 << 29:
        end = 1 << 29
    end -= 1
    for k in range(1 + (start >> 26), 1 + (end >> 26) + 1):
        list.append(k)
    for k in range(9 + (start >> 23), 9 + (end >> 23) + 1):
        list.append(k)
    for k in range(73 + (start >> 20), 73 + (end >> 20) + 1):
        list.append(k)
    for k in range(585 + (start >> 17), 585 + (end >> 17) + 1):
        list.append(k)
    for k in range(4681 + (start >> 14), 4681 + (end >> 14) + 1):
        list.append(k)
    return list
