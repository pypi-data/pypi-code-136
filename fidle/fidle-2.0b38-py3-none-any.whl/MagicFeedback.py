# ------------------------------------------------------------------
#   __  __             _      ______            _ _                _    
#  |  \/  |           (_)    |  ____|          | | |              | |   
#  | \  / | __ _  __ _ _  ___| |__ ___  ___  __| | |__   __ _  ___| | __
#  | |\/| |/ _` |/ _` | |/ __|  __/ _ \/ _ \/ _` | '_ \ / _` |/ __| |/ /
#  | |  | | (_| | (_| | | (__| | |  __/  __/ (_| | |_) | (_| | (__|   < 
#  |_|  |_|\__,_|\__, |_|\___|_|  \___|\___|\__,_|_.__/ \__,_|\___|_|\_\
#                 __/ |                                                 
#                |___/                           fidle.MagicFeedback
# ------------------------------------------------------------------
# A simple class to manage feedbacks from MagicCooker
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022


from genericpath import isfile
import os
import json

import fidle.config as config

class MagicFeedback:

    __version__  = config.VERSION

    def __init__(self):
        self.data = dict( type='MagicFeedback', version=config.VERSION )

    # --------------------------------------------------------------
    # -- Feedback stuffs
    # --------------------------------------------------------------

    def add(self, **entries):
        self.data = dict(**self.data, **entries)

    def remove(self, *keys):
        for k in keys:
            if k in self.data : del self.data[k]

    def save(self, filename):
        # print(json.dumps(self.data, indent=4, sort_keys=True))
        # ---- Save
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
