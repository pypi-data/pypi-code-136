from PySVG.Draw import Generic_Path


class Line(Generic_Path):
    def __init__(self, plot, pnt1, pnt2):
        super().__init__()
        self.plot = plot
        self.pnts = [pnt1, pnt2]
    
    def _process(self):
        exes = [pnt[0] for pnt in self.pnts]
        whys = [pnt[1] for pnt in self.pnts]
        
        x = self.plot.cart2pixel_x(exes)
        y = self.plot.cart2pixel_y(whys)
        
        self.points = [('M', x[0], y[0]), ('L', x[1], y[1])]
    
    def construct(self):
        self._process()
        return super().construct()
        
        
        

