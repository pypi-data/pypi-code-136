import array
import os
import struct
import subprocess
import tempfile

from . import config


class BigwigReader:

    def __init__(self, path, bin_size=10, default_value=0):
        self.path = path
        self.bin_size = bin_size
        self.default_value = default_value
        self._chr_sizes = None
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        pass

    @property
    def chr_sizes(self):
        if self._chr_sizes is None:
            self._chr_sizes = get_chr_sizes_from_bigwigbed(self.path, "bigwig")
        return self._chr_sizes

    def iter_loci_values(self, chr_ids, starts, ends):
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        stdin = "".join(f"{c} {s} {e}\n" for c, s, e in zip(chr_ids, starts, ends)).encode()
        cmd = [config.BIGWIG_READER_BIN, self.path, "/dev/stdout", "values", self.bin_size, self.default_value]
        cmd = [str(part) for part in cmd]
        process = subprocess.run(cmd, input=stdin, capture_output=True)
        if process.returncode:
            message = process.stderr.strip().decode()
            raise RuntimeError(f"failed to extract coverage from bigwig: {message}")
        start_index = 0
        for start, end in zip(starts, ends):
            bin_count = -(-(end - start) // self.bin_size)
            end_index = start_index + bin_count * 4
            buffer = process.stdout[start_index:end_index]
            yield array.array("f", buffer).tolist()
            start_index = end_index

    def iter_loci_entries(self, chr_ids, starts, ends):
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        stdin = "".join(f"{c} {s} {e}\n" for c, s, e in zip(chr_ids, starts, ends)).encode()
        cmd = [config.BIGWIG_READER_BIN, self.path, "/dev/stdout", "intervals", 0, 0]
        cmd = [str(part) for part in cmd]
        process = subprocess.run(cmd, input=stdin, capture_output=True)
        if process.returncode:
            message = process.stderr.strip().decode()
            raise RuntimeError(f"failed to extract coverage from bigwig: {message}")
        index = 0
        entry_count_struct = struct.Struct("=I")
        entry_struct = struct.Struct("=IIf")
        for chr_id in chr_ids:
            entry_count, = entry_count_struct.unpack(process.stdout[index:index + 4])
            index += 4
            entries = []
            for _ in range(entry_count):
                entry = [chr_id, *entry_struct.unpack(process.stdout[index:index + 12])]
                index += 12
                entries.append(entry)
            yield entries
        
    def iter_chr_entries(self, chr_id):
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        cmd = [config.BIGWIG_TO_BEDGRAPH_BIN, f"-chrom={chr_id}", self.path, "/dev/stdout"]
        cmd = [str(part) for part in cmd]
        with subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            for line in process.stdout:
                line = line.rstrip().split("\t")
                line[1] = int(line[1])
                line[2] = int(line[2])
                line[3] = float(line[3])
                yield line
            if process.wait():
                message = process.stderr.read().strip()
                raise RuntimeError(f"failed to iter bigwig chr {chr_id}: {message}")


class BigbedReader:

    def __init__(self, path, bin_size=10):
        self.path = path
        self.bin_size = bin_size
        self._chr_sizes = None
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        pass
    
    @property
    def chr_sizes(self):
        if self._chr_sizes is None:
            self._chr_sizes = get_chr_sizes_from_bigwigbed(self.path, "bigbed")
        return self._chr_sizes

    def iter_loci_values(self, chr_ids, starts, ends):
        bp_bin_factor = 1 / self.bin_size
        for start, end, entries in zip(starts, ends, self.iter_loci_entries(chr_ids, starts, ends)):
            span = end - start
            bin_count = -(-span // self.bin_size)
            values = [0] * bin_count
            for entry in entries:
                start_index = int(max(entry[1] - start, 0) * bp_bin_factor)
                end_index = int(min(entry[2] - start, span) * bp_bin_factor)
                value = entry[3]
                for index in range(start_index, end_index):
                    values[index] += value
            yield values

    def iter_loci_entries(self, chr_ids, starts, ends):
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        stdin = "".join(f"{c} {s} {e}\n" for c, s, e in zip(chr_ids, starts, ends)).encode()
        cmd = [config.BIGBED_READER_BIN, self.path, "/dev/stdout"]
        cmd = [str(part) for part in cmd]
        process = subprocess.run(cmd, input=stdin, capture_output=True)
        if process.returncode:
            message = process.stderr.strip().decode()
            raise RuntimeError(f"failed to extract coverage from bigbed: {message}")
        index = 0
        entry_count_struct = struct.Struct("=I")
        entry_struct = struct.Struct("=II")
        for chr_id in chr_ids:
            entry_count, = entry_count_struct.unpack(process.stdout[index:index + 4])
            index += 4
            entries = []
            for _ in range(entry_count):
                entry = [chr_id, *entry_struct.unpack(process.stdout[index:index + 8]), 1]
                index += 8
                entries.append(entry)
            yield entries

    def iter_chr_entries(self, chr_id):
        if not os.path.isfile(self.path):
            raise FileNotFoundError(self.path)
        stdin = f"{chr_id} 0 {self.chr_sizes[chr_id]}\n".encode()
        cmd = [config.BIGBED_READER_BIN, self.path, "/dev/stdout"]
        cmd = [str(part) for part in cmd]
        process = subprocess.run(cmd, input=stdin, capture_output=True)
        if process.returncode:
            message = process.stderr.strip().decode()
            raise RuntimeError(f"failed to extract coverage from bigbed: {message}")
        index = 0
        entry_count_struct = struct.Struct("=I")
        entry_struct = struct.Struct("=II")
        entry_count, = entry_count_struct.unpack(process.stdout[index:index + 4])
        index += 4
        for _ in range(entry_count):
            entry = [chr_id, *entry_struct.unpack(process.stdout[index:index + 8]), 1]
            index += 8
            yield entry


class BigwigWriter:
    """
    path = "path/to/target.unit.bigwig"
    with BigwigWriter(path) as writer:
        writer.add_entry(chr_id, start, end, value)
        writer.add_entries(chr_id, start, step, values)
    - entries must be added in order (chromosome and coordinate)
    - entries in one add_entries() call are successive, starting
      at <start> base pairs and separated by <step> base pairs
    - write_bigwig() and close() must be called once at the end
      if not used as a context manager
    """

    def __init__(self, output_path):
        self.output_path = output_path
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.data = {}
        self.current_chr_id = None
        self.current_bedgraph = None
        self.current_end = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            self.write_bigwig()
        self.close()
    
    def close(self):
        for chr_data in self.data.values():
            chr_data["bedgraph"].close()
        self.tmp_dir.cleanup()

    def write_bigwig(self):
        self.set_current_chr_size()
        chr_order = sorted(chr_data["id"] for chr_data in self.data.values())
        bedgraph_path = os.path.join(self.tmp_dir.name, "bedgraph")
        chr_sizes_path = os.path.join(self.tmp_dir.name, "chr_sizes")
        with open(bedgraph_path, "wb") as bedgraph:
            with open(chr_sizes_path, "w") as chr_sizes:
                for chr_id in chr_order:
                    chr_data = self.data[chr_id]
                    chr_data["bedgraph"].close()
                    with open(chr_data["path"], "rb") as chr_bedgraph:
                        chunk = chr_bedgraph.read(65535)
                        while chunk:
                            bedgraph.write(chunk)
                            chunk = chr_bedgraph.read(65535)
                    chr_sizes.write(f"{chr_id}\t{chr_data['size']}\n")
        cmd = [
            config.BEDGRAPH_TO_BIGWIG_BIN,
            bedgraph_path,
            chr_sizes_path,
            self.output_path]
        subprocess.run(cmd, check=True)

    def set_current_chr_size(self):
        if self.current_chr_id is None:
            return
        self.data[self.current_chr_id]["size"] = self.current_end
        self.current_chr_id = None
        self.current_bedgraph = None
        self.current_end = None

    def new_chr(self, chr_id):
        if chr_id in self.data:
            raise ValueError(f"unordered chromosome at {chr_id}")
        path = os.path.join(self.tmp_dir.name, f"part.{chr_id}")
        bedgraph = open(path, "w")
        self.data[chr_id] = dict(id=str(chr_id), path=path, bedgraph=bedgraph)
        self.current_chr_id = chr_id
        self.current_bedgraph = bedgraph
        self.current_end = 0

    def add_entry(self, chr_id, start, end, value):
        if chr_id != self.current_chr_id:
            self.set_current_chr_size()
            self.new_chr(chr_id)
        elif start < self.current_end:
            raise ValueError(f"unsorted entry at {chr_id}:{start}")
        self.current_bedgraph.write(f"{chr_id}\t{start}\t{end}\t{value}\n")
        self.current_end = end

    def add_entries(self, chr_id, start, step, values):
        if chr_id != self.current_chr_id:
            self.set_current_chr_size()
            self.new_chr(chr_id)
        elif start < self.current_end:
            raise ValueError(f"unsorted entry at {chr_id}:{start}")
        for value in values:
            end = start + step
            self.current_bedgraph.write(f"{chr_id}\t{start}\t{end}\t{value}\n")
            start = end
        self.current_end = end


def get_chr_sizes_from_bigwigbed(path, file_type):
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    chr_sizes = {}
    bin_path = dict(bigwig=config.BIGWIG_INFO_BIN, bigbed=config.BIGBED_INFO_BIN)[file_type]
    cmd = [str(part) for part in [bin_path, "-chroms", path]]
    stdout, stderr = subprocess.PIPE, subprocess.PIPE
    with subprocess.Popen(cmd, text=True, stdout=stdout, stderr=stderr) as process:
        section_reached = False
        for line in process.stdout:
            if line.startswith("chromCount"):
                section_reached = True
                continue
            if section_reached:
                if not line.startswith("\t"):
                    break
                line = line.strip().split(" ")
                chr_sizes[line[0]] = int(line[2])
        if process.wait():
            message = process.stderr.read().strip()
            raise RuntimeError(f"failed to get chr sizes from {path}: {message}")
        if not section_reached:
            raise RuntimeError(f"failed to get chr sizes from {path}")
    return chr_sizes
