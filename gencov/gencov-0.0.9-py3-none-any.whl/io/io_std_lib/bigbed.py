from dataclasses import dataclass
from typing import Optional


@dataclass
class BigbedDataNarrowPeak:
    chr_id: str
    start: int
    end: int
    name: Optional[str] = None
    score: Optional[float] = None
    strand: Optional[str] = None # + or - or . for unknown
    signal_value: Optional[int] = None # measurement of average enrichment for the region
    p_value: Optional[int] = None # statistical significance of signal value (-log10), set to -1 if not used
    q_value: Optional[int] = None # statistical significance with multiple-test correction applied (fdr -log10), set to -1 if not used
    peak: Optional[int] = None # point-source called for this peak, 0-based offset from chr_start, set to -1 if no point-source called


@dataclass
class BigbedDataBroadPeak:
    chr_id: str
    start: int
    end: int
    name: Optional[str] = None
    score: Optional[float] = None
    strand: Optional[str] = None # + or - or . for unknown
    signal_value: Optional[int] = None # measurement of average enrichment for the region
    p_value: Optional[int] = None # statistical significance of signal value (-log10), set to -1 if not used
    q_value: Optional[int] = None # statistical significance with multiple-test correction applied (fdr -log10), set to -1 if not used


@dataclass
class BigbedDataMethyl:
    chr_id: str
    start: int
    end: int
    name: Optional[str] = None
    score: Optional[int] = None
    strand: Optional[str] = None # + or - or . for unknown
    thick_start: Optional[int] = None # start of where display should be thick (start codon)
    thick_end: Optional[int] = None # end of where display should be thick (stop codon)
    reserved: Optional[int] = None # color value r, g, b
    read_count: Optional[int] = None # number of reads or coverage
    percent_meth: Optional[int] = None # percentage of reads that show methylation at this position in the genome


@dataclass
class BigbedDataTssPeak:
    chr_id: str
    start: int
    end: int
    name: Optional[str] = None
    score: Optional[float] = None
    strand: Optional[str] = None # + or - or . for unknown
    count: Optional[float] = None # count of reads mapping to this peak
    gene_id: Optional[str] = None # gene identifier
    gene_name: Optional[str] = None # ene name
    tss_id: Optional[str] = None # tss identifier
    peak_cov: Optional[str] = None # base by base read coverage of the peak


@dataclass
class classBigbedDataIdrPeak:
    chr_id: str
    start: int
    end: int
    name: Optional[str] = None
    score: Optional[float] = None
    strand: Optional[str] = None # + or - or . for unknown
    local_idr: Optional[float] = None # local idr value
    global_idr: Optional[float] = None # global idr value
    rep1_chr_start: Optional[int] = None # start position in chromosome of replicate 1 peak
    rep1_chr_end: Optional[int] = None # end position in chromosome of replicate 1 peak
    rep1_count: Optional[float] = None # count (used for ranking) replicate 1
    rep2_chr_start: Optional[int] = None # start position in chromosome of replicate 2 peak
    rep2_chr_end: Optional[int] = None # end position in chromosome of replicate 2 peak
    rep2_count: Optional[float] = None # count (used for ranking) replicate 2


def parse_bigbed_narrow_peak(chr_id, start_base, end_base, rest):
    entry = BigbedDataNarrowPeak(
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
        entry.signal_value = int(tokens[3])
    if token_count > 4:
        entry.p_value = int(tokens[4])
    if token_count > 5:
        entry.q_value = int(tokens[5])
    if token_count > 6:
        entry.peak = int(tokens[6])
    return entry


def parse_bigbed_broad_peak(chr_id, start_base, end_base, rest):
    entry = BigbedDataBroadPeak(
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
        entry.signal_value = int(tokens[3])
    if token_count > 4:
        entry.p_value = int(tokens[4])
    if token_count > 5:
        entry.q_value = int(tokens[5])
    return entry


def parse_bigbed_methyl(chr_id, start_base, end_base, rest):
    entry = BigbedDataMethyl(
        chr_id=chr_id,
        start=start_base,
        end=end_base)
    tokens = rest.split("\t")
    token_count = len(tokens)
    if token_count > 0:
        entry.name = tokens[0]
    if token_count > 1:
        entry.score = int(tokens[1])
    if token_count > 2:
        entry.strand = tokens[2]
    if token_count > 3:
        entry.thick_start = int(tokens[3])
    if token_count > 4:
        entry.thick_end = int(tokens[4])
    if token_count > 5:
        entry.reserved = int(tokens[5])
    if token_count > 6:
        entry.read_count = int(tokens[5])
    if token_count > 7:
        entry.percent_meth = int(tokens[5])
    return entry


def parse_bigbed_tss_peak(chr_id, start_base, end_base, rest):
    entry = BigbedDataTssPeak(
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
        entry.count = float(tokens[3])
    if token_count > 4:
        entry.gene_id = tokens[4]
    if token_count > 5:
        entry.gene_name = tokens[5]
    if token_count > 6:
        entry.tss_id = tokens[6]
    if token_count > 7:
        entry.peak_cov = tokens[7]
    return entry


def parse_bigbed_idr_peak(chr_id, start_base, end_base, rest):
    entry = classBigbedDataIdrPeak(
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
        entry.local_idr = float(tokens[3])
    if token_count > 4:
        entry.global_idr = float(tokens[4])
    if token_count > 5:
        entry.rep1_chr_start = int(tokens[5])
    if token_count > 6:
        entry.rep1_chr_end = int(tokens[6])
    if token_count > 7:
        entry.rep1_count = float(tokens[7])
    if token_count > 8:
        entry.rep2_chr_start = int(tokens[8])
    if token_count > 9:
        entry.rep2_chr_end = int(tokens[9])
    if token_count > 10:
        entry.rep2_count = float(tokens[10])
    return entry
