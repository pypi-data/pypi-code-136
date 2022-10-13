import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.6.0.post142"
version_tuple = (0, 6, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post0"
data_version_tuple = (0, 6, 0, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post0")
except ImportError:
    pass
data_git_hash = "383be6ebc6987a0d97c0462e0adb417f2b0f29e8"
data_git_describe = "0.6.0-0-g383be6eb"
data_git_msg = """\
commit 383be6ebc6987a0d97c0462e0adb417f2b0f29e8
Merge: 2144858d 76d9a0fd
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Oct 12 08:48:25 2022 +0200

    Merge pull request #688 from Silabs-ArjanB/ArjanB_csrrsx0
    
    Fixed description for which CSR instructions on mscratchcsw and mscra…

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
