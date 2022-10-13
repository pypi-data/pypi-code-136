import os
import shutil
import traceback
import sys
import lcbuilder.eleanor
sys.modules['eleanor'] = sys.modules['lcbuilder.eleanor']
import eleanor
from eleanor.maxsector import maxsector


class EleanorManager:
    @staticmethod
    def update():
        eleanor_path = os.path.join(os.path.expanduser('~'), '.eleanor')
        eleanor.update_max_sector()
        for sector in range(1, maxsector + 1):
            sectorpath = eleanor_path + '/metadata/s{:04d}'.format(sector)
            if os.path.exists(sectorpath) and os.path.isdir(sectorpath) and not os.listdir(sectorpath):
                os.rmdir(sectorpath)
            if (not os.path.exists(sectorpath) or not os.path.isdir(sectorpath) or not os.listdir(sectorpath)) \
                    and sector <= maxsector:
                try:
                    eleanor.Update(sector)
                except Exception as e:
                    traceback.print_exc()
                    shutil.rmtree(sectorpath)
                    break