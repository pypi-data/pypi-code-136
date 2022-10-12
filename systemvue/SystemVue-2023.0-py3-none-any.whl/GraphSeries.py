class GraphSeries:
    def __init__(self, graphSeries) -> None:
        self.graphSeries = graphSeries

    def setContext(self, context: str):
        self.graphSeries.setContext(context)
    
    @property
    def name(self) -> str:
        return self.graphSeries.name
