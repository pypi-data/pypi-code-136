# Author: Jakub Nawała <jnawala@agh.edu.pl>
# Created: June 1, 2021

import sys

# import functions from __main__ only if '-m' flag is not presented to avoid double imports
if '-m' not in sys.argv:
    from .__main__ import get_colourfulness_iqi, get_blur_amount_iqi, parse_user_input, process_single_mm_file, process_folder_w_mm_files

__version__ = "1.2.2"
