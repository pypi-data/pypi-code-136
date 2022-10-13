from typing import List, Union

import mcdm
import plotly.express as px
from aidev.utilities.types import Visualization
from numpy import abs, where
from aidev.utilities.types import FeatureDefinition
from pandas import DataFrame
from plotly.graph_objects import Figure


class Decision:
    """
    Class implementing Multi-Criteria Decision-Making (MCDM) techniques.
    """

    def __init__(
        self,
        data: DataFrame,
        features: FeatureDefinition,
        rank_type: str = "TOPSIS",
        weight_type: str = "MW",
        norm_type: str = "Vector",
    ) -> None:
        """

        :param data: The generated data.
        :type data: DataFame
        :param weights: list of weights to assign to each objective.
        :type weights: list
        :param rank_type: Method to performa MCDM.
        :type rank_type: str
        :param weight_type: Method used to handle weights.
        :type weight_type: str
        :param norm_type: Method used to calculated distances between designs.
        :type norm_type: str
        """

        nonzero_weights_objanme = []
        nonzero_weights = []

        for objname, weight in features.weights.items():
            if weight != 0:
                nonzero_weights_objanme.append(objname)
                nonzero_weights.append(weight)

        self.alternatives = data[nonzero_weights_objanme].values
        self.weights = nonzero_weights
        self.rank_type = rank_type
        self.weight_type = weight_type
        self.norm_type = norm_type

    def decide(self, data: DataFrame, return_choices: int = 10) -> DataFrame:
        """

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param return_choices: Number of sorted best designs to return.
        :type return_choices: int
        :return: A dataframe containing the best designs
        :rtype: DataFrame
        """
        ranked_sol = mcdm.rank(
            self.alternatives,
            w_vector=abs(list(self.weights)),
            alt_names=list(range(len(self.alternatives))),
            is_benefit_x=[False if weight >= 0 else True for weight in self.weights],
            n_method=self.norm_type,
            w_method=self.weight_type,
            s_method=self.rank_type,
        )
        bests_id = [sol[0] for sol in ranked_sol]
        is_eff = [
            True if i in bests_id[:return_choices] else False
            for i in range(data.shape[0])
        ]
        data["efficiency"] = where(is_eff, "Efficient", "Sub-Optimal")

        return data


class ScatterPlot(Visualization):
    """
    Implementation of Scatter plot visualization of the Pareto-Front.
    """

    def __init__(
        self,
        data: DataFrame,
        pareto_x: str,
        pareto_y: str,
        save: bool = True,
        figname: str = "pareto.html",
        **kwargs
    ) -> None:
        """

        :param pareto_x: target to plot on the x-axis.
        :type pareto_x: str
        :param pareto_y: target to plot on the y-axis.
        :type pareto_y: str
        """
        self.pareto_x = pareto_x
        self.pareto_y = pareto_y
        super().__init__(data, save, figname, **kwargs)

    def _method(self, data, **kwargs) -> Figure:
        """

        Method defining the scatter plot.

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (plotly Figure)
        :rtype: Figure

        See https://plotly.com/python/line-and-scatter/
        """
        if "efficiency" in data:
            m = px.scatter(data, x=self.pareto_x, y=self.pareto_y, color="efficiency")
        else:
            m = px.scatter(data, x=self.pareto_x, y=self.pareto_y)
        return m


class HeatMap(Visualization):
    """
    Implementation of Heatmap plot to visualize parameter correlations.
    """

    def __init__(
        self,
        data: DataFrame,
        columns: Union[List[str], None] = None,
        save: bool = True,
        figname: str = "correlations.html",
        **kwargs
    ) -> None:
        """
        :param columns: Columns name including parameters and targets to be included in the visualization.
        :type columns: Union[List[str], None]
        """
        self.columns = columns
        super().__init__(data, save, figname, **kwargs)

    def _method(self, data, **kwargs) -> Figure:
        """
        Method defining the heatmap plot

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (plotly Figure)
        :rtype: Figure

        See https://plotly.com/python/imshow/
        """
        if self.columns and set(self.columns).issubset(data.columns):
            data = data[self.columns]
        m = px.imshow(data.corr(), text_auto=".1f")  # type: ignore
        return m


class ParallelCoord(Visualization):
    def __init__(
        self,
        data: DataFrame,
        columns: Union[List[str], None] = None,
        save: bool = True,
        figname: str = "parallelcoord.html",
        **kwargs
    ):
        self.columns = columns
        super().__init__(data, save, figname, **kwargs)

    def _method(self, data, **kwargs) -> Figure:
        """
        Method defining the heatmap plot

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (plotly Figure)
        :rtype: Figure

        See https://plotly.com/python/imshow/
        """
        if self.columns and set(self.columns).issubset(data.columns):
            data = data[self.columns]
        m = px.parallel_coordinates(data, dimensions=list(data.columns))
        return m


# class PairCorr(Visualization):
#     """
#     Implementation of Scatter plot visualization of the Pareto-Front.
#     """

#     def __init__(
#         self,
#         data: DataFrame,
#         columns: Union[List[str], None] = None,
#         save: bool = True,
#         figname: str = "results.png",
#         **kwargs
#     ) -> None:
#         """
#         :param columns: Columns name including parameters and targets to be included in the visualization.
#         :type columns: Union[List[str], None]
#         """
#         self.columns = columns
#         super().__init__(data, save, figname, **kwargs)

#     def _method(self, data, **kwargs):
#         """
#         Method defining the pairwise plot.

#         :param data: pandas dataframe for training surrogate model.
#         :type data: DataFrame
#         :param kwargs: Optional arguments (see child classes)
#         :type kwargs:
#         :return: The visualization object (plotly Figure)
#         :rtype: Figure

#         See https://seaborn.pydata.org/generated/seaborn.pairplot.html
#         """
#         if self.columns and set(self.columns).issubset(data.columns):
#             data = data[self.columns]
#         m = PairGrid(data)
#         m.map_lower(scatterplot)
#         try:
#             m.map_upper(kdeplot)
#         except:
#             # with badly scaled objectives the kdeplot might fail
#             m.map_upper(scatterplot)
#         m.map_diag(histplot)
#         return m
