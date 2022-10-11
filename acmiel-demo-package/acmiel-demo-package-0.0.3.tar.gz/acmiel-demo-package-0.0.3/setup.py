import os
import tempfile
from pathlib import Path

from setuptools import setup


USER = os.getenv("USERNAME") or "sir"


def say_hi():
    tmpdir = Path(tempfile.gettempdir())
    hello_file = tmpdir / "hello-from-acmiel.txt"
    hello_content = (
        f"Hello {USER}, thanks for attempting to install this package! 💛\n"
        "\n"
        "I promise I didn't do anything malicious (no really)."
    )

    if not hello_file.exists():
        hello_file.write_text(hello_content + "\n")
        raise ValueError(f"There is a message for you in {hello_file} :-)")
    else:
        raise ValueError(hello_content)


if os.getenv("BUILDING_RELEASE") != "1":
    say_hi()

setup(
    name="acmiel-demo-package",
    version="0.0.3",
    long_description="Demo package to show why setup.py is scary.",
    long_description_content_type="text/x-rst",
)
