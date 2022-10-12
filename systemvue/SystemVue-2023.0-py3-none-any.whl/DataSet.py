from .Variable import Variable

class DataSet:
    def __init__(self, dataset) -> None:
        self.dataset = dataset

    def createVariable(self, name: str) -> Variable:
        return Variable(self.dataset.createVariable(name))

    def deleteVariable(self, name: str):
        self.dataset.deleteVariable(name)

    def importData(self, fileSpecification: str, format: str, options):
        self.dataset.importData(fileSpecification, format, options)

    def exportData(self, fileSpecification: str, format: str, options):
        self.dataset.exportData(fileSpecification, format, options)
    
    @property
    def name(self) -> str:
        return self.dataset.name
    
    @property
    def variables(self) -> dict[str, Variable]:
        return {k:Variable(x) for (k,x) in self.dataset.variables.items()}
