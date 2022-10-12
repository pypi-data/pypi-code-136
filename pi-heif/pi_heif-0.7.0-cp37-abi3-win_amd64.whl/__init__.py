"""
Import all possible stuff that can be used.
"""


# start delvewheel patch
def _delvewheel_init_patch_1_0_1():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    if sys.version_info[:2] >= (3, 8) and not os.path.exists(os.path.join(sys.base_prefix, 'conda-meta')) or sys.version_info[:2] >= (3, 10):
        os.add_dll_directory(libs_dir)
    else:
        from ctypes import WinDLL
        with open(os.path.join(libs_dir, '.load-order-pi_heif-0.7.0')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_1_0_1()
del _delvewheel_init_patch_1_0_1
# end delvewheel patch




from ._lib_info import (
    have_decoder_for_format,
    have_encoder_for_format,
    libheif_info,
    libheif_version,
)
from ._options import options
from ._version import __version__
from .as_opener import (
    AvifImageFile,
    HeifImageFile,
    register_avif_opener,
    register_heif_opener,
)
from .constants import heif_filetype_maybe  # DEPRECATED
from .constants import heif_filetype_no  # DEPRECATED
from .constants import heif_filetype_yes_supported  # DEPRECATED
from .constants import heif_filetype_yes_unsupported  # DEPRECATED
from .constants import (
    HeifChannel,
    HeifChroma,
    HeifColorProfileType,
    HeifColorspace,
    HeifCompressionFormat,
    HeifErrorCode,
    HeifFiletype,
)
from .error import HeifError

# pylint: disable=redefined-builtin
from .heif import (
    HeifFile,
    HeifImage,
    HeifThumbnail,
    check,
    check_heif,
    from_bytes,
    from_pillow,
    is_supported,
    open,
    open_heif,
    read,
    read_heif,
)
from .misc import get_file_mimetype, getxmp, set_orientation
from .thumbnails import add_thumbnails, thumbnail