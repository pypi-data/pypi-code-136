import importlib
import math
import zlib

from . import config
from . import io_c
from . import io_mod
from . import io_std
from .util import DiskCache, LazyImport

pyfaidx = LazyImport("pyfaidx", path=config.PYFAIDX_MOD)

CACHE = None
BIN_SIZE = 10
DEFAULT_VALUE = 0
FILL_ENTRIES = False


class LociSignalReader:

    def __init__(self, chr_ids, starts, ends, strands=None, cache=CACHE):
        self.chr_ids = list(chr_ids)
        self.starts = list(starts)
        self.ends = list(ends)
        self.strands = None if strands is None else list(strands)
        self.cache = cache
        self.sorting_indices = None
        if self.cache is not None:
            locations = [
                [str(chr_id), int(start), int(end), index]
                for index, (chr_id, start, end) in
                enumerate(zip(self.chr_ids, self.starts, self.ends))]
            for index in range(2, -1, -1):
                locations.sort(key=lambda location: location[index])
            self.chr_ids, self.starts, self.ends, self.sorting_indices = zip(*locations)
            cache_data = [self.chr_ids, self.starts, self.ends]
            self.cache = DiskCache(self.cache, "loci_signal", cache_data)

    @classmethod
    def from_starts(cls, chr_ids, starts, span, cache=CACHE):
        starts = list(starts)
        ends = (start + span for start in starts)
        return cls(chr_ids, starts, ends, cache)

    @classmethod
    def from_centers(cls, chr_ids, centers, span, cache=CACHE):
        centers = list(centers)
        left_span = math.floor(span / 2)
        right_span = math.ceil(span / 2)
        starts = (center - left_span for center in centers)
        ends = (center + right_span for center in centers)
        return cls(chr_ids, starts, ends, cache)

    def read(self, path, bin_size=BIN_SIZE, default_value=DEFAULT_VALUE):
        if self.cache:
            cache_path = self.cache.get_path([path, bin_size, default_value])
            if self.cache.exists(cache_path):
                return self.cache.read(cache_path)
        file_type = get_signal_file_type(path)
        if file_type == "bigwig":
            with BigwigReader(path, bin_size, default_value) as reader:
                data = reader.read_loci_values(self.chr_ids, self.starts, self.ends)
        elif file_type == "bigbed":
            with BigbedReader(path, bin_size) as reader:
                data = reader.read_loci_values(self.chr_ids, self.starts, self.ends)
        elif file_type == "bam":
            with BamReader(path, bin_size) as reader:
                data = reader.read_loci_values(self.chr_ids, self.starts, self.ends)
        else:
            raise RuntimeError(f"neither bigwig, bigbed or bam: {path}")
        if self.cache is not None:
            self.cache.write(cache_path, data)
        if self.sorting_indices is not None:
            data = [data[index] for index in self.sorting_indices]
        if self.strands is not None:
            data = list(strand_loci_values(data, self.strands))
        return data


class SignalReader:

    def __init__(self, reader):
        self.reader = reader
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.reader.close()

    @property
    def chr_sizes(self):
        return self.reader.chr_sizes

    def iter_loci_values(self, chr_ids, starts, ends):
        return self.reader.iter_loci_values(chr_ids, starts, ends)
    
    def read_loci_values(self, chr_ids, starts, ends):
        return list(self.iter_loci_values(chr_ids, starts, ends))

    def iter_loci_entries(self, chr_ids, starts, ends):
        return self.reader.iter_loci_entries(chr_ids, starts, ends)

    def read_loci_entries(self, chr_ids, starts, ends):
        return list(self.iter_loci_entries(chr_ids, starts, ends))

    def iter_chr_entries(self, chr_id):
        return self.reader.iter_chr_entries(chr_id)

    def read_chr_entries(self, chr_id):
        return list(self.iter_chr_entries(chr_id))

    def iter_entries(self, chr_id):
        for chr_id in self.chr_sizes:
            yield from self.reader.iter_chr_entries(chr_id)

    def read_entries(self):
        return list(self.read_entries())


class BigwigReader(SignalReader):

    def __init__(self, path, bin_size=BIN_SIZE, default_value=DEFAULT_VALUE, fill_entries=FILL_ENTRIES):
        self.path = path
        self.bin_size = bin_size
        self.default_value = default_value
        self.fill_entries = fill_entries
        super().__init__(get_signal_reader("bigwig")(path, bin_size, default_value))

    def iter_loci_entries(self, chr_ids, starts, ends):
        loci_entries = self.reader.iter_loci_entries(chr_ids, starts, ends)
        if self.fill_entries:
            for entries, chr_id, start, end in zip(loci_entries, chr_ids, starts, ends):
                entries = fill_locus_entries(entries, chr_id, self.default_value, start, end)
                entries = merge_locus_entries(entries)
                yield list(entries)
        else:
            yield from loci_entries

    def iter_chr_entries(self, chr_id):
        entries = self.reader.iter_chr_entries(chr_id)
        if self.fill_entries:
            end = self.chr_sizes[chr_id]
            entries = fill_locus_entries(entries, chr_id, self.default_value, 0, end)
            entries = merge_locus_entries(entries)
        yield from entries


class BigbedReader(SignalReader):

    def __init__(self, path, bin_size=BIN_SIZE):
        self.path = path
        self.bin_size = bin_size
        super().__init__(get_signal_reader("bigbed")(path, bin_size))


class BamReader(SignalReader):

    def __init__(self, path, bin_size=BIN_SIZE):
        self.path = path
        self.bin_size = bin_size
        super().__init__(get_signal_reader("bam")(path, bin_size))


def read_loci_signal(path, chr_ids, starts, ends, strands=None, bin_size=BIN_SIZE, default_value=DEFAULT_VALUE, cache=CACHE):
    reader = LociSignalReader(chr_ids, starts, ends, strands=strands, cache=cache)
    return reader.read(path, bin_size=bin_size, default_value=default_value)


def read_loci_sequence(source_path, chr_ids, starts, ends):
    sequences = []
    with pyfaidx.Fasta(source_path) as fa:
        for chr_id, start, end in zip(chr_ids, starts, ends):
            sequences.append(fa.get_seq(chr_id, start, end))
    return sequences


def strand_loci_values(loci_values, strands):
    for values, strand in zip(loci_values, strands):
        if strand == "-":
            values.reverse()
        elif strand != "+":
            raise ValueError(f"invalid strand: {strand} (+ or -)")
        yield values


def fill_locus_entries(entries, chr_id, default_value, start=None, end=None):
    last_entry = [None, None, start, None]
    for entry in entries:
        try:
            if entry[1] > last_entry[2]:
                yield [chr_id, last_entry[2], entry[1], default_value]
        except Exception:
            if last_entry[2] is not None:
                raise
        yield entry
        last_entry = entry
    if last_entry[0] is None:
        if start is not None and end is not None and end > start:
            yield [chr_id, start, end, default_value]
    elif end is not None and last_entry[2] < end:
        yield [chr_id, last_entry[2], end, default_value]


def merge_locus_entries(entries):
    last_entry = None
    for entry in entries:
        if last_entry is None:
            last_entry = entry
            continue
        if entry[1] <= last_entry[2] and entry[3] == last_entry[3]:
            last_entry[2] = entry[2]
            continue
        yield entry
    if last_entry is not None:
        yield entry


def get_signal_file_type(path):
    with open(path, "rb") as file:
        chunk = file.read(4)
        if chunk in (b"&\xfc\x8f\x88", b"\x88\x8f\xfc&"):
            return "bigwig"
        if chunk in (b"\xeb\xf2\x89\x87", b"\x87\x89\xf2\xeb"):
            return "bigbed"
        if chunk[:2] == b"\x1f\x8b":
            chunk += file.read(65536 - 4)
            try:
                decompressed_chunk = zlib.decompress(chunk, 31)
                if decompressed_chunk[:4] == b"BAM\x01":
                    return "bam"
            except Exception:
                pass
    return None


def get_signal_reader(file_type):
    targets = dict(
        bigwig=["BigwigReader", "BIGWIG_READER_BIN", "pyBigWig"],
        bigbed=["BigbedReader", "BIGBED_READER_BIN", "pyBigWig"],
        bam=["BamReader", None, "pysam"])
    reader_name, c_lib_bin, py_mod_name = targets[file_type]
    if config.FORCE_STD_LIB:
        return getattr(io_std, reader_name)
    if c_lib_bin and getattr(config, c_lib_bin):
        return getattr(io_c, reader_name)
    try:
        importlib.import_module(py_mod_name)
        return getattr(io_mod, reader_name)
    except Exception:
        return getattr(io_std, reader_name)


def get_signal_writer(file_type):
    targets = dict(
        bigwig=["BigwigWriter", "BEDGRAPH_TO_BIGWIG_BIN", "pyBigWig"])
    writer_name, c_lib_bin, py_mod_name = targets[file_type]
    if config.FORCE_STD_LIB:
        return getattr(io_std, writer_name)
    if c_lib_bin and getattr(config, c_lib_bin):
        return getattr(io_c, writer_name)
    try:
        importlib.import_module(py_mod_name)
        return getattr(io_mod, writer_name)
    except Exception:
        return getattr(io_std, writer_name)
