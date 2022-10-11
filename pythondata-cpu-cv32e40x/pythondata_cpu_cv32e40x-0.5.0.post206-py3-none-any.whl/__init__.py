import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post206"
version_tuple = (0, 5, 0, 206)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post206")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post64"
data_version_tuple = (0, 5, 0, 64)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post64")
except ImportError:
    pass
data_git_hash = "0159258bb9e4dec35b556136f3dc468cb244b69e"
data_git_describe = "0.5.0-64-g0159258b"
data_git_msg = """\
commit 0159258bb9e4dec35b556136f3dc468cb244b69e
Merge: f17b92ad a91c67fe
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 11 15:03:08 2022 +0200

    Merge pull request #686 from silabs-oysteink/mscratchcsw_illegal
    
    Restricting CSR access to mscratchcsw[l] to CSRRW with rd != x0

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
