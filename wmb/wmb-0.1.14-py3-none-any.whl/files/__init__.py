from ._aibs import *
from ._brain_region import *
from ._broad import *
from ._cemba import *
from ._cemba_epi_retro import *
from ._integration import *
from ._ref import *
from .palette import PALETTES

LOCAL_PREFIX = '/gale/netapp/cemba3c/BICCN'
REMOTE_PREFIX = '/cemba'


class AutoPathMixIn:
    @staticmethod
    def _is_remote():
        if pathlib.Path(LOCAL_PREFIX).exists():
            return False
        else:
            if pathlib.Path(REMOTE_PREFIX).exists():
                return True
            else:
                return False

    def _check_file_path_attrs(self, check=False):
        is_remote = self._is_remote()

        for attr in dir(self):
            if not attr.startswith('__') and attr.endswith('_PATH'):
                cur_path = self.__getattribute__(attr)
                if is_remote:
                    cur_path = pathlib.Path(str(cur_path).replace(LOCAL_PREFIX, REMOTE_PREFIX))
                    self.__setattr__(attr, cur_path)

                if check:
                    if not pathlib.Path(cur_path).exists():
                        print(f"{attr} do not exist: {cur_path}")
        return
