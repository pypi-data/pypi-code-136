from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Tuple
from collections.abc import Iterable

from numpy import ndarray, concatenate
from pandas import DataFrame
from plotly.graph_objects import Figure
from pymoo.core.callback import Callback
from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline


class Target:
    """
    Class for defining a target variable.
    """

    def __init__(
        self,
        name: str,
        weight: float,
        is_objective: bool = True,
        ineq: float = None,  # type: ignore has to remain float otherwise the GUI won't recognise what inpuit field to give
    ) -> None:
        """

        Initialize class.

        :param name: name of the target (as defined in NX).
        :type name: str
        :param ineq: Value of inequality constraint. Objective should be <= then ineq. Default None.
        :type ineq: float
        :return:
        :rtype: None
        """
        self.name = name
        self.weight = weight
        self.is_objective = is_objective
        self.ineq = ineq

    def __repr__(self) -> str:
        return f"Target('{self.name}', {self.weight}, {self.is_objective}, {self.ineq})"


class Parameter:
    """
    Class for defining a parameter variable.
    """

    def __init__(self, name: str, lb: float, ub: float) -> None:
        """

        Initialize class.

        :param name: Name of parameter.
        :type name: str
        :param lb: Lower bound of parameter.
        :type lb: float
        :param ub: Upper bound of parameter.
        :type ub: float
        :return:
        :rtype: None
        """
        self.name = name
        self.lb = lb
        self.ub = ub

    def __repr__(self) -> str:
        return f"Parameter('{self.name}', {self.lb}, {self.ub}"


class FeatureDefinition:
    """
    Class used to combined and extract parameters and targets related information.

    """

    def __init__(self, parameters: List[Parameter], targets: List[Target]) -> None:
        """

        Initialize class.

        :param parameters: List of parameter objects.
        :type parameters: List[Parameter]
        :param targets: List of target objects.
        :type targets: List[Target]
        :return:
        :rtype: None
        """
        self.parameters = parameters
        self.targets = targets
        self._update()

    def _update(self) -> None:
        """
        Update calculated and extracted values from parameters and targets.

        """
        self.pnames = [p.name for p in self.parameters]
        self.lbs = {p.name: p.lb for p in self.parameters}
        self.ubs = {p.name: p.ub for p in self.parameters}
        self.nvar = len(self.parameters)

        self.tnames = [t.name for t in self.targets]
        self.weights = {t.name: t.weight for t in self.targets}
        self.are_obj = {t.name: t.is_objective for t in self.targets}
        self.ineqs = {t.name: t.ineq for t in self.targets}


class Visualization(ABC):
    """
    Abstract class for results visualization.
    """

    def __init__(
        self,
        data: DataFrame,
        save: bool = True,
        figname: str = "results.html",
        **kwargs,
    ):
        """

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param save: Whether to save the generated image.
        :type save: bool
        :param figname: name to give to generated image.
        :type figname: str
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (plotly Figure)
        :rtype: Figure
        """
        self.fig = self._method(data, **kwargs)
        if save:
            self.fig.write_html(figname)

    def getfig(self):
        return self.fig

    @abstractmethod
    def _method(self, data: DataFrame, **kwargs) -> Figure:
        """
        Method defining visualization object. To be overridden.

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (plotly Figure)
        :rtype: Figure
        """
        pass


class Surrogate(ABC):
    """
    Abstract class for surrogate modelling.
    """

    def __call__(
        self, data: DataFrame, features: FeatureDefinition
    ) -> Tuple[Callable[..., List[float]], Tuple[float, float]]:
        """

        :param x: Data containing predictor values.
        :type x: Union[List, ndarray]
        :param y: Data containing target values.
        :type y: Union[List, ndarray]
        :return: Trained surrogate sklearn model and tuple containing model accuracy and standard deviation
        :rtype: tuple
        """

        x = data[features.pnames].values
        y = data[
            [
                tname
                for tname, is_obj, is_constr in zip(
                    features.tnames, features.are_obj.values(), features.ineqs.values()
                )
                if is_obj != 0 or is_constr is not None
            ]
        ].values

        pipe = self._model()
        model = pipe.fit(x, y)
        scores = cross_val_score(model, x, y, cv=4)
        performance = (scores.mean(), scores.std())

        def sur(x: List[float]) -> List[float]:
            return model.predict([x])[0]

        return sur, performance

    @abstractmethod
    def _model(self) -> Pipeline:
        """
        Method defining the surrogate model. To be overridden.

        :return: Sklearn pipeline containing the surrogate model.
        :rtype:
        """
        pass


class Sampling(ABC):
    """
    Abstract class for DoE sampling.
    """

    def __init__(self, features: FeatureDefinition) -> None:
        """

        :param features: Collective targets and parameters information in the form of Definition class
        :type features: FeatureDefinition
        """
        self.lbs = list(features.lbs.values())
        self.ubs = list(features.ubs.values())
        self.nvar = features.nvar

    def __call__(self, n_samples: int = 50) -> ndarray:
        """

        :param n_samples: Number of samples to generate in the DoE.
        :type n_samples: int
        :return: The samples to be evaluated.
        :rtype: ndarray
        """
        samples = self._method(n_samples)
        return samples

    @abstractmethod
    def _method(self, n_samples: int = 50) -> ndarray:
        """

        Method defining the sampling strategy.

        :param n_samples: Number of samples to generate in the DoE.
        :type n_samples: int
        :return: The samples.
        :rtype: ndarray
        """
        pass


class Optimization(ABC):
    def __init__(
        self,
        objective: Callable[..., List[float]],
        features: FeatureDefinition,
        popsize: int = 10,
    ) -> None:
        self.objective = objective
        self.features = features
        self.popsize = popsize
        self.nvar = features.nvar
        self.nobj = sum(features.are_obj.values())
        self.n_ieq_constr = len([f for f in features.ineqs.values() if f is not None])
        self.lbs = list(features.lbs.values())
        self.ubs = list(features.ubs.values())
        self.ineqs = list(features.ineqs.values())

    def __call__(
        self,
        termination: Tuple[str, int],
    ) -> Dict[str, list]:
        """

        :return: Dictionary containing the optimized parameters and target values.
        :rtype: dict
        """

        problem = self._problem()
        algorithm = self._algorithm()

        res = minimize(
            problem,
            algorithm,
            termination=termination,
            seed=1,
            callback=HistCallback(),
            return_least_infeasible=True,
        )

        if not isinstance(res.X[0], Iterable):
            res.X = [res.X]

        results = {
            "x": res.X,
            "fmodel": res.F,
            "x_hist": concatenate(res.algorithm.callback.data["x_hist"]),
            "fmodel_hist": concatenate(res.algorithm.callback.data["fmodel_hist"]),
        }

        return results

    def _problem(self):
        return Problem(
            self.objective,
            self.nvar,
            self.nobj,
            self.n_ieq_constr,
            self.lbs,
            self.ubs,
            self.ineqs,
        )

    @abstractmethod
    def _algorithm(self):
        pass


class Problem(ElementwiseProblem):
    def __init__(
        self,
        objective: Callable[..., List[float]],
        nvar: int,
        nobj: int,
        n_ieq_constr: int,
        lbs: list,
        ubs: list,
        ineqs: list,
    ) -> None:

        self.objective = objective
        self.ineqs = ineqs

        super().__init__(
            n_var=nvar, n_obj=nobj, n_ieq_constr=n_ieq_constr, xl=lbs, xu=ubs
        )

    def _evaluate(self, x, out, *args, **kwargs) -> None:
        results = self.objective(x)

        g = [
            result - ineq
            for result, ineq in zip(results, self.ineqs)
            if ineq is not None
        ]

        out["F"] = results
        out["G"] = g


class HistCallback(Callback):
    def __init__(self) -> None:
        super().__init__()
        self.data["fmodel_hist"] = []
        self.data["x_hist"] = []

    def notify(self, algorithm):
        self.data["fmodel_hist"].append(algorithm.pop.get("F"))
        self.data["x_hist"].append(algorithm.pop.get("X"))
