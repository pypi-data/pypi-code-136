import csv
import os
import re

from .util import gz_open


class Loci:

    def __init__(self, header, loci, origin=None):
        self.header = header
        self.loci = loci
        self.origin = origin

    @classmethod
    def from_file(cls, path, format=None):
        format = (format or gz_open.get_format(path)).lstrip(".").lower()
        if format == "tsv" or format == "txt":
            return cls.from_tsv(path)
        elif format == "csv":
            return cls.read_csv(path)
        elif format[:3] == "xls" or format == "ods":
            return cls.from_excel(path)
        elif format == "bed":
            return cls.read_bed(path)
        raise ValueError(f"unrecognized file format: {format} for {path}")

    @classmethod
    def from_tsv(cls, path):
        with gz_open(path, "r") as file:
            loci = list(csv.reader(file, delimiter="\t"))
        header = loci.pop(0)
        return cls(header, loci, origin=os.path.basename(path))

    @classmethod
    def from_csv(cls, path):
        with gz_open(path, "r") as file:
            loci = list(csv.reader(file))
        header = loci.pop(0)
        return cls(header, loci, origin=os.path.basename(path))

    @classmethod
    def from_excel(cls, path, sheet=None):
        import pandas as pd
        loci = pd.read_excel(path, sheet_name=sheet)
        header = loci.columns.tolist()
        loci = loci.values.tolist()
        return cls(header, loci, origin=os.path.basename(path))

    @classmethod
    def from_bed(cls, path):
        with gz_open(path, "r") as file:
            loci = list(csv.reader(file, delimiter="\t"))
        header = [
            "chr", "start", "end", "name", "score", "strand",
            "thick_start", "thick_end", "item_rgb",
            "block_count", "block_sizes", "block_starts"]
        header = header[:len(loci[0])] if loci else header
        return cls(header, loci, origin=os.path.basename(path))
    
    def get_col_index(self, name):
        try:
            index = self.header.index(name)
        except Exception:
            origin = f" in {self.origin}" if self.origin else ""
            raise ValueError(f"column {name} not found{origin}")
        return index

    def get_col(self, name):
        index = self.get_col_index(name)
        try:
            values = [row[index] for row in self.loci]
        except Exception:
            origin = f" in {self.origin}" if self.origin else ""
            raise ValueError(f"column {name} incomplete{origin}")
        return values
    
    def clean_chr(self):
        regex = re.compile(r"^(chr)?(\d+|x|y)$", re.I)
        chr_ids = self.get_col("chr")
        self.loci = [
            row
            for chr_id, row in zip(chr_ids, self.loci)
            if regex.match(chr_id)]
    
    def set_types(self, types):
        for name, type in types.items():
            index = self.get_col_index(name)
            for row in self.loci:
                try:
                    row[index] = type(row[index])
                except Exception:
                    origin = f" in {self.origin}" if self.origin else ""
                    message = \
                        f"failed to interpret {row[index]} as {type}" \
                        f"in column {name}{origin}"
                    raise ValueError(message)

    def filter(self, name, value, mode="in"):
        comparator = {
            "in": lambda x, y: x == y,
            "out": lambda x, y: x != y}[mode]
        ref_values = self.get_col(name)
        self.loci = [
            locus
            for locus, ref_value in zip(self.loci, ref_values)
            if comparator(ref_value, value)]
    
    def group_by(self, name):
        groups = {}
        ref_values = self.get_col(name)
        for locus, ref_value in zip(self.loci, ref_values):
            try:
                group = groups[ref_value]
            except KeyError:
                group = []
                groups[ref_value] = group
            group.append(locus)
        groups = {
            ref_value: Loci(self.header, loci, origin=self.origin)
            for ref_value, loci in groups.items()}
        return groups


def interpolate_random_loci(chr_ids, locs, count, min_distance=20000):
    error_message = \
        f"failed to interpolate {count} random loci " \
        f"at a min distance of {min_distance} bp " \
        f"using {min(len(chr_ids), len(locs))} input loci as bounds " \
        f"(likely because of an input loci count too low)"
    ranges = {}
    for chr_id, loc in zip(chr_ids, locs):
        try:
            chr_range = ranges[chr_id]
            if loc > chr_range["max"]:
                chr_range["max"] = loc
            elif loc < chr_range["min"]:
                chr_range["min"] = loc
        except KeyError:
            chr_range = dict(min=loc, max=loc)
            ranges[chr_id] = chr_range
    for chr_id, chr_range in ranges.items():
        chr_range["chr_id"] = chr_id
        chr_range["span"] = chr_range["max"] - chr_range["min"]
    ranges = list(ranges.values())
    ranges.sort(key=lambda chr_range: chr_range["span"], reverse=True)
    total_span = sum(chr_range["span"] for chr_range in ranges)
    if not total_span:
        raise RuntimeError(error_message)
    for chr_range in ranges:
        chr_range["sites_to_find"] = int(round(chr_range["span"] / total_span * count))
    ranges = [chr_range for chr_range in ranges if chr_range["sites_to_find"]]
    if ranges and sum(chr_range["sites_to_find"] for chr_range in ranges) < count:
        ranges[0]["sites_to_find"] += count - sum(chr_range["sites_to_find"] for chr_range in ranges)
    else:
        while sum(chr_range["sites_to_find"] for chr_range in ranges) > count:
            if ranges[-1]["sites_to_find"] > 1:
                ranges[-1]["sites_to_find"] -= 1
            else:
                del ranges[-1]
    if not ranges:
        raise RuntimeError(error_message)
    out_chr_ids, out_locs = [], []
    for chr_range in ranges:
        start, end, n = chr_range["min"], chr_range["max"], chr_range["sites_to_find"] + 2
        step = (end - start) / (n - 1)
        if int(step) < min_distance:
            raise RuntimeError(error_message)
        chr_locs = [int(start + step * i) for i in range(n)][1:-1]
        out_chr_ids += [chr_range["chr_id"]] * chr_range["sites_to_find"]
        out_locs += chr_locs
    return out_chr_ids, out_locs

