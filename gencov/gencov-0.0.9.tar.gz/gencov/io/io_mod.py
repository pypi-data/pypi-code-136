import math
import os

from .util import shut_up


class BigwigReader:

    def __init__(self, path, bin_size=10, default_value=0):
        self.path = path
        self.bin_size = bin_size
        self.default_value = default_value
        self.file = open_bigwig(self.path, must_be="bigwig")
        self.reader = self.file.file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.file.close()

    @property
    def chr_sizes(self):
        return dict(self.reader.chroms())

    def iter_loci_values(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            values = self.reader.values(chr_id, start, end)
            values = values[::self.bin_size]
            values = [
                self.default_value if math.isnan(value)
                else value for value in values]
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.intervals(chr_id, start, end)
            if entries is None:
                entries = []
            yield [list(entry) for entry in entries]
    
    def iter_chr_entries(self, chr_id, step=100000):
        chr_end = self.chr_sizes[chr_id]
        last_entry = [None, 0, 0, None]
        for start in range(0, chr_end, step):
            end = min(start + step, chr_end)
            entries = self.reader.intervals(chr_id, start, end)
            if not entries:
                continue
            if entries[0][0] <= last_entry[2]:
                if entries[0][2] == last_entry[3]:
                    entries[0] = list(entries[0])
                    entries[0][0] = last_entry[1]
                elif last_entry[0] is not None:
                    yield last_entry
            elif last_entry[0] is not None:
                yield last_entry
            for entry in entries[:-1]:
                yield [chr_id, *entry]
            last_entry = [chr_id, *entries[-1]]
        if last_entry[0] is not None:
            yield last_entry


class BigbedReader:

    def __init__(self, path, bin_size=10):
        self.path = path
        self.bin_size = bin_size
        self.file = open_bigwig(self.path, must_be="bigbed")
        self.reader = self.file.file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.file.close()

    @property
    def chr_sizes(self):
        return dict(self.reader.chroms())

    def iter_loci_values(self, chr_ids, starts, ends):
        bp_bin_factor = 1 / self.bin_size
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.entries(chr_id, start, end, withString=False)
            if entries is None:
                entries = []
            span = end - start
            bin_count = -(-span // self.bin_size)
            values = [0] * bin_count
            for entry in entries:
                start_index = int(max(entry[0] - start, 0) * bp_bin_factor)
                end_index = int(min(entry[1] - start, span) * bp_bin_factor)
                for index in range(start_index, end_index):
                    values[index] += 1
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.entries(chr_id, start, end, withString=False)
            if entries is None:
                entries = []
            entries = [
                [chr_id, entry[0], entry[1], 1]
                for entry in entries]
            yield entries

    def iter_chr_entries(self, chr_id):
        end = self.chr_sizes[chr_id]
        yield from self.iter_loci_entries([chr_id], [0], [end])[0]


class BamReader:

    def __init__(self, path, bin_size=10):
        self.path = path
        self.bin_size = bin_size
        self.file = open_bam(self.path, require_index=True)
        self.reader = self.file.file
        self._chr_sizes = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.file.close()

    @property
    def chr_sizes(self):
        if self._chr_sizes is None:
            self._chr_sizes = {}
            for chr_id in self.reader.references:
                self._chr_sizes[chr_id] = self.reader.get_reference_length(chr_id)
        return self._chr_sizes

    def iter_loci_values(self, chr_ids, starts, ends):
        bp_bin_factor = 1 / self.bin_size
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.fetch(chr_id, start, end)
            span = end - start
            bin_count = -(-span // self.bin_size)
            values = [0] * bin_count
            for entry in entries:
                start_index = int(max(entry.reference_start - start, 0) * bp_bin_factor)
                end_index = int(min(entry.reference_end - start, span) * bp_bin_factor)
                for index in range(start_index, end_index):
                    values[index] += 1
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.fetch(chr_id, start, end)
            entries = [
                [chr_id, entry.reference_start, entry.reference_end, 1]
                for entry in entries]
            yield entries

    def iter_chr_entries(self, chr_id):
        entries = self.reader.fetch(chr_id)
        for entry in entries:
            yield [chr_id, entry.reference_start, entry.reference_end, 1]


class open_bigwig:

    def __init__(self, path, must_be=None):
        import pyBigWig as pybigwig
        self.path = path
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        self.file = pybigwig.open(self.path)
        if must_be is not None:
            method = dict(bigwig="isBigWig", bigbed="isBigBed")[must_be]
            if not getattr(self.file, method):
                raise Exception(f"not a {must_be} file: {path}")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.file.close()


class open_bam:

    def __init__(self, path, require_index=False):
        from pysam import AlignmentFile
        self.path = str(path)
        self.require_index = require_index
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        if self.require_index and not os.path.isfile(f"{self.path}.bai"):
            raise FileNotFoundError(f"{self.path}.bai")
        with shut_up():
            self.file = AlignmentFile(self.path, "rb")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.file.close()


class BigwigWriter:
    """
    path = "path/to/target.unit.bigwig"
    header = dict(chr1=195471971, chr2=182113224, ...)
    with PyBigwigWriter(path, header) as writer:
        writer.add_entries("chr1", start=3000000, step=10, values=[0, 0, ...])
        writer.add_entries("chr1", start=4000000, step=10, values=[0, 0, ...])
        writer.add_entries("chr2", start=3000000, step=10, values=[0, 0, ...])
    - entries must be added in order (chromosome and coordinate)
    - chromosome order is the one specified in header (name:size by chr)
    - entries in one add_entries() call are successive, starting
      at <start> base pairs and separated by <step> base pairs
    - better if successive calls to add_entry() and add_entries()
      have same <step> and successive values
    - close() must be called once at the end if not used as a context manager
    """

    def __init__(self, output_path, header, accumulator_size=1000000):
        import pyBigWig as pybigwig
        self.output_path = str(output_path)
        self.header = header
        self.output_file = pybigwig.open(self.output_path, "w")
        self.output_file.addHeader(list(self.header.items()))
        self.current_chr_id = None
        self.current_start = None
        self.current_end = None
        self.current_step = None
        self.accumulator = []
        self.accumulator_size = accumulator_size

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        dump_accumulator = exc_type is None
        self.close(dump_accumulator)
    
    def close(self, dump_accumulator=True):
        if dump_accumulator:
            self.dump_accumulator()
        self.output_file.close()

    def dump_accumulator(self):
        if not self.accumulator:
            return
        if self.current_end > self.header[self.current_chr_id]:
            raise ValueError(f"out of bounds entries in {self.current_chr_id}")
        self.output_file.addEntries(
            self.current_chr_id,
            self.current_start,
            values=self.accumulator,
            step=self.current_step,
            span=self.current_step,
            validate=False)
        self.accumulator = []
        self.current_start = self.current_end

    def set_current_chr_id(self, chr_id):
        chrs_names = list(self.header)
        current_chr_id_index = -1 \
            if self.current_chr_id is None \
            else chrs_names.index(self.current_chr_id)
        chr_index = chrs_names.index(chr_id)
        if chr_index != current_chr_id_index + 1:
            raise ValueError(f"chromosome order mismatch at {chr_id}")
        self.current_chr_id = chr_id

    def add_entry(self, chr_id, start, end, value):
        self.add_entries(chr_id, start, end - start, [value])
        
    def add_entries(self, chr_id, start, step, values):
        if chr_id != self.current_chr_id:
            self.dump_accumulator()
            self.set_current_chr_id(chr_id)
            self.current_start = start
            self.current_end = start
            self.current_step = step
        elif start < self.current_end:
            raise ValueError(f"unsorted entries in {self.current_chr_id}")
        elif start > self.current_end or step != self.current_step:
            self.dump_accumulator()
            self.current_start = start
            self.current_end = start
            self.current_step = step
        elif len(self.accumulator) > self.accumulator_size:
            self.dump_accumulator()
        self.accumulator.extend(values)
        self.current_end += len(values) * step
