import os
import subprocess

from pypers.core.interfaces import db
from pypers.core.interfaces.storage.backup import Backup
from pypers.utils.utils import clean_folder, delete_files
from pypers.steps.base.step_generic import EmptyStep


class Index(EmptyStep):
    """
    Index / Backup / DyDb publish
    """
    spec = {
        "version": "2.0",
        "descr": [
            "Returns the directory with the extraction"
        ],
        "args":
        {
            'inputs': [
                {
                    'name': 'idx_files',
                    'descr': 'files to be indexed',
                    'iterable': True
                },
                {
                    'name': 'extraction_dir',
                    'descr': 'files to be indexed',
                    'iterable': True
                },

            ],
            'outputs': [
                {
                    'name': 'flag',
                    'descr': 'flag for done'
                }
            ]
        }
    }

    # "files" : {
    #     "st13" : {
    #         "idx" : "000/st13/idx.json",
    #         "latest" : "000/st13/latest.json"
    #     },
    #     ...
    # }
    def process(self):
        if not len(self.idx_files):
            return
        self.collection_name = self.collection.replace('harmonize_', '')

        # rewrite paths to absolute paths
        st13s = {os.path.basename(os.path.dirname(record)): record for record in self.idx_files}

        # index the files
        failed_log = os.path.join(self.output_dir, 'failed.index')
        jar_file = os.environ.get('INDEXER_JAR').strip()

        # write fofn file
        fofn_file = os.path.join(self.output_dir, 'findex.fofn')

        with open(fofn_file, 'w') as f:
            f.write('\n'.join(self.idx_files))
        cmd = 'java -jar %s --fofn %s --logFile %s --collection %s --type %s --extension .json'
        cmd = cmd % (jar_file,
                     fofn_file,
                     failed_log,
                     self.collection_name,
                     self.pipeline_type)

        proc = subprocess.Popen(cmd.split(' '),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                close_fds=True)
        stdout, stderr = proc.communicate()

        rc = proc.returncode
        if rc != 0:
            self.logger.error(str(stderr))
            db.get_db_error().send_error(self.run_id,
                                         self.collection_name,
                                         {'source': 'indexer'},
                                         str(stderr))
            return

        if os.path.exists(failed_log):
            with open(failed_log, 'r') as f:
                for line in f.readlines():
                    st13 = os.path.basename(os.path.dirname(line))
                    self.logger.info("Failed indexing on %s" % st13)
                    st13s.pop(st13)

        if self.release != 1:
            self._del_files(st13s)
        else:
            # backup what has been indexed of idx files
            self._backup_files(st13s)
        clean_folder(self.extraction_dir)

    def postprocess(self):
        failed_log = os.path.join(self.output_dir, 'failed.index')
        if os.path.exists(failed_log):
            os.remove(failed_log)
        self.flag = [1]

    # -------------
    # FILES BACKUP
    # -------------
    def _backup_files(self, st13s):
        backup = Backup(self.pipeline_type, self.collection_name)

        for st13, path in st13s.items():
            backup.store_doc_idx(path, st13, hard=True)

    def _del_files(self, st13s):
        for st13, path in st13s.items():
            os.remove(path)