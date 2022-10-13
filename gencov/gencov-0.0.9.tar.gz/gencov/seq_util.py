import os
import subprocess
import tempfile

from .config import GENOMES_DIR
from .io import read_loci_sequence

"""
import numpy as np
BASES_INDEX = "ATGC"



def Sequences:

    def __init__(self, sequences):
        self.sequences = sequences
    
    @classmethod
    def from_strings(cls, strings):
        encoding = dict(
            A=[0], T=[1], G=[2], C=[3],

        )
        sequences = []
        for string in strings:

        
        with gz_open(path, "r") as file:
            loci = list(csv.reader(file, delimiter="\t"))
        header = loci.pop(0)
        return cls(header, loci, origin=os.path.basename(path))
"""


def get_sequences(source_path, chr_ids, starts, ends):
    if os.path.exists(os.path.join(GENOMES_DIR, source_path)):
        source_path = os.path.join(GENOMES_DIR, source_path, f"{source_path}.fa")
    return read_loci_sequence(source_path, chr_ids, starts, ends)


def score_motif_homer(genome_name, motif_path, chr_ids, starts, span):
    with tempfile.TemporaryDirectory() as tmp_dir:
        in_path = os.path.join(tmp_dir, "input.bed")
        out_path = os.path.join(tmp_dir, "output.bed")
        with open(in_path, "w") as in_file:
            for chr_id, start in zip(chr_ids, starts):
                in_file.write(f"{chr_id}\t{start}\t{start + span}\n")
        command = \
            f"export MUGQIC_INSTALL_HOME=/cvmfs/soft.mugqic/CentOS6\n" \
            f"module use $MUGQIC_INSTALL_HOME/modulefiles\n" \
            f"module load mugqic/homer/4.11\n" \
            f"annotatePeaks.pl '{in_path}' '{genome_name}' -m '{motif_path}' > '{out_path}'\n"
        subprocess.run(command, shell=True, check=True)
        with open(out_path, "r") as out_file:
            print(out_file.read())















