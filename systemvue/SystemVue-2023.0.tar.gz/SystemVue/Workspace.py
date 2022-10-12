from .Analysis import Analysis
from .DataSet import DataSet
from .Design import Design
from .Equations import Equations
from .Graph import Graph
from .Variable import Variable

class Workspace:
    """
    A class for Workspace
    ...

    Attributes
    ----------
    workspace_path : str
        path to workspace
    name : str
        name of workspace
    datasets : dict[str, DataSet]
        dict of (name, dataset) as the (key, value) pair in the workspace
    analyses : dict[str, Analysis]
        dict of (name, analysis) as the (key, value) pair in the workspace
    equations : dict[str, Equations]
        dict of (name, equations) as the (key, value) pair in the workspace
    graphs : dict[str, Graph]
        dict of (name, graph) as the (key, value) pair in the workspace
    variables : dict[str, Variable]
        dict of (name, variable) as the (key, value) pair in the workspace
    designs : dict[str, Design]
        dict of (name, design) as the (key, value) pair in the workspace

    Methods
    -------
    create_dataset -> DataSet
        creates a dataset and returns it
    addVariable() -> Variable
        adds variable to workspace and returns the variable
    """
    def __init__(self, ws) -> None:
        self.ws = ws

    def createDataSet(self, dataSetName: str) -> DataSet:
        """
        Creates a dataset and returns it
        """
        return DataSet(self.ws.createDataSet(dataSetName))

    def addVariable(self) -> Variable:
        """
        Adds variable to workspace and returns the variable
        """
        return self.ws.addVariable()

    @property
    def name(self) -> str:
        """
        Returns name of workspace
        """
        return self.ws.name

    @property
    def workspace_path(self) -> str:
        """
        Returns path to workspace
        """
        return self.ws.workspace_path

    @property
    def analyses(self) -> dict[str, Analysis]:
        """
        Returns dict of (name, analysis) as the (key, value) pair in the workspace
        """
        return {k:Analysis(x) for (k,x) in self.ws.analyses.items()}

    @property
    def datasets(self) -> dict[str, DataSet]:
        """
        Returns dict of (name, dataset) as the (key, value) pair in the workspace
        """
        return {k:DataSet(x) for (k,x) in self.ws.datasets.items()}

    @property
    def designs(self) -> dict[str, Design]:
        """
        dict of (name, design) as the (key, value) pair in the workspace
        """
        return {k:Design(x) for (k,x) in self.ws.designs.items()}

    @property
    def equations(self) -> dict[str, Equations]:
        """
        Returns dict of (name, equations) as the (key, value) pair in the workspace
        """
        return {k:Equations(x) for (k,x) in self.ws.equations.items()}

    @property
    def graphs(self) -> dict[str, Graph]:
        """
        Returns dict of (name, graph) as the (key, value) pair in the workspace
        """
        return {k:Graph(x) for (k,x) in self.ws.graphs.items()}

    @property
    def variables(self) -> dict[str, Variable]:
        """
        dict of (name, variable) as the (key, value) pair in the workspace
        """
        return {k:Variable(x) for (k,x) in self.ws.variables.items()}
