class Param:
    def __init__(self, param) -> None:
        self.param = param
    
    @property
    def name(self) -> str:
        return self.param.name
    
    @property
    def units(self) -> str:
        return self.param.units
    
    @property
    def value(self):
        return self.param.value
    
    @value.setter
    def value(self, val):
        self.param.value = val
