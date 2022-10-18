from __future__ import division, print_function, absolute_import
from typing import AnyStr, List, Tuple, Dict, Optional
from itertools import groupby
import csv
from six import ensure_str, ensure_binary

from pybedtools import BedTool, create_interval_from_list

import json
import os
import argparse

REFERENCE_METADATA_FILE = "reference.json"
REF_TYPE_ATAC = "atac"
REF_TYPE_ATAC_GEX = "atac_gex"
TRANSCRIPT_ANNOTATION_GENE_TYPES = [
    "protein_coding",
    "TR_V_gene",
    "TR_D_gene",
    "TR_J_gene",
    "TR_C_gene",
    "IG_V_gene",
    "IG_D_gene",
    "IG_J_gene",
    "IG_C_gene",
]
DISTANCE_LEFT_OF_TSS = 1000
DISTANCE_RIGHT_OF_TSS = 100
DISTANCE_TO_INTERGENIC = 200000

class ReferenceManager:
    """Class that represents reference metadata. Note that all strings are of type `str`"""

    def __init__(self, path: str):
        self.path = path

        # Load reference metadata
        if self.metadata_file:
            with open(self.metadata_file, "r") as infile:
                self.metadata = json.load(infile)
        else:
            self.metadata = None

        # Load contigs defs
        # Check contigs is a valid JSON first before loading
        try:
            with open(self.contig_definitions, "r") as infile:
                self.contigs = json.load(infile)
                if (
                    "non_nuclear_contigs" in self.contigs
                    and self.contigs["non_nuclear_contigs"] is None
                ):
                    self.contigs["non_nuclear_contigs"] = []

        except ValueError as e:
            raise Exception("Malformed json in '%s': %s" % (self.contig_definitions, e))

        self.all_contigs = []  # type: List[str]
        self.contig_lengths = {}  # type: Dict[str, int]
        with open(self.fasta_index, "r") as infile:
            for line in infile:
                line = line.strip().split()
                name, length = line[0], line[1]
                self.all_contigs.append(name)
                self.contig_lengths[name] = int(length)

    def _filepath_or_error(self, subpaths, err_msg):
        filepath = os.path.join(self.path, *subpaths)
        if not os.path.exists(filepath):
            raise IOError(err_msg)
        return filepath

    def _filepath_or_none(self, subpaths):
        filepath = os.path.join(self.path, *subpaths)
        return filepath if os.path.exists(filepath) else None

    @property
    def metadata_file(self) -> Optional[str]:
        if self._filepath_or_none([REFERENCE_METADATA_FILE]):
            return self._filepath_or_none([REFERENCE_METADATA_FILE])
        else:
            return self._filepath_or_none(["metadata.json"])

    @property
    def genome(self) -> str:
        if self.metadata and "genomes" in self.metadata:
            return "_and_".join(self.metadata["genomes"])
        else:
            filepath = self._filepath_or_error(["genome"], "Reference is missing genome name file")
            with open(filepath) as infile:
                return infile.readline().strip()

    @property
    def contig_definitions(self) -> Optional[str]:
        try:
            return self._filepath_or_error(
                ["fasta", "contig-defs.json"], "Reference is missing contig definition file"
            )
        except IOError:
            return self.metadata_file

    @property
    def fasta(self):
        return self._filepath_or_error(
            ["fasta", "genome.fa"], "Reference is missing genome fasta sequence"
        )

    @property
    def fasta_index(self):
        return self._filepath_or_error(
            ["fasta", "genome.fa.fai"], "Reference is missing fasta index file"
        )

    @property
    def genes(self):
        try:
            return self._filepath_or_error(
                ["genes", "genes.gtf"], "Reference is missing genes.gtf file"
            )
        except IOError:
            return self._filepath_or_error(
                ["genes", "genes.gtf.gz"], "Reference is missing genes.gtf[.gz] file"
            )

    @property
    def motifs(self):
        return self._filepath_or_none(["regions", "motifs.pfm"])

    @property
    def blacklist_track(self):
        return self._filepath_or_none(["regions", "blacklist.bed"])

    @property
    def ctcf_track(self):
        return self._filepath_or_none(["regions", "ctcf.bed"])

    @property
    def dnase_track(self):
        return self._filepath_or_none(["regions", "dnase.bed"])

    @property
    def enhancer_track(self):
        return self._filepath_or_none(["regions", "enhancer.bed"])

    @property
    def promoter_track(self):
        return self._filepath_or_none(["regions", "promoter.bed"])

    @property
    def tss_track(self):
        return self._filepath_or_none(["regions", "tss.bed"])

    @property
    def transcripts_track(self):
        return self._filepath_or_none(["regions", "transcripts.bed"])

    @property
    def all_bed_files(self):
        fpaths = [
            self.tss_track,
            self.transcripts_track,
            self.ctcf_track,
            self.blacklist_track,
            self.dnase_track,
            self.enhancer_track,
            self.promoter_track,
        ]
        return [path for path in fpaths if path]

    @property
    def get_header_string(self):
        header = []
        header.append("# reference_path={}\n".format(self.path).encode())
        if self.metadata is not None:
            header.append(
                "# reference_fasta_hash={}\n".format(self.metadata.get("fasta_hash", "")).encode()
            )
            header.append(
                "# reference_gtf_hash={}\n".format(
                    self.metadata.get("gtf_hash") or self.metadata.get("gtf_hash.gz", "")
                ).encode()
            )
            header.append(
                "# reference_version={}\n".format(self.metadata.get("version", "")).encode()
            )
            header.append(
                "# mkref_version={}\n".format(self.metadata.get("mkref_version", "")).encode()
            )
        else:
            header.append(b"# reference_fasta_hash=\n")
            header.append(b"# reference_gtf_hash=\n")
            header.append(b"# reference_version=\n")
            header.append(b"# mkref_version=\n")
        header.append(b"#\n")

        for contig in self.primary_contigs():
            header.append("# primary_contig={}\n".format(contig).encode())
        return header

    # TODO: make all these functions properties (and update usage)
    def non_nuclear_contigs(self) -> List[str]:
        """Lists non-nuclear contigs (e.g. mitochondria and chloroplasts)"""
        key = "non_nuclear_contigs"
        return self.contigs[key] if key in self.contigs else []

    def get_contig_lengths(self):
        return self.contig_lengths

    def get_vmem_est(self):
        total_contig_len = sum(self.contig_lengths.values())
        return 1.2 * total_contig_len / 1e9

    def primary_contigs(self, species: Optional[str] = None) -> List[str]:
        """List all primary contigs, optionally filter by species."""
        species_prefixes = self.list_species()
        if species is not None:
            assert isinstance(species, str)
            if species not in species_prefixes:
                raise ValueError("Unknown species")
        return [
            x for x in self.contigs["primary_contigs"] if self.is_primary_contig(x, species=species)
        ]

    def list_species(self) -> List[str]:
        """Look for species_prefixes key present in ATAC <= 1.2 references in
        the contig-defs.json

        In newer ARC refences this information is instead in the reference.json
        in the `genomes` key used by cellranger.

        Note however that the `genomes` key is ignored for single-species
        reference and is instead defined as `[""]`
        """
        pres = self.contigs.get("species_prefixes")
        if pres:
            return pres

        pres = self.contigs.get("genomes")
        if pres is None or len(pres) == 1:
            return [""]
        return pres

    def is_primary_contig(self, contig_name: str, species: Optional[str] = None) -> bool:
        assert isinstance(contig_name, str)
        assert species is None or isinstance(species, str)
        if contig_name not in self.contigs["primary_contigs"]:
            return False
        if species is not None and self.species_from_contig(contig_name) != species:
            return False
        return True

    def species_from_contig(self, contig: str) -> str:
        """Given the name of a contig, extract the species."""
        assert isinstance(contig, str)
        species_prefixes = self.list_species()
        if species_prefixes == [""]:
            return ""

        s = contig.split("_")
        if len(s) > 1:
            return s[0]
        else:
            return ""

    def make_chunks(self, max_chunks: int, contigs: Optional[List[str]] = None) -> List[List[str]]:
        """Divide the contigs in a reference into roughly equal-size chunks.

        Note that this is a very simple heuristic and will not always work for various
        combinations of contig sizes and number of chunks. Any empty chunks are dropped.

        Args:
            max_chunks (int): maximum desired number of chunks
            contigs (List[str], optional): Provide a custom list of contigs to partition. If not
            specified, we partition all contigs into chunks. Defaults to None.

        Returns:
            List[List[str]]: A list of chunks, where each chunk is a list of contig names. There
            will be atmost max_chunks chunks.
        """

        assert max_chunks > 0
        if contigs is None:
            contigs = list(self.contig_lengths.keys())
        contigs.sort(key=lambda c: self.contig_lengths[c])
        chunks = [[] for _ in range(max_chunks)]
        index = 0
        reverse = False
        while contigs:
            contig = contigs.pop()
            chunks[index].append(contig)
            index += -1 if reverse else 1
            if not reverse and index == len(chunks):
                reverse = True
                index -= 1
            if reverse and index == -1:
                reverse = False
                index = 0
        return [chunk for chunk in chunks if chunk]

    def verify_contig_defs(self):
        """Verify that the contig defs are correctly formatted"""

        def check_aos(a):
            if not isinstance(a, list):
                return False

            for k in a:
                if not isinstance(k, str):
                    return False
            return True

        # Step 1 does the file exist? -> duplicated functionality in contig_definitions
        if not os.path.exists(self.contig_definitions):
            return "Contig definitions file '%s' is missing" % (self.contig_definitions)

        # Step 2 is it valid JSON? -> implemented before loading during
        # ReferenceManager initiation
        contigs = self.contigs

        # Step 3: species_prefixes must be an array of strings
        species_prefixes = self.list_species()
        if not check_aos(species_prefixes):
            return "Species_prefixes must be an array of strings"
        if len(species_prefixes) == 1 and species_prefixes[0] != "":
            return "Cannot specify species prefix for single species references"

        # Step 4: primary contigs must be an array of strings
        if not check_aos(contigs.get("primary_contigs")):
            return "Primary_contigs must be an array of strings"

        # Step 5: prefix contigs can not be prefixes of themselves, and shouldn't
        # contain underscores
        for p1 in species_prefixes:
            for p2 in species_prefixes:
                if p1 != p2 and p1.startswith(p2):
                    return "Species_prefixes are ambiguous. No prefix may be a prefix of another prefix."
        for p in species_prefixes:
            if "_" in p:
                return "species prefix {} contains and underscore. Underscores are not allowed in species prefixes".format(
                    p
                )

        # step 6: every primary contig and non_nuclear_contigs must be prefixed by a species prefix. Also, every
        # species prefix must be used
        used_prefix = {p: False for p in species_prefixes}
        for c in contigs["primary_contigs"] + contigs["non_nuclear_contigs"]:
            ok = False
            c = str(c)
            for p in species_prefixes:
                if c.startswith(p):
                    used_prefix[p] = True
                    ok = True
                if c == p:
                    return "Species prefix {} matches a contig completely. Species should be a partial prefix to contig".format(
                        p
                    )
            if not ok:
                return "Each primary contig must be prefixed by a species prefix"
        not_used_prefix = [p for p in species_prefixes if not used_prefix[p]]
        if len(not_used_prefix) > 0:
            return (
                "Species prefixes {} are not prefixes for any contigs in the genome fasta".format(
                    ",".join(used_prefix)
                )
            )

        # Step 7: every primary contig and non_nuclear_contigs must exist in the
        # reference
        all_fasta_contigs = []

        for line in open(self.fasta_index):
            fields = line.strip().split()
            all_fasta_contigs.append(fields[0])

        for c in contigs["primary_contigs"] + contigs["non_nuclear_contigs"]:
            if c not in (all_fasta_contigs):
                return (
                    "Contig %s is in the config definition but not in the genome fasta. Please check if the reference is properly built."
                    % (c)
                )

        # Step 8: there must be a primary contig
        if len(contigs["primary_contigs"]) == 0:
            return "At least one contig must be primary."

        return None

def get_peak_nearby_genes(peak):
    """parse peaks with closest TSS and overlaped transcript

    :param peak: can be 6 columns when a peak has closest TSS and also overlaps with a transcript:
                 chr1 937133 937621 ISG15 -616 ISG15
                 or just 5 column if the peak doesn't overlap with any transcript
                 chr1 937133 937621 ISG15 -616
                 the 4th and 6th (if present) column is a string in which gene symbols are separated by comma
                 the 5th column is distance values separated by comma
                 column 1 to 5 are required and column 6 is optional
    :return: Interval object created from a list like ['chr1', '6051602', '6053638', 'KCNAB2', '0', 'promoter'].
    If a peak is associated with multiple annotations, an interval object will be created for each annotation.
    """
    genes = list(peak[3].split(","))

    # In a case where an entire chromosome is called a peak and >1000 TSS
    # are identified as closest, BedTools does not report distances
    distances = [] if len(peak.fields) < 5 else list(peak[4].split(","))
    peak_types = []

    # call promoter peaks first
    is_promoter = {}
    for i, dist in enumerate(distances):
        dist = int(dist)
        if -dist <= DISTANCE_LEFT_OF_TSS and dist <= DISTANCE_RIGHT_OF_TSS:
            is_promoter[genes[i]] = True

    # call distal peaks
    is_distal = {}
    for i, dist in enumerate(distances):
        dist = int(dist)
        if -dist <= DISTANCE_LEFT_OF_TSS and dist <= DISTANCE_RIGHT_OF_TSS:
            peak_types.append("promoter")

        elif abs(dist) <= DISTANCE_TO_INTERGENIC:
            # distal peaks, if this peak is already a promoter of the gene being tested, do not annotate it again as a distal peak
            if genes[i] in is_promoter:
                genes[i] = ""
                distances[i] = ""
                peak_types.append("")
            else:
                peak_types.append("distal")
                is_distal[genes[i]] = True
        else:
            genes[i] = ""
            distances[i] = ""
            peak_types.append("")

        if genes.count("") == len(genes):
            genes, distances, peak_types = [], [], []

    # if a peak has an overlapping gene AND it has not been annotated as the promoter peak of that gene , call distal peaks
    if len(list(peak)) > 5:
        for gene in peak[5].split(","):
            if gene not in is_promoter and gene not in is_distal:
                distances.append("0")
                peak_types.append("distal")
                genes.append(gene)

    # if the peak still has not been annotated, it is an intergenic peak
    if peak_types == []:
        peak_types.append("intergenic")
        genes = [""]
        distances = [""]

    # clean up and unify
    assert len(genes) == len(peak_types)
    annos = set(anno for anno in zip(genes, distances, peak_types) if anno != ("", "", ""))
    genes, distances, peak_types = zip(*sorted(annos))

    intervals = []
    for gene, dist, ptype in zip(genes, distances, peak_types):
        i = create_interval_from_list([peak[0], peak[1], peak[2], gene, dist, ptype])
        intervals.append(i[:])
    return intervals


def remove_duplicate_features(old_bed_file, new_bed_file):
    """Remove duplicate features, distances from a BED file

    A BED entry of the form:

    1    100    200    a,a,b    30,30,40

    is turned into:
    1    100    200    a,b    30,40

    Args:
        old_bed_file (AnyStr): BED file with duplicate feature entries
        new_bed_file (AnyStr): BED file with de-duplicated entries
    """
    with open(new_bed_file, "w") as out:
        for line in BedTool(old_bed_file):
            fields = line.fields
            seen = set()
            features = fields[3].split(",")
            dists = fields[4].split(",")
            new_features = []
            new_dists = []
            for f, d in zip(features, dists):  # pylint: disable=invalid-name
                if (f, d) in seen:
                    continue
                new_features.append(f)
                new_dists.append(d)
                seen.add((f, d))
            out_str = "{}\t{}\t{}\t{}\t{}\n".format(
                fields[0], fields[1], fields[2], ",".join(new_features), ",".join(new_dists)
            )
            out.write(out_str)


def annotate_peaks(peaks, ref_path):
    """Annotate peaks.

    peak to gene annotation strategy:
        1. if a peak overlaps with promoter region (-1kb, + 100) of any TSS, call it a promoter peak
        2. if a peak is within 200kb of the closest TSS, AND if it is not a promoter peak, call it a distal peak
        3. if a peak overlaps of a transcript, AND it is not a promoter nor a distal peak of the gene, call it a distal peak
            This step is optional
        4. call it an intergenic peak
    """

    ref_mgr = ReferenceManager(ref_path)
    tss = BedTool(ref_mgr.tss_track)

    # if tss.bed contains the 7th column (gene type), then apply filter. Otherwise use all tss sites
    if tss.field_count() == 7:
        tss_filtered = tss.filter(lambda x: x[6] in TRANSCRIPT_ANNOTATION_GENE_TYPES).saveas()
    else:
        df_tss = tss.to_dataframe()
        df_tss["gene_type"] = "."
        tss_filtered = BedTool.from_dataframe(df_tss).saveas()

    # including transcripts.bed is optional
    if ref_mgr.transcripts_track is None:
        transcripts_filtered = BedTool([])
    else:
        transcripts = BedTool(ref_mgr.transcripts_track)
        if transcripts.field_count() == 7:
            transcripts_filtered = transcripts.filter(
                lambda x: x[6] in TRANSCRIPT_ANNOTATION_GENE_TYPES
            ).saveas()
        else:
            df_tx = transcripts.to_dataframe()
            df_tx["gene_type"] = "."
            transcripts_filtered = BedTool.from_dataframe(df_tx).saveas()

    # run bedtools closest for peaks against filtered tss, group by peaks and summarize annotations from select columns
    # 1=chrom1 (peaks), 2=start1 (peaks), 3=end1 (peaks), 7=name (tss_filtered),
    # 11=distance of closest feature in B (tss_filtered) to feature in A (peaks) using negative distances for upstream features
    peaks_nearby_tss = (
        peaks.closest(tss_filtered, D="b", g=ref_mgr.fasta_index)
        .groupby(g=[1, 2, 3], c=[7, 11], o=["collapse"])
        .saveas("peaks_nearby_tss_dups.bed")
    )
    assert len(peaks_nearby_tss) == len(peaks)

    # remove duplicate transcript, distance entries
    remove_duplicate_features("peaks_nearby_tss_dups.bed", "peaks_nearby_tss.bed")
    peaks_nearby_tss = BedTool("peaks_nearby_tss.bed")

    results = []
    peaks_nearby_tss_butno_tx = (
        peaks_nearby_tss.intersect(  # pylint: disable=too-many-function-args,unexpected-keyword-arg
            transcripts_filtered, v=True
        ).saveas()
    )
    peaks_nearby_tss_yes_tx = (
        peaks_nearby_tss.intersect(  # pylint: disable=too-many-function-args,unexpected-keyword-arg
            transcripts_filtered, u=True
        ).saveas()
    )
    assert len(peaks_nearby_tss_butno_tx) + len(peaks_nearby_tss_yes_tx) == len(peaks)

    # avoid error when no peaks overlap with any transcipts
    # 1=chrom1 (peaks), 2=start1 (peaks), 3=end1 (peaks),
    # 4=closest TSS, 5=distance of closest TSS, 9=name (transcripts_filtered)
    if len(peaks_nearby_tss_yes_tx) > 0:
        peaks_nearby_tss_and_tx = peaks_nearby_tss_yes_tx.intersect(
            transcripts_filtered, wa=True, wb=True
        ).groupby(g=[1, 2, 3, 4, 5], c=[9], o=["distinct"])
        for peak in peaks_nearby_tss_and_tx:
            results.extend(get_peak_nearby_genes(peak))

        # after the intersection with transcripts the peaks_nearby_tss_and_tx
        # may not include all peaks from peaks_nearby_tss_yes_tx
        # this step ensures that those are included in the peak_annotation.
        peaks_with_transcripts = {
            create_interval_from_list(p[0:5]) for p in peaks_nearby_tss_and_tx
        }
        for peak in peaks_nearby_tss_yes_tx:
            if peak not in peaks_with_transcripts:
                results.extend(get_peak_nearby_genes(peak))

    for peak in peaks_nearby_tss_butno_tx:
        results.extend(get_peak_nearby_genes(peak))

    return results


def read_peak_annotation(peak_annotation_tsv: AnyStr) -> List[Tuple[str, str]]:
    """Parses the peak annotation TSV.

    Args:
        peak_annotation_tsv (AnyStr): path to tsv file with six fields per row
        (chrom, start, end, gene, distance, peak_type)

    Returns:
        List[Tuple[str, str]]: annotations associated with each peak in the format
        ["promoter1;promoter2", "nearby_gene1;nearby_gene2"]
    """
    peak_annotation = []
    if peak_annotation_tsv:
        with open(ensure_str(peak_annotation_tsv), "r") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)  # skip header
            annotations = []
            for row in reader:
                annotations.append([str(field or "") for field in row])
        for _, group in groupby(annotations, lambda x: (x[0], x[1], x[2])):
            promoter = []
            nearby_gene = []
            for row in group:
                if row[5] == "promoter":
                    promoter.append(row[3])
                nearby_gene.append(row[3])
            peak_annotation.append((";".join(promoter), ";".join(nearby_gene)))
    return peak_annotation

def build_gene_id_name_map(ref_mgr):
    """Builds a lookup table that maps the gene ID to the gene name, if it's available.
    Otherwise fall back on the gene ID.  Makes annotation files more understandable.
    """
    gtf_iter = BedTool(ref_mgr.genes)
    id_name_map = {}
    for interval in gtf_iter:
        if interval[2] != "gene":
            continue
        try:
            interval.attrs
        except ValueError as err:
            raise ValueError(
                "Parsing error in reading the GTF attributes for interval\n\
                {}\nCheck that no semicolons are present in gene_id, gene_name, \
                or other fields in the the attributes column.\
                ".format(
                    interval
                )
            ) from err

        gene_id = interval.attrs["gene_id"].encode()
        id_name_map[gene_id] = (
            interval.attrs["gene_name"].encode() if "gene_name" in interval.attrs else gene_id
        )

    return id_name_map

def capatsv(bed, ref, tsv):
    ref_mgr = ReferenceManager(ref)
    #sort the peaks on the fasta index file in the reference
    #which is not numerically sorted btw
    peaks = BedTool(bed).sort(g=ref_mgr.fasta_index).saveas()
    annotations = annotate_peaks(peaks, ref)
    #undo the sorting by going into the original input file and getting its chr order
    #need to ditch any # at the top, the file is presumably sorted
    os.system('grep -v "#" '+bed+' | cut -f 1 | uniq > order.txt')
    #use that little text list of chromosomes to sort on here
    annotation_bed = BedTool(annotations).sort(g="order.txt").saveas()
    gene_id_name_map = build_gene_id_name_map(ref_mgr)
    with open(tsv, "wb") as out:
        out.write(b"chrom\tstart\tend\tgene\tdistance\tpeak_type\n")
        for row in annotation_bed:
            for i,c in enumerate(row):
                #the ENSG ID is the fourth entry in this row
                if i==3:
                    #the gene map is in binary form, this is just a regular string, fix it
                    if ensure_binary(c) in gene_id_name_map:
                        c = gene_id_name_map[ensure_binary(c)]
                out.write(ensure_binary(c))
                #only insert a tab if it's not the last column
                if i<5:
                    out.write(b"\t")
            out.write(b"\n")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bed', dest='bed', required=True, help='Path to BED file of peaks to annotate')
    parser.add_argument('--ref', dest='ref', required=True, help='Path to Cellranger ARC reference used in peak calling')
    parser.add_argument('--tsv', dest='tsv', required=True, help='Path to desired annotation TSV output')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    capatsv(args.bed, args.ref, args.tsv)

if __name__ == "__main__":
    main()
