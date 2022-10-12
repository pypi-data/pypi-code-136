from .GraphSeries import GraphSeries

class Graph:
    def __init__(self, graph) -> None:
        self.graph = graph

    def export_graph_as_image(self, path: str, format: str, width: int, height: int, dpi: int):
        self.graph.export_graph_as_image(path, format, width, height, dpi)

    def set_dataset_reference(self, series: str, dataset: str):
        self.graph.set_dataset_reference(series, dataset)

    def open(self):
        self.graph.open()

    def close(self):
        self.graph.close()

    @property
    def name(self) -> str:
        return self.graph.name
    
    @property
    def graphSeries(self) -> GraphSeries:
        return {k:GraphSeries(x) for (k,x) in self.graph.graphSeries.items()}
