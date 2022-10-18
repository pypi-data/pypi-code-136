import os
import tarfile


async def is_tarfile(filename):
    """
    Wrapper for tarfile.is_tarfile on the hub
    """
    return tarfile.is_tarfile(filename)


async def extractall(filename, destination):
    """
    Wrapper for tarfile.extractall on the hub
    """

    def _is_within_directory(directory, target):
        """
        Helper function to ensure tar members are within the common prefix
        """
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
        prefix = os.path.commonprefix([abs_directory, abs_target])
        return prefix == abs_directory

    def _safe_extract(tar, path=".", members=None, numeric_owner=False):
        """
        Helper function to prevent path traversal in tarfile.extractall
        """
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not _is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
        tar.extractall(path, members, numeric_owner=numeric_owner)

    if hub.exec.tar.is_tarfile(filename):
        with tarfile.open(filename) as tar_source:
            _safe_extract(tar_source, destination)

    return True
