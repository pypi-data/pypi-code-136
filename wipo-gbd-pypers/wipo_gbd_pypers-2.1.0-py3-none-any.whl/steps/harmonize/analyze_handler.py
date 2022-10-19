import os
import json
import subprocess
from pypers.core.interfaces import db
from . import BaseHandler

class Analyze(BaseHandler):
    skip_analyze_verbal_images = 'emtm, frtm, krtm, vntm'

    def process(self, data_file, appnum):
        if not len(data_file.get('doc', None)):
            return
        self.img_files = []

        record = data_file.get('doc', {})
        st13 = data_file.get('st13', None)

        # dynamo db / gbd_pypers_indexer
        img_files_for_analysis = []

        # no images => move on
        if not len(record.get('img_files', [])):
            return

        # read feature from record
        feature = record.get('feature')

        # read image_analysis from latest
        latest_data = record['data_files']['latest']
        latest_img_analysis = latest_data.get('image_analysis', [])

        for img_info in record['img_files']:
            img_file = img_info['img']

            is_analysed = self._is_analysed(img_info['crc'],
                                            latest_img_analysis)
            is_skipped = self._skip_feature(feature)

            # will not analyse image => remove
            if is_analysed or is_skipped:
                os.remove(img_file)
                continue

            img_files_for_analysis.append(img_file)


        # no images to (re)analyse
        if not len(img_files_for_analysis):
            return

        # IMAGEANALYSIS STARTS HERE
        # -------------------------
        self.logger.debug('[ANALYZE][START] // %s image files to analyze' % len(img_files_for_analysis))
        # write fofn file
        fofn_file = os.path.join(self.extraction_dir, st13, 'images.fofn')
        os.makedirs(os.path.dirname(fofn_file), exist_ok=True)
        with open(fofn_file, 'w') as f:
            f.write('\n'.join(img_files_for_analysis))

        self._run_analyze_command(fofn_file)

        # loop records to find images with analysis files present
        lire_data = []

        for img_info in record['img_files']:
            img_path = os.path.dirname(img_info['img'])
            img_name = os.path.basename(img_info['img'])

            img_analysis_file = os.path.join(img_path,
                                             img_name.replace('.png', '.json'))
            with open(img_analysis_file, 'r') as f:
                lire_data_img = json.loads(f.read())
            # a newly analysed image !
            lire_data.append(lire_data_img)
            # done with image file
            os.remove(img_analysis_file)
            os.remove(img_info['img'])
        record['data_files']['latest']['image_analysis'] = lire_data
        os.remove(fofn_file)

    def _is_analysed(self, crc, latest_img_analysis):
        for img in latest_img_analysis:
            if img.get('crc') == crc:
                return True
        return False

    def _skip_feature(self, feature):
        return feature is 'Word' and self.collection in self.skip_analyze_verbal_images

    def _run_analyze_command(self, fofn_file):
        jar_file = os.environ.get('IMAGEANALYSIS_JAR').strip()
        conf_url = os.environ.get('IMAGEANALYSIS_CONF_URL', '').strip()
        atac_url = os.environ.get('IMAGEANALYSIS_CLASSIF_ENDPOINT', '').strip()
        cmd = "java -jar %s --configuration %s --type %s --atac %s --fofn %s --threads 5 --outputContent index"
        cmd = cmd % (jar_file,
                     conf_url,
                     self.pipeline_type,
                     atac_url,
                     fofn_file)
        proc = subprocess.Popen(cmd.split(' '),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                close_fds=True)
        stdout, stderr = proc.communicate()

        rc = proc.returncode

        if rc != 0:
            self.logger.error(str(stderr))
            db.get_db_error().send_error(self.run_id,
                                         self.collection,
                                         {'source': 'image_analysis'},
                                         str(stderr))
