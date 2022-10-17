import os
from pathlib import Path
import click
from rich.console import Console
from tabulate import tabulate
import textwrap

METADATA_HELP = {
    'fileformat': {
        'raw': '##fileformat=vcf_specification_version',
        'description': 'The version of the VCF specifications.',
        'example': '##fileformat=VCFv4.3'
    },
    'fileDate': {
        'raw': '##fileDate=date',
        'description': 'The creation date of the VCF should be specified in the metadata via the field ##fileDate, the notation corresponds to ISO 8601 (Kuhn, 1995) (in the basic form without separator: YYYYMMDD).',
        'example': '##fileDate=20120921'
    },
    'bioinformatics_source': {
        'raw': '##bioinformatics_source=url',
        'description': 'The analytic approach (usually consisting of chains of bioinformatics tools) for creating the VCF file is specified in the ##bioinformatics_source field. Such approaches often involve several steps, like read mapping, variant calling and imputation, each carried out using a different program. Every component of this process should be clearly described, including all the parameter values.',
        'example': '##bioinformatics_source="doi.org/10.1038/s41588-018-0266-x"'
    },
    'reference_ac': {
        'raw': '##reference_ac=assembly_accession',
        'description': 'This field contains the accession number (including the version) of the reference sequence on which the variation data of the present VCF is based. The NCBI page on the Genome Assembly Model states (NCBI, 2002): “The assembly accession starts with a three letter prefix, GCA for GenBank assemblies […]. This is followed by an underscore and 9 digits. A version is then added to the accession. For example, the assembly accession for the GenBank version of the public human reference assembly (GRCh38.p11) is GCA_000001405.26”. Note these accessions are shared by all INSDC archives.',
        'example': '##reference_ac=GCA_902498975.1'
    },
    'reference_url': {
        'raw': '##reference_url=url',
        'description': 'While the ##reference_ac field contains the accession number of the reference genome assembly, the ##reference_url field contains a URL (or URI/DOI) for downloading of this reference genome assembly, preferably from one INSDC archive. The reference genome assembly should be in FASTA format; the user is free to provide a packed or unpacked publicly available version of the genome assembly.',
        'example': '##reference_url=“ftp.ncbi.nlm.nih.gov/genomes/all/GCA/902/498/975/GCA_902498975.1_Morex_v2.0/GCA_902498975.1_Morex_v2.0_genomic.fna.gz”'
    },
    'contig': {
        'raw': '##contig=<ID=ctg1, length=sequence_length, assembly=gca_accession, md5=md5_hash, species=NCBI Taxon ID>',
        'description': 'The individual sequence(s) of the reference genome assembly are described in more detail in the #contig field(s). Each contig entry contains at least the attribute ID, and typically also include length, assembly, md5 and species. The ID is the identifier of the sequence contig used in the reference genome assembly. Length contains the base pair length of the sequence contig in the reference genome assembly. The assembly is the accession number of the reference genome. If the md5 parameter is given, please note that the individual sequence contigs MD5 checksum is expected, not the MD5 sum of the complete reference genome assembly. The species is the taxonomic name of the species of the reference genome assembly.',
        'example': '##contig=<ID=chr1H,length=522466905,assembly=GCA_902498975.1,md5=8d21a35cc68340ecf40e2a8dec9428fa,species=NCBITaxon:4513>'
    },
    'SAMPLE': {
        'raw': '##SAMPLE=<ID=BioSample_accession, DOI=doi, ext_ID=registry:identifier>',
        'description': 'The ##SAMPLE fields describe the material whose variants are given in the genotype call columns in greater detail and can be extended using the specifications of the VCF format. Genotyped samples are indicated in the VCF by the BioSample accession, which is formed as follows (based on information from the BioSamples documentation): “BioSample accessions always begin with SAM. The next letter is either E or N or D depending if the sample information was originally submitted to EMBL-EBI or NCBI or DDBJ, respectively. After that, there may be an A or a G to denote an Assay sample or a Group of samples. Finally, there is a numeric component that may or may not be zero-padded.” Additional information (like complete Multi-Crop Passport Descriptor (Alercia et al., 2015) records) on the sample material is provided under the DOI (Alercia et al., 2018). If there are additional IDs like project or database IDs, they can be provided alongside the DOI as “ext_ID”. They are strongly recommended if no DOI is available. If the material is held by a FAO-WIEWS recognised institution, the external ID consists of the FAO-WIEWS instcode, the genus and the accession number (see example 2). If the database is not registered with FAO-WIEWS, the DNS of the holding institution or laboratory, the database identifier, the identifier scheme and the identifier value should be provided (see example 3). For multiple external IDs the field should be used multiple times (delimited by commas). By default, the registry in the “ext_ID” field should follow the specification in Identifier.org according to MIRIAM (Juty et al., 2012).',
        'example': '##SAMPLE=<ID=SAMEA104646767,DOI="doi.org/10.25642/IPK/GBIS/7811152">'
    },
}

class Result:

    def __init__(self, line_parser_instance):

        self.line_parser_instance = line_parser_instance
        
        self.found_sample_ids_in_metadata = line_parser_instance.found_sample_ids_in_metadata
        self.found_sample_ids_in_body_header = line_parser_instance.found_sample_ids_in_body_header
        self.line_numbers_with_unexpected_whitespaces = line_parser_instance.line_numbers_with_unexpected_whitespaces

        self.missing_metadata_fields = []
        pass


    def _prepare_and_check_results(self):

        for _field in METADATA_HELP.keys():
            if _field not in self.line_parser_instance.found_metadata_fields:
                self.missing_metadata_fields.append(_field)
        
        if len(self.missing_metadata_fields) > 0:
            table_header = ['VCF metadata field', 'Description', 'Example']
            table = []
            for _field in self.missing_metadata_fields:
                table.append([METADATA_HELP[_field]['raw'], METADATA_HELP[_field]['description'], METADATA_HELP[_field]['example'] ])

            self.table_output = tabulate(table, table_header, tablefmt="fancy_grid", maxcolwidths=[50, 80, 80])



    def _check_sample_id_consistency(self):

        has_sample_id_mismatch = False
        
        if len(self.found_sample_ids_in_metadata) != len(self.found_sample_ids_in_body_header):
            has_sample_id_mismatch = True

        sample_ids_in_metadata_but_not_in_body = [item for item in self.found_sample_ids_in_metadata if item not in self.found_sample_ids_in_body_header]
        if len(sample_ids_in_metadata_but_not_in_body) > 0:
            has_sample_id_mismatch = True

        sample_ids_in_body_but_not_in_metadata = [item for item in self.found_sample_ids_in_body_header if item not in self.found_sample_ids_in_metadata]
        if len(sample_ids_in_body_but_not_in_metadata) > 0:
            has_sample_id_mismatch = True

        self._check_sample_id_consistency_result = {
            'has_sample_id_mismatch': has_sample_id_mismatch,
            'sample_ids_in_metadata_but_not_in_body': sample_ids_in_metadata_but_not_in_body,
            'sample_ids_in_body_but_not_in_metadata': sample_ids_in_body_but_not_in_metadata
        }


    def show_table(self):

        has_errors = False
        self._prepare_and_check_results()

        if len(self.missing_metadata_fields) > 0:
            has_errors = True
            click.echo(click.style("VALIDATION ERROR: The following metadata fields could not be found in the VCF file:", fg='red'))
            print(self.table_output)

        console = Console()
        with console.status("[bold green]Validating the VCF file...") as status:
            while True:
                self._check_sample_id_consistency()
                break

        if self._check_sample_id_consistency_result['has_sample_id_mismatch']:
            has_errors = True
            click.echo(click.style("\nVALIDATION ERROR: A mismatch between the sample IDs defined in the metadata and the sample IDs listed in the VCF body was found. Please look into the logfile for further information.", fg='red'))

        if len(self.line_numbers_with_unexpected_whitespaces) > 0:
            has_errors = True
            output_whitespaces = '\nVALIDATION ERROR: The VCF file has lines with unexpected whitespace characters. Please look into the logfile for further information.\n'
            click.echo(click.style(output_whitespaces, fg='red'))

        if not has_errors:
            click.echo(click.style("Congratulation! No validation errors have been found.", fg='green'))
            return False


    def write_logfile(self, original_filename):

        logfile_filename = Path(original_filename).stem+'_VALIDATED.log'

        if len(self.missing_metadata_fields) == 0:
            return False

        with open(logfile_filename, "w") as logfile:

            logfile.write('\nVALIDATION ERROR: The following metadata fields could not be found in the VCF file:\n\n')
            logfile.write(self.table_output)

            if self._check_sample_id_consistency_result['has_sample_id_mismatch']:
                logfile.write('\n\nVALIDATION ERROR: A mismatch between the sample IDs defined in the metadata and the sample IDs listed in the VCF body was found.')


            if len(self._check_sample_id_consistency_result['sample_ids_in_metadata_but_not_in_body']) > 0:
                logfile.write('\n\nThe following sample IDs have been found in the metadata but not in the VCF body:\n\n')
                _joined = ', '.join([str(_id) for _id in self._check_sample_id_consistency_result['sample_ids_in_metadata_but_not_in_body']])
                _lines = textwrap.wrap(_joined, 150)
                logfile.write('\n'.join(_lines))


            if len(self._check_sample_id_consistency_result['sample_ids_in_body_but_not_in_metadata']) > 0:
                logfile.write('\n\n\nThe following sample IDs have been found in the VCF body but not in the metadata:\n\n')
                _joined = ', '.join([str(_id) for _id in self._check_sample_id_consistency_result['sample_ids_in_body_but_not_in_metadata']])
                _lines = textwrap.wrap(_joined, 150)
                logfile.write('\n'.join(_lines))


            if len(self.line_numbers_with_unexpected_whitespaces) > 0:
                _joined = ', '.join([str(_line_no) for _line_no in self.line_numbers_with_unexpected_whitespaces])
                _lines = textwrap.wrap(_joined, 150)
                output_whitespaces = '\nVALIDATION ERROR: The following lines have unexpected whitespaces:\n'+'\n'.join(_lines)
                logfile.write('\n'+output_whitespaces)

            path_logfile = os.path.realpath(logfile.name)
            click.secho('=== VALIDATION FINISHED ===\n', fg='green')
            click.secho('A logfile with the results was written to: '+path_logfile, fg='green')
            print()