from . import io_std_lib


class BigwigReader:

    def __init__(self, path, bin_size=10, default_value=0):
        self.path = path
        self.bin_size = bin_size
        self.default_value = default_value
        self.loader = io_std_lib.loader.DataLoader(self.path)
        self.reader = io_std_lib.bigwig.BigwigReader(self.loader, must_be="bigwig")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.loader.close()

    @property
    def chr_sizes(self):
        return self.reader.header.chr_tree.chr_size

    def iter_loci_values(self, chr_ids, starts, ends):
        bp_bin_factor = 1 / self.bin_size
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.read_bigwig_data(chr_id, start, chr_id, end)
            span = end - start
            bin_count = -(-span // self.bin_size)
            values = [self.default_value] * bin_count
            for entry in entries:
                start_index = int(max(entry.start - start, 0) * bp_bin_factor)
                end_index = int(min(entry.end - start, span) * bp_bin_factor)
                value = entry.value
                for index in range(start_index, end_index):
                    values[index] = value
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.read_bigwig_data(chr_id, start, chr_id, end)
            entries = [
                [chr_id, entry.start, entry.end, entry.value]
                for entry in entries]
            yield entries

    def iter_chr_entries(self, chr_id, step=100000):
        chr_end = self.chr_sizes[chr_id]
        last_entry = [None, 0, 0, None]
        for start in range(0, chr_end, step):
            end = min(start + step, chr_end)
            entries = self.reader.read_bigwig_data(chr_id, start, chr_id, end)
            if not entries:
                continue
            if entries[0][1] <= last_entry[2]:
                if entries[0][3] == last_entry[3]:
                    entries[0][1] = last_entry[1]
                elif last_entry[0] is not None:
                    yield last_entry
            elif last_entry[0] is not None:
                yield last_entry
            yield from entries[:-1]
            last_entry = entries[-1]
        if last_entry[0] is not None:
            yield last_entry


class BigbedReader:

    def __init__(self, path, bin_size=10):
        self.path = path
        self.bin_size = bin_size
        self.loader = io_std_lib.loader.DataLoader(self.path)
        self.reader = io_std_lib.bigwig.BigwigReader(self.loader, must_be="bigbed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.loader.close()

    @property
    def chr_sizes(self):
        return self.reader.header.chr_tree.chr_size

    def iter_loci_values(self, chr_ids, starts, ends):
        bp_bin_factor = 1 / self.bin_size
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.read_bigbed_data(chr_id, start, chr_id, end)
            span = end - start
            bin_count = -(-span // self.bin_size)
            values = [0] * bin_count
            for entry in entries:
                start_index = int(max(entry.start - start, 0) * bp_bin_factor)
                end_index = int(min(entry.end - start, span) * bp_bin_factor)
                for index in range(start_index, end_index):
                    values[index] += 1
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.read_bigbed_data(chr_id, start, chr_id, end)
            entries = [
                [chr_id, entry.start, entry.end, 1]
                for entry in entries]
            yield entries

    def iter_chr_entries(self, chr_id):
        yield from self.iter_loci_entries([chr_id], [0], [self.chr_sizes[chr_id]])[0]


class BamReader:

    def __init__(self, path, bin_size=10):
        self.path = path
        self.bai_path = f"{path}.bai"
        self.bin_size = bin_size
        self.loader = io_std_lib.loader.DataLoader(self.path)
        self.bai_loader = io_std_lib.loader.DataLoader(self.bai_path)
        self.reader = io_std_lib.bam.BamReader(self.loader, self.bai_loader)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        self.loader.close()
        self.bai_loader.close()

    @property
    def chr_sizes(self):
        return self.reader.header.chr_lengths

    def iter_loci_values(self, chr_ids, starts, ends):
        bp_bin_factor = 1 / self.bin_size
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.read(chr_id, start, end)
            span = end - start
            bin_count = -(-span // self.bin_size)
            values = [0] * bin_count
            for entry in entries:
                start_index = int(max(entry.start - start, 0) * bp_bin_factor)
                end_index = int(min(entry.start + entry.length_on_ref - start, span) * bp_bin_factor)
                for index in range(start_index, end_index):
                    values[index] += 1
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        for chr_id, start, end in zip(chr_ids, starts, ends):
            entries = self.reader.read(chr_id, start, end)
            entries = [
                [chr_id, entry.start, entry.start + entry.length_on_ref, 1]
                for entry in entries]
            yield entries
            
    def iter_chr_entries(self, chr_id):
        end = self.chr_sizes[chr_id]
        yield from self.iter_loci_entries([chr_id], [0], [end])[0]
