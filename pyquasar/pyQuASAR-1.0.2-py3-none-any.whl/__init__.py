"""Wrap quasar for pipelines"""

from pyQuASAR.pyQuASAR import (
    write_compressed_pileup, pileup_to_bed, write_compressed_pileup_bed,
    bed_to_quasar, genotype, generate_allele_dict_items, genotype_to_vcf,
    write_split_vcf, DIR, SNPS_BED_PATH
)
