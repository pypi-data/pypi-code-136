#===============================================================================
# pyQuASAR.py
#===============================================================================

# Imports ======================================================================

import funcgenom
import gzip
import itertools
import os
import os.path
import pipes
import subprocess
import tempfile

from Bio.bgzf import BgzfWriter

from pyQuASAR.env import DIR, SNPS_BED_PATH




# Constants ====================================================================

GENOTYPE_DICT = {0: ('0/0', '0/1'), 1: ('0/1', '0/0'), 2: ('1/1', '0/0')}




# Functions ====================================================================

def write_compressed_pileup(pileup_bytes: bytes, pileup_file_path: str):
    """Write a compressed QuASAR intermediate pileup to disk
    
    Parameters
    ----------
    pileup_bytes : bytes
        Pileup file as a bytes object
    pileup_file_path : str
        File path to write data
    """
    
    with gzip.open(pileup_file_path, 'wb') as f:
        f.write(pileup_bytes)


def pileup_to_bed(
    pileup_bytes,
    snps_bed_path: str = SNPS_BED_PATH,
    temp_file_dir=None
) -> str:
    """Convert a pileup to a BED file in memory
    
    Parameters
    ----------
    pileup_bytes : bytes
        Pileup file as a bytes object
    snps_bed_path : str
        Path to BED file containing SNPs
    temp_file_dir
        directory for temporary files
    
    Returns
    -------
    str
        BED file
    """
    
    with tempfile.NamedTemporaryFile(dir=temp_file_dir) as temp_file:
        temp_file_name = temp_file.name
    
    t = pipes.Template()
    for cmd, kind in (
        ('less', '--'),
        (
            (
                r"awk -v OFS='\t' "
                "'{ "
                "if ("
                "$4>0 "
                "&& $5 !~ /[^\^][<>]/ "
                "&& $5 !~ /\+[0-9]+[ACGTNacgtn]+/ "
                "&& $5 !~ /-[0-9]+[ACGTNacgtn]+/ "
                "&& $5 !~ /[^\^]\*/"
                ") "
                "print $1,$2-1,$2,$3,$4,$5,$6"
                "}'"
            ),
            '--'
        ),
        ('sortBed -i stdin', '--'),
        (f'intersectBed -a stdin -b {snps_bed_path} -wo', '--'),
        ('cut -f 1-7,11-14', '--'),
    ):
        t.append(cmd, kind)
    f = t.open(temp_file_name, 'w')
    f.write(pileup_bytes.decode())
    f.close()
    return open(temp_file_name).read()


def write_compressed_pileup_bed(
    pileup_bytes,
    pileup_bed_path,
    snps_bed_path=None,
    temp_file_dir=None
):
    """Write a compressed QuASAR intermediate pileup.bed file to disk
    
    Parameters
    ----------
    pileup_bytes : bytes
        Pileup file as a bytes object
    pileup_bed_path : str
        File path to write data
    snps_bed_path : str
        Path to BED file containing SNPs
    temp_file_dir
        directory for temporary files
    """
    
    with gzip.open(pileup_bed_path, 'wt') as f:
        f.write(
            pileup_to_bed(
                pileup_bytes,
                snps_bed_path=snps_bed_path,
                temp_file_dir=temp_file_dir
            )
        )


def bed_to_quasar(bed_path):
    """Convert the pileup.bed file to quasar input format
    
    Write the new file to disk next to the input file.
    
    Parameters
    ----------
    bed_path
       Path to a pileup.bed.gz file
    """
    
    working_dir = os.getcwd()
    os.chdir(os.path.dirname(bed_path))
    subprocess.call(
        (
            'Rscript', '--vanilla',
            f'{DIR}/QuASAR/scripts/convertPileupToQuasar.R',
            os.path.basename(bed_path)
        ),
        stdout=subprocess.DEVNULL
    )
    os.chdir(working_dir)


def genotype(*input_file_paths):
    """Run quasar on formatted input files to obtain genotypes
    
    Parameters
    ----------
    input_file_paths
        paths to input files
    
    Returns
    -------
    bytes
        Standard output from QuASAR
    """
    
    with subprocess.Popen(
        (
            (
                'Rscript',
                os.path.join(os.path.dirname(__file__), 'QuASAR_genotype.R')
            )
            + tuple(input_file_paths)
        ),
        stdout=subprocess.PIPE
    ) as quasar_genotype:
        return quasar_genotype.communicate()[0]


def generate_allele_dict_items(snps_bed_path: str):
    """Generate tuples defining an allele dict
    
    Parameters
    ----------
    snps_bed_path : str
        Path to BED file containing SNPs
    
    Yields
    ------
    tuple
        Variant ID and a pair of alleles
    """
    
    with open(snps_bed_path, 'r') as f:
        for line in f:
            chr, _, pos, id, ref, alt, maf = line.split()
            yield id, (ref, alt)


def genotype_to_vcf(
    genotype_bytes: bytes,
    sample_name: str = 'SAMPLE',
    snps_bed_path: str = SNPS_BED_PATH,
    threshold: float = 0.99,
    het_only: bool = False,
    temp_file_dir=None
):
    """Convert genotype probabilities from QuASAR to VCF format
    
    Parameters
    ----------
    genotype_bytes : bytes
        Standard output from QuASAR as a bytes object
    sample_name : str
        Sample name for the VCF file
    snps_bed_path : str
        Path to BED file containing SNPs
    threshold : float
        Genotype probability threshold for variants to include
    het_only : bool
        Include only heterozygous variants if true
    temp_file_dir
        directory for temporary files
    
    Yields
    ------
    str
        A line of a VCF file
    """
    
    yield from (
        '##fileformat=VCFv4.0',
        '##reference=GRCh37',
        '##INFO=<ID=BUILD,Number=1,Type=Integer,Description="Genome build">',
        (
            '##INFO='
            '<ID=GP,Number=3,Type=Float,Description="Genotype probabilities">'
        ),
        '##FORMAT=<ID=GT,Number=1,Type=String,Description=Genotype>',
        '\t'.join(
            (
                '#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO',
                'FORMAT', sample_name, '{}_COMP'.format(sample_name)
            )
        )
    )
    allele_dict = dict(generate_allele_dict_items(snps_bed_path))
    with tempfile.NamedTemporaryFile(dir=temp_file_dir) as temp_variants:
        temp_variants.write(genotype_bytes)
        with funcgenom.Genome() as genome:
            genome.load_variants(
                temp_variants.name,
                add_header=('chr', '_', 'pos', 'id', 'g0', 'g1', 'g2')
            )
            genome.sort_variants()
            for variant in genome.variants():
                g0, g1, g2 = (float(g) for g in variant.tuple[-3:])
                if (
                    any(g > threshold for g in (g0, g1, g2))
                    and
                    ((not het_only) or (g1 > threshold))
                ):
                    ref, alt = allele_dict[variant.id]
                    genotype, complementary_genotype = GENOTYPE_DICT[
                        (g0, g1, g2).index(max(g0, g1, g2))
                    ]
                    yield '\t'.join(
                        (
                            variant.chromosome,
                            str(variant.position),
                            variant.id,
                            ref,
                            alt,
                            '.',
                            'PASS',
                            'BUILD=37;GP={},{},{}'.format(g0, g1, g2),
                            'GT',
                            genotype,
                            complementary_genotype
                        )
                    )


def write_split_vcf(vcf, prefix: str):
    """Write VCF data split by chromosome
    
    Parameters
    ----------
    vcf
        Iterator giving lines of VCF data
    prefix : str
        Output prefix for split VCF files
    """
    
    header = []
    for key, group in itertools.groupby(vcf, key=lambda l: l[:2]):
        if key in {'##', '#C'}:
            header.extend(list(group))
        else:
            with BgzfWriter(f'{prefix}.chr{key.rstrip()}.vcf.gz', 'wb') as f:
                f.write(
                    '\n'
                    .join(itertools.chain(header, tuple(group), ('',)))
                    .encode()
                )
