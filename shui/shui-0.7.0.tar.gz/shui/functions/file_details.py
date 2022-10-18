"""Functions for downloading a particular version from the remote repository"""
import pathlib3x as pathlib
from shui.classes import FileInfo, FileWithHash, Version


def get_file_details(version: Version, install_dir: pathlib.Path) -> FileWithHash:
    """Construct local paths for a particular Spark/Hadoop version"""
    tarball_path = install_dir / version.filename
    sha512_path = tarball_path.append_suffix(".sha512")
    return FileWithHash(
        FileInfo(version.url, tarball_path),
        FileInfo(f"{version.url}.sha512", sha512_path),
    )
