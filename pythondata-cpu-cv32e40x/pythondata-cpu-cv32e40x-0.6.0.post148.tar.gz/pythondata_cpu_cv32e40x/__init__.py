import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.6.0.post148"
version_tuple = (0, 6, 0, 148)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post148")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post6"
data_version_tuple = (0, 6, 0, 6)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post6")
except ImportError:
    pass
data_git_hash = "eac5a0fe86c6509dddc2faba2a4c4118b97a29cf"
data_git_describe = "0.6.0-6-geac5a0fe"
data_git_msg = """\
commit eac5a0fe86c6509dddc2faba2a4c4118b97a29cf
Merge: 383be6eb 255a2a33
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 19 07:57:41 2022 +0200

    Merge pull request #689 from silabs-oysteink/clic-updates
    
    Updates related to PR #680

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
