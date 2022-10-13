import json
from json.decoder import JSONDecodeError

from e2j2.exceptions import E2j2Exception


def parse(json_file):
    try:
        with open(json_file) as fh:
            data = json.load(fh)
    except IOError as err:
        # Mark as failed
        raise E2j2Exception("IOError raised while reading file") from err
    except JSONDecodeError as err:
        raise E2j2Exception("invalid JSON") from err

    return data
