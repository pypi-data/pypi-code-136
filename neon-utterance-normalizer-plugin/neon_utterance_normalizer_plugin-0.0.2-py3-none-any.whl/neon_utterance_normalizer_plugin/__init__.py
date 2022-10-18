# # NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# # All trademark and other rights reserved by their respective owners
# # Copyright 2008-2021 Neongecko.com Inc.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re
import lingua_franca.config

from typing import List, Optional
from lingua_franca.parse import normalize
from neon_transformers import UtteranceTransformer
from neon_transformers.tasks import UtteranceTask


class UtteranceNormalizer(UtteranceTransformer):
    task = UtteranceTask.TRANSFORM

    def __init__(self, name="utterance_normalizer", priority=1):
        super().__init__(name, priority)
        lingua_franca.config.load_langs_on_demand = True

    def transform(self, utterances: List[str],
                  context: Optional[dict] = None) -> (list, dict):
        context = context or {}
        lang = context.get("lang") or self.config.get("lang", "en-us")
        clean = [self._strip_punctuation(u) for u in utterances]
        norm = [normalize(u, lang=lang, remove_articles=False) for u in clean]
        norm2 = [normalize(u, lang=lang, remove_articles=True) for u in clean]
        norm += [u for u in norm2 if u not in utterances and u not in norm]
        norm += [u for u in clean if u not in utterances and u not in norm]
        norm = [u for u in norm if u not in utterances]
        return norm + utterances, {}

    @staticmethod
    def _strip_punctuation(utterance: str):
        return utterance.rstrip('.').rstrip('?').rstrip('!')
