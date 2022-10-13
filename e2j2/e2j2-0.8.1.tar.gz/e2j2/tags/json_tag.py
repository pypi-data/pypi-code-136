import json
import re
from json.decoder import JSONDecodeError

from e2j2.exceptions import E2j2Exception


def parse(json_string):
    try:
        # handle hashrocket styled json
        if re.search(r'"\s*=>\s*["{[]', json_string):
            return json.loads(re.sub(r'"\s*=>\s*', '":', json_string))
        return json.loads(json_string)
    except JSONDecodeError as err:
        raise E2j2Exception("invalid JSON") from err
