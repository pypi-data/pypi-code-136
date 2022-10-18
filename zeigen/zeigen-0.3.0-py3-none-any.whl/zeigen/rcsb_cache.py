"""Download/cache RCSB structure files."""
from __future__ import annotations

import gzip
import os
import shutil
import sys
from pathlib import Path

# third-party imports
import loguru
import typer
from loguru import logger as mylogger
from progressbar import DataTransferBar  # type: ignore
from requests.exceptions import HTTPError  # type: ignore
from requests_download import ProgressTracker  # type: ignore
from requests_download import download as request_download  # type: ignore


DEFAULT_CACHE_DIR = "./"
ENV_CACHE_DIR = "RCSB_CACHE_DIR"
FILES_URL = "https://files.rcsb.org/download/"
MODELS_URL = "https://models.rcsb.org/"
STRUCTURE_FILE_TYPES = {
    "pdb": {"ext": ".pdb", "url": FILES_URL},
    "cif": {"ext": ".cif", "url": FILES_URL},
    "bcif": {"ext": ".bcif", "url": MODELS_URL},
    "xml": {"ext": ".xml", "url": FILES_URL},
    "xml-header": {"ext": "-noatom.xml", "url": FILES_URL},
    "assembly-pdb": {"ext": ".pdb1", "url": FILES_URL},
    "assembly-cif": {"ext": "-assembly1.cif", "url": FILES_URL},
    "assembly-bcif": {"ext": ".bcif", "url": MODELS_URL},
}
ID_FIELD_LEN = 4
DEFAULT_COMMANDLINE_TYPE = "pdb"
DEFAULT_SCRIPT_TYPE = "cif"


class RCSBCache:
    """Cache RCSB structure files."""

    def __init__(
        self,
        logger: loguru.Logger | None = None,
        module_name: str | None = None,
        app: typer.Typer | None = None,
    ) -> None:
        """Create run values."""
        self._app: typer.Typer | None = app
        if logger is None:
            self._logger = mylogger
        else:
            self._logger = logger
        if self._app is not None:

            @self._app.command()
            def get_structure(
                rcsb_id: str,
                file_type: str = DEFAULT_COMMANDLINE_TYPE,
                compressed: bool = True,
                cache_dir: str = DEFAULT_CACHE_DIR,
                verbose: bool = True,
            ) -> None:
                """Download & cache RCSB structure file."""
                file_path = self.rcsb_cache(
                    rcsb_id, file_type, compressed, cache_dir, verbose
                )
                print(file_path)

    def rcsb_normalize(self, id: str) -> str:
        """Check and normalize RCSB ID."""
        if len(id) != ID_FIELD_LEN:
            raise ValueError(f'RCSB ID "{id}" is too long.')
        if not id[0].isnumeric():
            raise ValueError(f'First character of RCSB ID "{id}" is not numeric.')
        return id.upper()

    def decompress_gz_file(self, in_path: Path) -> None:
        """Decompress gzipped file."""
        out_path = in_path.parent / in_path.stem
        with gzip.open(in_path, "rb") as f_in:
            with out_path.open("wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        in_path.unlink()

    def get_ext_and_url(self, file_type: str) -> tuple[str, str]:
        """Look up extension and url for filetype."""
        if file_type in STRUCTURE_FILE_TYPES:
            ext = STRUCTURE_FILE_TYPES[file_type]["ext"]
            url = STRUCTURE_FILE_TYPES[file_type]["url"]
        else:
            self._logger.error(f"File type {file_type} not defined.")
            self._logger.error(
                f"Known file types are {list(STRUCTURE_FILE_TYPES.keys())}."
            )
        return ext, url

    def get_cache_path(self, cache_dir: str) -> Path:
        """Create cache path, checking envvar."""
        if ENV_CACHE_DIR in os.environ:
            cache_path = Path(os.environ[ENV_CACHE_DIR])
        else:
            cache_path = Path(cache_dir)
        if not cache_path.exists():
            self._logger.error(f"Cache dir {cache_path} does not exist.")
            sys.exit(1)
        return cache_path

    def rcsb_cache(
        self,
        rcsb_id: str,
        file_type: str = DEFAULT_SCRIPT_TYPE,
        compressed: bool = True,
        cache_dir: str = DEFAULT_CACHE_DIR,
        verbose: bool = False,
    ) -> Path:
        """Download structure file to cache."""
        try:
            rcsb_id = self.rcsb_normalize(rcsb_id)
        except ValueError as error:
            self._logger.error(error)
            sys.exit(1)
        cache_path = self.get_cache_path(cache_dir)
        ext, url = self.get_ext_and_url(file_type)
        filename = f"{rcsb_id}{ext}"
        cached_file_path = cache_path / filename
        if compressed:
            dl_filename = filename + ".gz"
            compression = "compressed"
        else:
            dl_filename = filename
            compression = ""
        dl_path = cache_path / dl_filename
        if not cached_file_path.exists():
            try:
                if verbose:
                    self._logger.info(
                        f"Downloading {compression}"
                        + f' {file_type} file {rcsb_id} to "{cache_path}".'
                    )
                    trackers = (ProgressTracker(DataTransferBar()),)
                    request_download(url + dl_filename, dl_path, trackers=trackers)
                else:
                    request_download(url + dl_filename, dl_path)
            except HTTPError:
                self._logger.error(
                    f"{file_type} entry for {rcsb_id} not found in RCSB."
                )
                self._logger.error(f"URL was {url + dl_filename}")
                sys.exit(1)
            if compressed:
                self.decompress_gz_file(dl_path)
        return cached_file_path
