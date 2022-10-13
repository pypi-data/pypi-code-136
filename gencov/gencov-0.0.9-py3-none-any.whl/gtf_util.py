import re

from .util import gz_open, merge_intervals


class GTFEntry:

    __slots__ = (
        "chr", "source", "type", "start", "end",
        "score", "strand", "phase", "attributes")

    attributes_regex = re.compile(r"(\w+)\s+\"([^\"]*)\"")
    attributes_join = " "
    attributes_format = "{} \"{}\";"

    @classmethod
    def read_fields(cls, *fields_values, **fields):
        entry = cls()
        for value, key in zip(fields_values, cls.__slots__):
            setattr(entry, key, value)
        for value, key in fields.items():
            setattr(entry, key, value)
        return entry
        
    @classmethod
    def read_entry(cls, entry):
        return cls.read_fields(*entry)

    @classmethod
    def read_line(cls, line):
        values = line.split("\t")
        entry = cls()
        entry.chr = values[0]
        entry.source = values[1]
        entry.type = values[2]
        entry.start = int(values[3]) - 1
        entry.end = int(values[4])
        entry.score = None if values[5] == "." else float(values[5])
        entry.strand = values[6]
        entry.phase = None if values[7] == "." else int(values[7])
        entry.attributes = cls.read_attributes(values[8])
        return entry

    @classmethod
    def read_attributes(cls, line):
        return dict(
            match.groups()
            for match in cls.attributes_regex.finditer(line))
    
    def to_line(self):
        values = list(self)
        values[3] = str(values[3] + 1)
        values[4] = str(values[4])
        values[5] = "." if values[5] is None else str(values[5])
        values[7] = "." if values[7] is None else str(values[7])
        values[8] = self.to_attributes_line(values[8])
        return "\t".join(values)

    @classmethod
    def to_attributes_line(cls, fields):
        if fields:
            return cls.attributes_join.join(
                cls.attributes_format.format(key, value)
                for key, value in fields.items())
        return "."

    def get_gene_name(self, default=None):
        try:
            return self.attributes["gene_name"]
        except KeyError:
            pass
        if default is None:
            raise ValueError("no gene name attribute")
        return default

    def get_gene_type(self, default=None):
        for attribute in ("gene_type", "gene_biotype"):
            try:
                return self.attributes[attribute]
            except KeyError:
                pass
        if default is None:
            raise ValueError("no gene type attribute")
        return default

    def __repr__(self):
        fields = ", ".join(
            f"{key}={getattr(self, key)!r}"
            for key in self.__slots__)
        return f"{self.__class__.__name__}({fields})"

    def __iter__(self):
        for key in self.__slots__:
            yield getattr(self, key)


class GFF3Entry(GTFEntry):

    attributes_regex = re.compile(r"(\w+)=([^;]*)")
    attributes_join = ";"
    attributes_format = "{}={}"


def iter_gtf_entries(file, format="gtf", select_types=None):
    Entry = dict(gtf=GTFEntry, gff3=GFF3Entry)[format]
    if select_types is None:
        for line in file:
            if line.startswith("#"):
                continue
            yield Entry.read_line(line)
    else:
        type_regex = re.compile(r"[^\t]*\t[^\t]*\t([^\t]*)\t")
        for line in file:
            if line.startswith("#"):
                continue
            entry_type = type_regex.match(line).group(1)
            if entry_type not in select_types:
                continue
            yield Entry.read_line(line)


def entry_to_bed_transcript(entry, exons):
    location = f"{entry.chr}\t{entry.start}\t{entry.end}"
    name = {"Name": entry.get_gene_name(), **entry.attributes}
    name = ";".join(f"{key}={value}" for key, value in name.items())
    name = re.sub(r"\s", " ", name)
    score = 1000 if entry.get_gene_type() == "protein_coding" else 100
    strand = entry.strand or "."
    thick_start = entry.start
    thick_end = entry.end
    item_rgb = 0
    block_count = len(exons)
    block_sizes = ",".join(str(exon[1] - exon[0]) for exon in exons)
    block_starts = ",".join(str(exon[0] - entry.start) for exon in exons)
    return \
        f"{location}\t{name}\t{score}\t{strand}\t" \
        f"{thick_start}\t{thick_end}\t{item_rgb}\t" \
        f"{block_count}\t{block_sizes}\t{block_starts}"


def extract_genes(gtf_path, out_path, gtf_format="gtf"):
    with gz_open(gtf_path, "r") as gtf_file:
        with gz_open(out_path, "w") as out_file:
            out_file.write("chr\tstart\tend\tstrand\tname\tid\ttype\n")
            for entry in iter_gtf_entries(gtf_file, gtf_format, select_types=["gene"]):
                out_file.write("\t".join((
                    entry.chr,
                    str(entry.start),
                    str(entry.end),
                    entry.strand,
                    entry.get_gene_name(default="."),
                    entry.attributes["gene_id"],
                    entry.get_gene_type())))
                out_file.write("\n")


