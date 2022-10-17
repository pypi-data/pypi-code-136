# standard libraries
from typing import NoReturn

try:
    from .main import (
        main,  # pyright: ignore [reportUnusedImport, reportGeneralTypeIssues]
    )
except ImportError:

    def main() -> NoReturn:
        # standard libraries
        import sys

        print(
            "The infiniaml CLI could not run because the required "
            "dependencies were not installed.\nMake sure you've installed "
            "everything with: pip install 'infiniaml_client[cli]'"
        )
        sys.exit(1)
