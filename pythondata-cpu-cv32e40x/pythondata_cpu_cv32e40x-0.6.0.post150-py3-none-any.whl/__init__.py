import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.6.0.post150"
version_tuple = (0, 6, 0, 150)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post150")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post8"
data_version_tuple = (0, 6, 0, 8)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post8")
except ImportError:
    pass
data_git_hash = "42281285739d2238a9031144e4373ef2ab6a25d2"
data_git_describe = "0.6.0-8-g42281285"
data_git_msg = """\
commit 42281285739d2238a9031144e4373ef2ab6a25d2
Merge: eac5a0fe 202d4b9d
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 19 15:47:37 2022 +0200

    Merge pull request #690 from silabs-oivind/fix_e40s_issue_277
    
    Clear mstatus.mprv when entering user mode through dret

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
