from PySVG.Draw import Rect


class Box(Rect):
    def __init__(self, plot, pnt1, pnt2):
        super().__init__()
        self.plot = plot
        self.pnts = [pnt1, pnt2]
    
    def _process(self):
        exes = [pnt[0] for pnt in self.pnts]
        whys = [pnt[1] for pnt in self.pnts]
        
        x = self.plot.cart2pixel_x(exes)
        w = abs(x[0] - x[1])
        y = self.plot.cart2pixel_y(whys)
        h = abs(y[0] - y[1])
        
        self.x, self.y, self.w, self.h = min(x), min(y), w, h
    
    def construct(self):
        self._process()
        return super().construct()
        
        
        

