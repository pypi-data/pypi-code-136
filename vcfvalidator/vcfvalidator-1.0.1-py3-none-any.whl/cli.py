import sys
import click

sys.setrecursionlimit(1000000)

from vcfvalidator import __version__ as __VCFVALIDATOR_VERSION__
from vcfvalidator.vcfvalidator import VcfParser

@click.group()
@click.version_option(prog_name='vcfvalidator', version=__VCFVALIDATOR_VERSION__)
def main():
    """This is the vcfvalidator CLI"""
    pass


@click.command()
@click.argument('path-vcf', type=click.Path(exists=True, file_okay=True, readable=True, writable=False, resolve_path=True))
def validate_metadata(path_vcf):
    """Validate metadata of a VCF file located at PATH_VCF.
    
    PATH_VCF is the path of the *.vcf or *.vcf.gz file to validate
    """

    click.secho('File to validate: '+path_vcf, fg='green')

    parser = VcfParser(vcf_file_path=path_vcf)
    parser.parse_as_chunks("m", 1000, True)




main.add_command(validate_metadata)

if __name__ == '__main__':
    main()