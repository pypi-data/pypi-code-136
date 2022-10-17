import re
import click


METADATA_FIELDS = {
    'fileformat': {
        'multiple': False,
        'startswith': '##fileformat=',
        'regexp': '^#+fileformat=VCFv[0-9.]+',
        'parser_func_name': '_parse_fileformat_line'
    },
    'fileDate': {
        'multiple': False,
        'startswith': '##fileDate=',
        'regexp': '^#+fileDate=(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])',
        'parser_func_name': '_parse_filedate_line'
    },
    'bioinformatics_source': {
        'multiple': False,
        'startswith': '##bioinformatics_source=',
        'regexp': '#+bioinformatics_source=\"([a-zA-z0-9.\d\D\/])+\"',
        'parser_func_name': '_parse_bioinformatics_source_line'
    },
    'reference_url': {
        'multiple': False,
        'startswith': '##reference_url=',
        'regexp': '#+reference_url=\"([a-zA-z0-9.\d\D\/])+\"',
        'parser_func_name': '_parse_reference_url_line'
    },
    'reference_ac': {
        'multiple': False,
        'startswith': '##reference_ac=',
        'regexp': '#+reference_ac=[a-zA-Z\S\d]+',
        'parser_func_name': '_parse_reference_ac_line'
    },
    'contig': {
        'multiple': True,
        'startswith': '##contig=',
        'regexp': '#+contig=<[a-zA-Z={\D\s\d},]+>',
        'parser_func_name': '_parse_contig_line'
    },
    'SAMPLE': {
        'multiple': True,
        'startswith': '##SAMPLE=',
        'regexp': '^#+SAMPLE=<([a-zA-Z={\D\s\d},]+)>$',
        'parser_func_name': '_parse_sample_line'
    },
    'BODY_HEADER': {
        'multiple': False,
        'startswith': '#CHROM',
        'regexp': None,
        'parser_func_name': '_parse_body_header_line',
        'standard_values': ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'],
    }
}


class VcfLineParser:

    whitespaces_pattern = re.compile ( r"^([^\S\r\n].+|.+[^\S\r\n])$" )

    vcf_spec_version = ''
    found_metadata_fields = {}
    found_sample_ids_in_metadata = []
    found_sample_ids_in_body_header = []
    line_numbers_with_unexpected_whitespaces = []


    def parse_line(self, line, line_number):

        if self._check_for_unexpected_whitespaces(line):
            self.line_numbers_with_unexpected_whitespaces.append(line_number)

        #if line.startswith(' '):
        #    print(line)

        line = line.strip()

        for _field in METADATA_FIELDS:

            if line.startswith(METADATA_FIELDS[_field]['startswith']):
                _line_processor = getattr(self, METADATA_FIELDS[_field]['parser_func_name'])
                _line_processor(line)

                if _field != 'BODY_HEADER':
                    self.found_metadata_fields[_field] = self.found_metadata_fields.get(_field, 0) + 1


    def _parse_fileformat_line(self, line):
        p = re.compile("##fileformat=VCFv(.*)")
        result = p.search(line)
        print()
        click.echo(click.style("VCF Version: "+result.group(1), fg='yellow', bold=True))
        print()
        self.vcf_spec_version = result.group(1)


    def _parse_filedate_line(self, line):
        pass


    def _parse_bioinformatics_source_line(self, line):
        pass


    def _parse_reference_url_line(self, line):
        pass


    def _parse_reference_ac_line(self, line):
        pass


    def _parse_contig_line(self, line):
        pass


    def _parse_sample_line(self, line):
        p = re.compile(METADATA_FIELDS['SAMPLE']['regexp'])
        result = p.search(line)

        try:
            if result.group(1):
                matches = dict(re.findall(r'([^=]+)=([^=]+)(?:,|$)', result.group(1)))
                if matches['ID']:
                    self.found_sample_ids_in_metadata.append(matches['ID'])
        except AttributeError:
            pass


    def _parse_body_header_line(self, line):
        items = line.strip().split('\t')
        self.found_sample_ids_in_body_header = [item for item in items if item not in METADATA_FIELDS['BODY_HEADER']['standard_values']]


    def _check_for_unexpected_whitespaces(self, line):
        
        if self.whitespaces_pattern.match(line):
            return True
        
        return False