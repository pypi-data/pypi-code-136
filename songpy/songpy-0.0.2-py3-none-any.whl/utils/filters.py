import re


class PolishNoteNamesPreprocessor:
    @classmethod
    def process(cls, raw: str) -> str:
        product = re.sub(r"\[B", "[Bb", raw)
        product = re.sub(r"\[H", "[B", product)
        return product
