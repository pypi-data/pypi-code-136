import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# NCBI metafiles
NCBI_TAXONOMY_DB = "ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz"

NCBI_GENOME_METAFILE_DICT = {
    "refseq_summary": "ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt",
    "genbank_summary": "ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt",
    "genome_size_summary": "ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/species_genome_size.txt.gz",
}

