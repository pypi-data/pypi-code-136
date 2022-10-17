import click

from vcfvalidator import __version__ as __VCFVALIDATOR_VERSION__
from vcfvalidator.vcfvalidator import VcfValidator

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

    click.secho('VCF file to validate: '+path_vcf, fg='green')

    validator = VcfValidator(vcf_file_path=path_vcf)
    validator.validate_metadata()




main.add_command(validate_metadata)

if __name__ == '__main__':
    main()