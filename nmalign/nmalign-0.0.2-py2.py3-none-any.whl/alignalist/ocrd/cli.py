from pkg_resources import resource_string
import json
import click

from ocrd.decorators import ocrd_cli_options, ocrd_cli_wrap_processor
from ocrd import Processor
from ocrd_utils import (
    getLogger,
    make_file_id,
    assert_file_grp_cardinality,
    MIMETYPE_PAGE,
    MIME_TO_PIL,
    MIME_TO_EXT
)
from ocrd_modelfactory import page_from_file
from ocrd_models.ocrd_page import (
    AlternativeImageType,
    to_xml
)

from .. import lib

OCRD_TOOL = json.loads(resource_string(__name__, 'ocrd-tool.json').decode('utf8'))
TOOL = 'ocrd-alignalist'

class AlignLines(Processor):

    def __init__(self, *args, **kwargs):
        kwargs['ocrd_tool'] = OCRD_TOOL['tools'][TOOL]
        kwargs['version'] = OCRD_TOOL['version']
        super().__init__(*args, **kwargs)
    
    def process(self):
        """map...

        Produce a new PAGE output file by serialising the resulting hierarchy.
        """
        LOG = getLogger('processor.AlignLines')
        assert_file_grp_cardinality(self.input_file_grp, 2)
        assert_file_grp_cardinality(self.output_file_grp, 1)
        
        for (n, input_file) in enumerate(self.input_files):
            file_id = make_file_id(input_file, self.output_file_grp)
            page_id = input_file.pageId or input_file.ID
            LOG.info("INPUT FILE %i / %s", n, page_id)
            pcgts = page_from_file(self.workspace.download_file(input_file))
            self.add_metadata(pcgts)
            page = pcgts.get_Page()

            pcgts.set_pcGtsId(file_id)
            self.workspace.add_file(
                ID=file_id,
                file_grp=self.output_file_grp,
                pageId=input_file.pageId,
                mimetype=MIMETYPE_PAGE,
                local_filename=os.path.join(self.output_file_grp,
                                            file_id + '.xml'),
                content=to_xml(pcgts))

@click.command()
@ocrd_cli_options
def ocrd_alignalist(*args, **kwargs):
    return ocrd_cli_wrap_processor(AlignLines, *args, **kwargs)
