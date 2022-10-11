from distutils.core import setup
import os
import sys

def is_venv():
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or
        (os.environ.get("CONDA_PREFIX", None) is not None)
    )

if not is_venv():
    print("WARNING: you should be installing this package within a virtual environment")
    print("(if running from google colab, ignore this message)")

# Let's go
setup()
