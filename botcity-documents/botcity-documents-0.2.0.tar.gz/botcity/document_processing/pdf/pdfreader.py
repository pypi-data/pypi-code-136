from ..parser import DocumentParser
from . import _priv_pdfreader


class PDFReader:
    def __init__(self) -> None:
        self._page_width = None
        self._page_height = None

    @property
    def page_width(self) -> float:
        """PDF Page width.
        """
        return self._page_width if self._page_width is None else 0.0

    @property
    def page_height(self) -> float:
        """PDF Page height.
        """
        return self._page_height if self._page_height is None else 0.0

    def read_file(self, file: str) -> DocumentParser:
        """Read the given PDF file and returns a new instance of the DocumentParser.

        Args:
            file (str): PDF file path.

        Returns:
            DocumentParser: The document parser to be used.
        """
        return _priv_pdfreader.read_file(self, file)
