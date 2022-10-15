from carveman.carver.CarverBase import CarverBase

class PDFCarver(CarverBase):
    def __init__(self, dir) -> None:
        super().__init__(dir)
        self._setDir("pdf")
        self._addSignature(".pdf", "25504446", "2525454F46")