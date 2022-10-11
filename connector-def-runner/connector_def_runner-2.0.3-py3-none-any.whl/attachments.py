import io
import re


FILENAME_HEADER_KEY = 'Content-Disposition'
FILENAME_REGEX = """filename=['"]?([^"']*)['"]"""


def get_filename(response):
    """ Posts a file obtained from the response.
    """
    filename = 'unknown'
    if FILENAME_HEADER_KEY in response.headers:
        match = re.search(FILENAME_REGEX, response.headers[FILENAME_HEADER_KEY])
        if match:
            filename = match.group(1)
    return filename


def get_file_object(response):
    return {
        'filename': get_filename(response),
        'file_data': io.BytesIO(response.content)
    }


def parse_attachment_output(response, manifest):
    if 'file' not in manifest['output'].get('properties', {}):
        return

    if manifest['output']['properties']['file']['type'] == 'array':
        return [get_file_object(response)]
    else:
        return get_file_object(response)
