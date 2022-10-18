"""Class to relate local and remote information about a Spark/Hadoop file"""
import requests
import pathlib3x as pathlib
import tqdm


class FileInfo:
    """Class to relate local and remote information about a Spark/Hadoop file"""

    def __init__(self, remote_url: str, local_path: pathlib.Path):
        self.url = remote_url
        self.path = local_path

    @property
    def name(self) -> str:
        """Get the name of the local file"""
        return self.path.name

    @property
    def is_hashfile(self) -> bool:
        """Boolean indicating whether this is a hashfile"""
        return self.path.suffix == ".sha512"

    def download(self) -> None:
        """Download this Spark/Hadoop version from a remote URL to a local path"""
        response = requests.get(self.url, stream=True, allow_redirects=True)
        content_length = response.headers.get("content-length")
        total_bytes = int(content_length) if content_length else None
        with open(self.path, "wb") as output_file:
            with tqdm.tqdm(
                total=total_bytes, unit="B", unit_scale=True
            ) as progress_bar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        output_file.write(chunk)
                        progress_bar.update(len(chunk))

    def is_hash_for(self, other: "FileInfo") -> bool:
        """Boolean indicating whether this is the hashfile corresponding to another file"""
        return self.is_hashfile and self.path.stem == other.path.name

    def remove(self) -> None:
        """Remove the local file"""
        if self.path.is_file():
            self.path.unlink()
