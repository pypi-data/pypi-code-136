from carveman.carver.CarverBase import CarverBase

class ImageCarver(CarverBase):
    def __init__(self, dir) -> None:
        super().__init__(dir)
        self._setDir("image")
        self._addSignature(".jpg", "FFD8FFE0", "FFD9")
        self._addSignature(".png", "89504E470D0A1A0A", "49454E44AE426082")