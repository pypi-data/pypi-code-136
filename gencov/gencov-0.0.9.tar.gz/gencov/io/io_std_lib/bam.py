from dataclasses import dataclass
from enum import Enum
import math
from symbol import continue_stmt
from typing import Optional

from .bam_header import read_bam_header
from .bam_index import blocks_for_range, read_bam_index
from .util import BinaryParser, decompress_bgzf


CIGAR_DECODER = "MIDNSHP=X"
SEQ_CONSUMING_CIGAR_OPS = "MIS=X"
REF_CONSUMING_CIGAR_OPS = "MDN=X"
SEQ_DECODER = "=ACMGRSVTWYHKDBN"

class BamAlignmentFlag(Enum):
    READ_PAIRED = 0x1 # template having multiple segments in sequencing
    PROPER_PAIR = 0x2 # each segment properly aligned according to the aligner
    READ_UNMAPPED = 0x4 # segment unmapped
    MATE_UNMAPPED = 0x8 # next segment in the template unmapped
    READ_STRAND = 0x10 # seq being reverse complemented
    MATE_STRAND = 0x20 # seq of the next segment in the template being reverse complemented
    FIRST_OF_PAIR = 0x40 # first segment in the template
    SECOND_OF_PAIR = 0x80 # last segment in the template
    SECONDARY_ALIGNMNET = 0x100 # secondary alignment
    READ_FAILS_VENDOR_QUALITY_CHECK = 0x200 # not passing filters, such as platform/vendor quality controls
    DUPLICATE_READ = 0x400 # pcr or optical duplicate
    SUPPLEMENTARY_ALIGNMENT = 0x800 # supplementary alignment


@dataclass
class CigarOp:
    op_len: int
    op: str
    seq_offset: int


@dataclass
class BamAlignmentMate:
    chr_id: str
    position: int
    strand: bool


@dataclass
class BamAlignment:
    chr_id: str
    start: int
    flags: int
    strand: bool
    read_name: str
    cigar_ops: list[CigarOp]
    template_length: int
    mapping_quality: int
    seq: str
    phred_qualities: list[int]
    length_on_ref: int
    mate: Optional[BamAlignmentMate] = None


def is_flagged(bitwise_flags, flag):
    return not not (bitwise_flags & flag)


class BamReader:
    """
    bam reader class that can read ranges of data from bam alignment files with and index
    needs to read entire index to work, caches index and header
    """

    def __init__(self, loader, index_loader):
        self.loader = loader
        self.index_loader = index_loader
        self._index = None
        self._header = None

    @property
    def index(self):
        if self._index is None:
            self._index = read_bam_index(self.index_loader)
        return self._index
    
    @property
    def header(self):
        if self._header is None:
            self._header = read_bam_header(self.loader)
        return self._header
    
    def read(self, chr_id, start, end):
        ref_id = self.header.chr_to_id[chr_id]
        chunks = blocks_for_range(self.index.ref_data[ref_id], start, end)
        return read_bam(self.loader, self.header, chunks, ref_id, start, end)


def read_bam(loader, header, chunks, ref_id, start, end):
    """
    reads alignments from a bam file given file regions
    to look ("chunks") from an index and search parameters

    arguments:
        loader: data loader for the bam file
        header: bam file header
        chunks: regions to look for matching alignments
        ref_id: file's reference id for the given chromosome
        start, end: as in name
    """
    for chunk in chunks:
        buf_size = chunk.end.block_position + (1 << 16) - chunk.start.block_position
        chunk_bytes = loader.load(chunk.start.block_position, buf_size)
        decompressed_chunk = decompress_bgzf(chunk_bytes)
        chunk_alignments = read_bam_features(
            decompressed_chunk[chunk.start.data_position:],
            header, ref_id, start, end)
        yield from chunk_alignments


def read_bam_features(blocks_data, header, ref_id, bp_start, bp_end):
    parser = BinaryParser(blocks_data)
    while parser.position < len(blocks_data) - 4:
        block_size = parser.read_int32()
        block_end = parser.position + block_size
        if block_size + parser.position > len(blocks_data):
            break # if we don't have enough data to read, exit
        block_ref_id = parser.read_int32()
        if block_ref_id != ref_id:
            parser.position = block_end
            continue # continue if read is unmapped or not on same chr
        start = parser.read_int32()
        read_name_len = parser.read_uint8()
        mapping_quality = parser.read_uint8()
        bin = parser.read_uint16()
        num_cigar_ops = parser.read_uint16()
        flags = parser.read_uint16()
        strand = "-" if is_flagged(flags, BamAlignmentFlag.READ_STRAND.value) else "+"
        seq_len = parser.read_int32()
        mate_ref_id = parser.read_int32()
        mate_pos = parser.read_int32()
        template_len = parser.read_int32()
        read_name = parser.read_string(read_name_len)
        if start > bp_end or start + seq_len < bp_start:
            parser.position = block_end
            continue # continue if read does not overlap with given start-end
        # build cigar
        cigar_ops = []
        seq_offset = 0
        length_on_ref = 0
        for _ in range(num_cigar_ops):
            raw_cigar = parser.read_uint32()
            op_len = raw_cigar >> 4
            op = CIGAR_DECODER[raw_cigar & 0xf]
            cigar_ops.append(CigarOp(op_len=op_len, op=op, seq_offset=seq_offset))
            if op in SEQ_CONSUMING_CIGAR_OPS:
                seq_offset += op_len
            if op in REF_CONSUMING_CIGAR_OPS:
                length_on_ref += op_len
        # build sequence
        seq_chars = []
        seq_bytes = (seq_len + 1) / 2
        for _ in range(int(math.ceil(seq_bytes))):
            seq_byte = parser.read_uint8()
            seq_chars.append(SEQ_DECODER[(seq_byte & 0xf0) >> 4])
            seq_chars.append(SEQ_DECODER[seq_byte & 0x0f])
        # slice because seq_chars might have one extra character (if seq_len is an odd number)
        seq = "".join(seq_chars[:seq_len])
        # build phred-scaled base qualities
        phred_qualities = [parser.read_uint8() for _ in range(seq_len)]
        # add mate
        if mate_ref_id >= 0:
            mate = BamAlignmentMate(
                chr_id=header.id_to_chr[mate_ref_id],
                position=mate_pos,
                strand="-" if is_flagged(flags, BamAlignmentFlag.MATE_STRAND.value) else "+")
        else:
            mate = None
        yield BamAlignment(
            chr_id=header.id_to_chr[block_ref_id],
            start=start,
            flags=flags,
            strand=strand,
            read_name=read_name,
            cigar_ops=cigar_ops,
            template_length=template_len,
            mapping_quality=mapping_quality,
            seq=seq,
            phred_qualities=phred_qualities,
            length_on_ref=length_on_ref,
            mate=mate)
        # we need to jump to the end of the block here because we're skipping reading tags
        parser.position = block_end
