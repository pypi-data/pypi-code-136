"""Class to contain file information for a file and its associated hash file"""
import hashlib
from typing import Iterator
from .fileinfo import FileInfo


class FileWithHash:
    """Class to contain file information for a file and its associated hash file"""

    def __init__(self, file_: FileInfo, hashfile: FileInfo):
        if not hashfile.is_hashfile:
            raise ValueError(f"{hashfile.name} is not a hashfile!")
        if not hashfile.is_hash_for(file_):
            raise ValueError(
                f"{hashfile.name} is not the correct hashfile for {file_.name}!"
            )
        self.file = file_
        self.hashfile = hashfile

    def __iter__(self) -> Iterator[FileInfo]:
        yield self.file
        yield self.hashfile

    def remove(self) -> None:
        """Remove tarball and SHA512 hash"""
        for fileinfo in self:
            fileinfo.remove()

    def verify(self) -> bool:
        """Verify that a file matches its SHA512 hash"""
        # Get the file hash
        file_hash = hashlib.sha512()
        buffer_size = 524288  # read in chunks of 512kb
        with self.file.path.open("rb") as input_file:
            while True:
                input_bytes = input_file.read(buffer_size)
                if len(input_bytes):
                    file_hash.update(input_bytes)
                else:
                    break
        calculated_hash = file_hash.hexdigest().lower()
        # Read the reference hash
        with self.hashfile.path.open("r") as input_hash:
            reference_hash = "".join(input_hash.readlines()).split()[0].strip().lower()
        return calculated_hash == reference_hash
