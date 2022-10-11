import json
import logging
from copy import deepcopy
from typing import Text

import regex

from seetm.shared.constants import (
    Encoding,
    FilePermission,
    TOKEN_TO_TOKEN_MAP_PATH,
)

logger = logging.getLogger(__name__)


class TokenToTokenMapper:
    def __init__(self, case_sensitive: bool = True):
        self.case_sensitive = case_sensitive
        try:
            with open(
                    file=TOKEN_TO_TOKEN_MAP_PATH,
                    mode=FilePermission.READ,
                    encoding=Encoding.UTF8
            ) as token_to_token_map_file:
                self.token_to_token_map = json.load(token_to_token_map_file)
        except Exception as e:
            logger.debug(e)
            logger.warning("Failed to load token_to_token_map. "
                           "Rule based mappings will be ignored")
            self.token_to_token_map = {}

    def get_mappables(self):
        return list(self.token_to_token_map.keys()) + list(self.token_to_token_map.values())

    def get_maps(self):
        return self.token_to_token_map

    def map(self, text: Text) -> Text:
        text_copy = deepcopy(text)
        text_copy = text_copy.strip()

        if not self.case_sensitive:
            text_copy = str.lower(text_copy)

        for token_key, token_map in self.token_to_token_map.items():
            if not self.case_sensitive:
                token_map = [str.lower(token) for token in token_map]
            token_map = list(set(token_map))

            # sort in decending order to captcher longer patterns first
            token_map.sort(key=lambda x: len(x), reverse=True)

            for pattern in token_map:
                if pattern == token_key:
                    continue

                text_copy = regex.sub('[\s]' + pattern + '[\s]', f" {token_key} ", text_copy)
                text_copy = regex.sub('^' + pattern + '[\s]', f"{token_key} ", text_copy)
                text_copy = regex.sub('[\s]' + pattern + '$', f" {token_key}", text_copy)
                text_copy = regex.sub('^' + pattern + '$', f"{token_key}", text_copy)
        return text_copy
