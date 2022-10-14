from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Dict, List, Tuple, Union, Optional

import numpy as np
import pandas as pd


@dataclass
class Evaluation:
    """Schema for results of evaluating solutions.

    Attributes
        energy (List[float]): a list of values of energy.
        objective (Optional[List[float]], optional): a list of values of objective function. Defaults to None.
        constraint_violations (Optional[Dict[str, List[float]]], optional): a list of constraint violations. A key is the name of a constraint. A value is cost of a constraint. Defaults to None.
        penalty (Optional[Dict[str, List[float]]], optional): a list of costs of penalty terms. A key is the name of a penalty. A value is cost of a penalty term. Defaults to None.
    """

    energy: Optional[List[float]] = None
    objective: Optional[List[float]] = None
    constraint_violations: Optional[Dict[str, List[float]]] = None
    penalty: Optional[Dict[str, List[float]]] = None

    def __getitem__(
        self, item: Union[int, slice, List[int], Tuple[int], np.ndarray]
    ) -> Evaluation:
        """Perform the operation __getitem__.

        Args:
            item (Union[int, slice, List[int], Tuple[int], np.ndarray]): Index of evaluation metrics.

        Returns:
            Evaluation: Evaluation object.
        """

        def _slice(start: int, stop: int, step: Optional[int] = None) -> Evaluation:
            energy = None if self.energy is None else self.energy[start:stop:step]
            objective = (
                None if self.objective is None else self.objective[start:stop:step]
            )
            constraint_violations = (
                None
                if self.constraint_violations is None
                else {
                    label: constraint_violations[start:stop:step]
                    for label, constraint_violations in self.constraint_violations.items()
                }
            )
            penalty = (
                None
                if self.penalty is None
                else {
                    label: penalty[start:stop:step]
                    for label, penalty in self.penalty.items()
                }
            )
            return Evaluation(
                energy=energy,
                objective=objective,
                constraint_violations=constraint_violations,
                penalty=penalty,
            )

        if isinstance(item, int):
            start, stop, step = item, item + 1, None
            return _slice(start, stop, step)
        elif isinstance(item, slice):
            start, stop, step = item.start, item.stop, item.step
            return _slice(start, stop, step)
        elif isinstance(item, (list, tuple, np.ndarray)):
            item = np.array(item) if len(item) else np.array([], dtype=int)
            if item.dtype == int or item.dtype == bool:
                energy = (
                    None
                    if self.energy is None
                    else np.array(self.energy)[item].tolist()
                )
                objective = (
                    None
                    if self.objective is None
                    else np.array(self.objective)[item].tolist()
                )
                constraint_violations = (
                    None
                    if self.constraint_violations is None
                    else {
                        label: np.array(constraint_violations)[item].tolist()
                        for label, constraint_violations in self.constraint_violations.items()
                    }
                )
                penalty = (
                    None
                    if self.penalty is None
                    else {
                        label: np.array(penalty)[item].tolist()
                        for label, penalty in self.penalty.items()
                    }
                )
                return Evaluation(
                    energy=energy,
                    objective=objective,
                    constraint_violations=constraint_violations,
                    penalty=penalty,
                )
            else:
                raise IndexError(f'Element of "{item}" must be int or bool.')
        else:
            raise IndexError(
                f'Type of index "{item}" must be int or slice or List[int] or Tuple[int] or 1d numpy.ndarray.'
            )

    def to_pandas_dataframe(self) -> pd.DataFrame:
        """Convert Evaluation object to pandas.DataFrame object.

        Returns:
            pandas.DataFrame: pandas.DataFrame object.
        """

        evaluation = asdict(self)

        if evaluation["constraint_violations"]:
            constraint_violations = {
                f"constraint_violation[{k}]": v
                for k, v in evaluation.pop("constraint_violations").items()
            }
        else:
            constraint_violations = {}
            del evaluation["constraint_violations"]

        if self.penalty:
            penalty = {f"penalty[{k}]": v for k, v in evaluation.pop("penalty").items()}
        else:
            penalty = {}
            del evaluation["penalty"]

        evaluation |= constraint_violations | penalty
        return pd.DataFrame(evaluation)

    @classmethod
    def from_serializable(cls, obj: dict):
        """To Evaluation object from Dict of SampleSet.

        Args:
            obj (Dict): Dict of Evaluation.

        Returns:
            Evaluation: Evaluation obj.
        """

        return cls(
            energy=obj.get("energy"),
            objective=obj.get("objective"),
            constraint_violations=obj.get("constraint_violations"),
            penalty=obj.get("penalty"),
        )

    def to_serializable(self):
        return asdict(self)

    def _extend(self, other):
        # Concatenate energy
        self.energy.extend(other.energy)

        # Concatenate objective
        if isinstance(other.objective, list):
            self.objective.extend(other.objective)

        # Concatenate constraint_violations
        if isinstance(other.constraint_violations, dict):
            for (
                con_label,
                constraint_violation,
            ) in other.constraint_violations.items():
                self.constraint_violations[con_label].extend(constraint_violation)

        # Concatenate penalty
        if isinstance(other.penalty, list):
            self.penalty.extend(other.penalty)
