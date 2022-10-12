import os


def find_meta_file(gml_file: str = None) -> str | None:
    """
    Returns a meta_file file path for a given gml file. Usually a .xsd or .gfs file
    :param gml_file: file path for gml file
    :return: meta_file: file path to meta file or None if not found
    """

    dirname = os.path.dirname(gml_file)
    basename = os.path.basename(gml_file)
    basename_no_ext = os.path.splitext(basename)[0]

    files_temp = [filename for filename in os.listdir(dirname) if filename.lower().startswith(basename_no_ext.lower()) and filename != basename]
    if files_temp:
        meta_file = os.path.join(dirname, files_temp[0])
    else:
        meta_file = None

    return meta_file
