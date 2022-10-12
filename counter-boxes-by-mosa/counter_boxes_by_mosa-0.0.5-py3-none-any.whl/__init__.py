import sys
from pathlib import Path

FILE = Path(__file__).resolve()
root_path = FILE.parents[0]
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))
