

""""""# start delvewheel patch
def _delvewheel_init_patch_1_0_1():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'treefarms.libs'))
    if sys.version_info[:2] >= (3, 8) and not os.path.exists(os.path.join(sys.base_prefix, 'conda-meta')) or sys.version_info[:2] >= (3, 10):
        os.add_dll_directory(libs_dir)
    else:
        from ctypes import WinDLL
        with open(os.path.join(libs_dir, '.load-order-treefarms-0.1.0')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_1_0_1()
del _delvewheel_init_patch_1_0_1
# end delvewheel patch

# We're just going to bring these to the front
# This is Tynan guessing what
from treefarms.model.treefarms import TREEFARMS
from treefarms.model.threshold_guess import get_thresholds