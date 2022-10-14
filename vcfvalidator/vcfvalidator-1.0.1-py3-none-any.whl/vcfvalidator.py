import gzip
import logging
import re
import click
from tabulate import tabulate
from pathlib import Path
import textwrap

'''
The parser class which parses the VCF attributes with respect to the paper: https://f1000research.com/articles/11-231
'''
class VcfParser:
    
    #VCF_METADATA = ["contig", "fileDate", "bioinformatics_source", "reference_url", "reference_ac", "fileformat", "SAMPLE", "INFO"]
    VCF_METADATA = ["contig", "fileDate", "bioinformatics_source", "reference_url", "reference_ac", "fileformat", "SAMPLE"]
    VCF_HEADER = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT"]
    
    VCF_REGEX_METADATA = {
    "INFO": "#+INFO=<[a-zA-Z={\D\s\d},]+>",
    "filter": "#+FILTER=<[a-zA-Z={\D\s\d},]+>",
    "format": "#+FORMAT=<[a-zA-Z={\D\s\d},]+>",
    "contig": "#+contig=<[a-zA-Z={\D\s\d},]+>",
    "fileformat": "^#+fileformat=VCFv[0-9.]+",
    "fileDate": "^#+fileDate=(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])",
    "bioinformatics_source": "#+bioinformatics_source=\"([a-zA-z0-9.\d\D\/])+\"" ,
    "reference_url": "#+reference_url=\"([a-zA-z0-9.\d\D\/])+\"",
    "reference_ac": "#+reference_ac=[a-zA-Z\S\d]+",
    "SAMPLE":"^(#+SAMPLE=<[a-zA-Z={\D\s\d},]+>)$"}
    
    VCF_REGEX_HEADER = {"CHROM": "#CHROM\\t\D"}

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
    
    def __init__(self, vcf_file_path):
        self.vcf_file_path = vcf_file_path

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        logfilename = Path(self.vcf_file_path).stem+'_VALIDATED.log'
        file_handler = logging.FileHandler(logfilename, mode='w')

        logging.basicConfig(
            level=logging.INFO,
            #format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
            format='%(message)s',
            datefmt='%H:%M:%S',
            handlers=[file_handler] # , stream_handler
        )

        '''
        logging.basicConfig(
            filename="logs.log",
            filemode="w",
            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO,
            force=True
        )
        '''
        
        logging.captureWarnings(True)
    
    
    
    '''
    The methond parse_as_chunks requires checking argument (metadata 'm', header data 'h'), chunk_size, 
    and flag to limit the reading till header data only (True for limiting, False for reading complete file) 
    '''
    def parse_as_chunks (self, arg, chunk_size, limit_to_header):
        
        filename = self.vcf_file_path

        file_extension = Path(self.vcf_file_path).suffix

        if file_extension == '.gz':
            file_open_handler = gzip.open(filename, "r")
        elif file_extension == '.vcf':
            file_open_handler = open(filename, "r")


        with file_open_handler as file:
            if arg == "m":
                self.parsing_file(self.VCF_METADATA, self.VCF_REGEX_METADATA, file, arg, chunk_size, limit_to_header)       
            elif arg == "h":
                self.parsing_file(self.VCF_HEADER, self.VCF_REGEX_HEADER, file, arg, chunk_size, limit_to_header)
    

        
    def parsing_file(self, attributes, regex_dict, file, arg, chunk_size, limit_to_header = True):
        chunk = 1
        line_no = 0
        row_no = 0

        line_numbers_with_unexpected_whitespaces = []
        
        #print ("Reading chunk no: ", chunk)
        for row in file:
            if not row:
                break
                
            if row_no < chunk_size:
                line_no = line_no + 1   
                row_no = row_no + 1
                
                try:
                    line = row.decode("utf-8")
                except (UnicodeDecodeError, AttributeError):
                    line = row

                
              
                for key, value in regex_dict.items():
                    if (arg == "m" and re.match(value, line) and key in attributes):
                        if key == 'fileformat':
                            p = re.compile("##fileformat=VCFv(.*)")
                            result = p.search(line)
                            print()
                            click.echo(click.style("VCF Version: "+result.group(1), fg='yellow', bold=True))
                            print()
                        
                        attributes.remove(key)
                    
                    elif (arg == "h" and re.match(value, line)):
                        header_attributes = line.split("\t")
                        for attribute in header_attributes[0:10]:
                            con_attribute = attribute.replace("#", "")
                            if (con_attribute in attributes):
                                attributes.remove(con_attribute)
                    
                   
                has_whitespaces = self.check_with_whitespaces(line_no, line)
                if has_whitespaces:
                    line_numbers_with_unexpected_whitespaces.append(line_no)

                if (line.startswith("#CHROM") and limit_to_header == True):
                    break
                        
            else:
                chunk = chunk + 1
                row_no = 1
                continue

        if len(attributes) == 0:
            click.echo(click.style("Congratulation! No validation errors have been found.", fg='green', bold=True))
            return False

        click.echo(click.style("VALIDATION ERRORS: The following metadata fields could not be found in the VCF file:", fg='yellow', bold=True))

        table_header = ['VCF metadata field', 'Description', 'Example']
        table = []
        for attribute in attributes:
            table.append([self.METADATA_HELP[attribute]['raw'], self.METADATA_HELP[attribute]['description'], self.METADATA_HELP[attribute]['example'] ])


        table_output = tabulate(table, table_header, tablefmt="fancy_grid", maxcolwidths=[50, 80, 80])
        print(table_output)

        result_filename = Path(self.vcf_file_path).stem+'_VALIDATED.log'
        with open(result_filename, "w") as text_file:
            text_file.write('\nVALIDATION ERRORS: The following metadata fields could not be found in the VCF file:\n\n')
            text_file.write(table_output)

            if len(line_numbers_with_unexpected_whitespaces) > 0:
                _joined = ', '.join([str(_line_no) for _line_no in line_numbers_with_unexpected_whitespaces])
                _lines = textwrap.wrap(_joined, 150)
                output_whitespaces = '\nThe following lines have unexpected whitespaces:\n'+'\n'.join(_lines)
                text_file.write(output_whitespaces)
                click.echo(click.style(output_whitespaces, fg='yellow'))



    '''
    The method check_with_whitespaces checks if the data line contains whitespaces or not
    '''
    def check_with_whitespaces(self, line_no, line):
        match = re.match("[\\\h]+", line) #checks for whitespaces
        if match:
            #logging.info ("  Line : " + str(line_no)  + " have whitespaces")
            return True
        
        return False
            
            
            