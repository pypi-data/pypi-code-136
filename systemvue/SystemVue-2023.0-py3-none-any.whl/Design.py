from .Param import Param
from .Part import Part

class Design:
    def __init__(self, design) -> None:
        self.design = design
    
    @property
    def name(self) -> str:
        return self.design.name
    
    @property
    def parts(self) -> dict[str, Part]:
        return {k:Part(x) for (k,x) in self.design.parts.items()}
    
    @property
    def parameters(self) -> dict[str, Param]:
        return {k:Param(x) for (k,x) in self.design.parameters.items()}
