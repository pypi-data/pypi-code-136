from fastai.text import *
import sentencepiece as spm
from pathlib import Path
from typing import List

path = Path(__file__).parent

class IndicTokenizer():
    def __init__(self, lang: str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        model_path = path/f'models/{lang}/tokenizer.model'
        self.sp.Load(str(model_path))

    def tokenizer(self, t: str) -> List[str]:
        return self.sp.EncodeAsPieces(t)

    def numericalize(self, t: str) -> List[int]:
        return self.sp.EncodeAsIds(t)

    def textify(self, ids: List[int]) -> str:
        return (''.join([self.sp.IdToPiece(id).replace('▁', ' ') for id in ids])).strip()

    def remove_foreign_tokens(self, t: str):
        local_pieces = []
        for i in self.sp.EncodeAsIds(t):
            local_pieces.append(self.sp.IdToPiece(i))
        return local_pieces
