from pypers.steps.base.step_generic import EmptyStep
from .data_handler import GBDFormat
from .img_handler import GBDImage
from .dyncopy_handler import DynCopy
from .dynlive_handler import DynLive
from .analyze_handler import Analyze
from .idx_handler import IdxTransform

from pypers.core.interfaces.storage.backup import Backup
import json
import os


class ETLProcess(EmptyStep):
    """
    Process manifets file files into subdirectories.
    Rename files and logos to appnum
    """
    spec = {
        "version": "2.0",
        "descr": [
            "Returns the directory with the extraction"
        ],
        "args":
        {
            "inputs": [
                {
                    "name": "manifest",
                    "descr": "the manifest list",
                    "iterable": True
                }
            ],
            "outputs": [
                {
                    "name": "idx_files",
                    "descr": "the extracted data organized by appnum"
                },
                {
                    "name": "extraction_dir",
                    "descr": "the extracted dir"
                }
            ]
        }
    }

    # self.manifest ORIFILES_DIR/run_id/type/collection/office_extraction_date/archive_name/manifest.json
    def process(self):
        collection = self.collection.replace('harmonize_', '')
        self.extraction_dir = os.path.dirname(self.manifest)
        self.backup_processor = Backup(self.pipeline_type, collection)

        params = {
            'collection': collection,
            'pipeline_type':self.pipeline_type,
            'extraction_dir': self.extraction_dir,
            'run_id': self.run_id,
            'output_dir': self.output_dir,
            'logger': self.logger,
            'backup_handler': self.backup_processor
        }

        self.processors = [GBDFormat(**params), GBDImage(**params), DynCopy(**params), DynLive(**params), Analyze(**params),
                           IdxTransform(**params)]

        with open(self.manifest, 'r') as f:
            manifest_data = json.load(f)
        data_files = self._filter_missing_files(manifest_data.get('files', {}))
        appnum_files_flat = [(data, appnum) for appnum, data in data_files.items()]
        idx_paths = []
        for entry in self.worker_parallel(appnum_files_flat, self._process_record):
            if entry:
                idx_paths.append(entry)
        self.idx_files = [idx_paths]
        self.extraction_dir = [self.extraction_dir]

    def _process_record(self, item):
        data_file, appnum = item
        try:
            for processor in self.processors:
                getattr(processor, 'process')(data_file, appnum)
            res = data_file.get('doc', {}).get('idx', None)
        except:
            self.logger.error('Failed to process %s' % appnum)
            res = None
        if res:
            try:
                if 'data' in data_file.keys():
                    os.remove(os.path.join(self.extraction_dir, data_file['data']['ori']))
                if 'imgs' in data_file.keys():
                    for logo in data_file['imgs']:
                        if not logo.get('ori', None):
                            continue
                        os.remove(os.path.join(self.extraction_dir, logo['ori']))
            except:
                # Just cleanup, not throing any errors.
                pass
        return res

    def _file_exists(self, file):
        file_path = os.path.join(self.extraction_dir, file)
        return os.path.exists(file_path)

    def _filter_missing_files(self, unfiltered):
        filtered = {}
        for key, item in unfiltered.items():
            item_present = True
            if 'data' in item.keys():
                item_present = item_present and self._file_exists(item['data']['ori'])
            if 'imgs' in item.keys():
                for logo in item['imgs']:
                    if not logo.get('ori', None):
                        continue
                    item_present = item_present and self._file_exists(logo['ori'])
            if item_present:
                filtered[key] = item
        return filtered




