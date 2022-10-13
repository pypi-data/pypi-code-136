"""Recordio reader/writer

Recordio is a file format for a sequence of records. Records are stored as an
unsigned varint specifying the length of data, followed by the data itself as
a binary blob.
"""


from io import BufferedReader, BufferedWriter
from typing import Iterable

from recordio import varint


class Reader:
    def __init__(self, file: BufferedReader):
        self._file = file

    def next(self) -> str:
        size = varint.decode_unsigned(self._file)
        data = self._file.read(size)
        return data.decode()


class Scanner:
    def __init__(self, file: BufferedReader):
        self._reader = Reader(file)

    def scan(self) -> Iterable[str]:
        try:
            while True:
                yield self._reader.next()
        except EOFError:
            return


class Writer:
    def __init__(self, file: BufferedWriter):
        self._file = file

    def write(self, record: str):
        data = record.encode()
        size = len(data)
        size_bytes = varint.encode_unsigned(size)
        self._file.write(size_bytes)
        self._file.write(data)
