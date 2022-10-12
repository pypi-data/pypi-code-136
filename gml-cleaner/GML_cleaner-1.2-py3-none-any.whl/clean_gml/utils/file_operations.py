import os


def get_file_split(file: str = None) -> tuple[str | None, str | None, str | None]:
    dirname = os.path.dirname(file)
    filename_no_ext = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    return dirname, filename_no_ext, extension
