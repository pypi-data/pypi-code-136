from .DataSet import DataSet
from .Design import Design


class Analysis:
    def __init__(self, analysis) -> None:
        self.analysis = analysis

    def run(self):
        self.analysis.run()
    
    @property
    def name(self) -> str:
        return self.analysis.name
    
    @property
    def dataset_name(self) -> str:
        return self.analysis.dataset_name

    @dataset_name.setter
    def dataset_name(self, name: str):
        self.analysis.dataset_name = name
    
    @property
    def design_name(self) -> str:
        return self.analysis.design_name

    @design_name.setter
    def design_name(self, name: str):
        self.analysis.design_name = name
    
    @property
    def design(self) -> Design:
        return Design(self.analysis.design)
    
    @property
    def dataset(self) -> DataSet:
        return DataSet(self.analysis.dataset)
