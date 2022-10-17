import os


def get_prog_dir(conda_opt_dir, prefix):
    for dirname in os.listdir(conda_opt_dir):
        if prefix in dirname:
            return os.path.join(conda_opt_dir, dirname)


CONDA_OPT_DIR = '/opt/conda/opt'

# busco
BUSCO_DOWNLOAD_DIR = os.getenv("BUSCO_DOWNLOAD_DIR")
BUSCO_PATH = 'busco'

# edta
EDTA_PERL_SCRIPT = 'EDTA.pl'

# trinity
TRINITY_PATH = 'Trinity'

# pasa
PASAHOME = get_prog_dir(CONDA_OPT_DIR, 'pasa')
SAMTOOLS_PATH = 'samtools'

# hisat2
HISAT2_PATH = 'hisat2'
HISAT2_BUILD_PATH = 'hisat2-build'

# stringtie
STRINGTIE_PATH = 'stringtie'
GTF_TO_ALIGNMENT_GFF3_PERL_SCRIPT = 'gtf_to_alignment_gff3.pl'

# hugep2g
HUGEP2G_PATH = 'HugeP2G'

# braker
BRAKER_PERL_SCRIPT = 'braker.pl'

# evm
EVM_HOME = get_prog_dir(CONDA_OPT_DIR, 'evidencemodeler')

# orthofinder
ORTHOFINDER_PATH = 'orthofinder'

# diamond
DIAMOND_PATH = 'diamond'

# interproscan
INTERPROSCAN_PATH = '/opt/interproscan/interproscan.sh'
