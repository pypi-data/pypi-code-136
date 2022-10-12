from .Param import Param

class Part:
    def __init__(self, part) -> None:
        self.part = part
    
    @property
    def name(self) -> str:
        return self.part.name
    
    @property
    def model(self) -> str:
        return self.part.model
    
    @property
    def parameters(self) -> dict[str, Param]:
        return {k:Param(x) for (k,x) in self.part.parameters.items()}
