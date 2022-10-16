#===============================================================================
# env.py
#===============================================================================

# Imports ======================================================================

import os
import os.path




# Constants ====================================================================

DIR = os.environ.get('PYQUASAR_DIR', os.path.dirname(__file__))
SNPS_BED_PATH = os.environ.get(
    'PYQUASAR_SNPS_BED_PATH', os.path.join(DIR, '1KG_SNPs_filt.bed')
)
