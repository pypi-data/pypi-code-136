import warnings
from feapder.utils.log import log
warnings.warn('logfile argument deprecated', DeprecationWarning)
log.warning('logfile argument deprecated')