# apt-get install libffi-dev # To avoid installation error: ModuleNotFoundError: No module named '_ctypes'
from repo_utils import install_dependencies
import os

# Install requirements of all definitions in the repository
install_dependencies(os.path.dirname(__file__))