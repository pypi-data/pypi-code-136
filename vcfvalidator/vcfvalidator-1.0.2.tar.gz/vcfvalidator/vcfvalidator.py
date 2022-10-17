import gzip
from pathlib import Path

from vcfvalidator.parser import VcfLineParser
from vcfvalidator.result import Result

'''
The parser class which parses the VCF attributes with respect to the paper: https://f1000research.com/articles/11-231
'''
class VcfValidator:

    def __init__(self, vcf_file_path):

        self.vcf_file_path = vcf_file_path
        self.line_parser = VcfLineParser()

    
    def _openfile(self):

        file_extension = Path(self.vcf_file_path).suffix

        if file_extension == '.gz':
            self.file_open_handler = gzip.open(self.vcf_file_path, "r")
        elif file_extension == '.vcf':
            self.file_open_handler = open(self.vcf_file_path, "r")


    def validate_metadata(self):

        self._openfile()

        with self.file_open_handler as file:

            line_no = 0
            
            for line in file:
                if not line:
                    break
                    
                line_no += 1   
                
                try:
                    line = line.decode("utf-8")
                except (UnicodeDecodeError, AttributeError):
                    pass

                self.line_parser.parse_line(line, line_no)
                    
                # stop parsing after begin of VCF body
                if (line.startswith("#CHROM")):
                    break


            result = Result(self.line_parser)
            result.show_table()
            result.write_logfile(self.vcf_file_path)