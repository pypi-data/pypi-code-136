#===============================================================================
# env.py
#===============================================================================

import os
import os.path

JAR = os.environ.get(
    'PICARDTOOLS_JAR', os.path.join(os.path.dirname(__file__), 'picard.jar')
)
