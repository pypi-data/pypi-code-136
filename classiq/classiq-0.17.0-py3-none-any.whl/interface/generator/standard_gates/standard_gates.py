from typing import List, Optional

import pydantic
import sympy

from classiq.interface.generator import function_params
from classiq.interface.generator.arith.register_user_input import RegisterUserInput
from classiq.interface.generator.standard_gates.standard_angle_metaclass import (
    MyMetaAngledClassModel,
)

"""
To add new standard gates, refer to the following guide
https://docs.google.com/document/d/1Nt9frxnPkSn8swNpOQ983E95eaEiDWaiuWAKglGtUAA/edit#heading=h.e9g9309bzkxt
"""

_POSSIBLE_PARAMETERS: List[str] = ["theta", "phi", "lam"]
DEFAULT_STANDARD_GATE_ARG_NAME: str = "TARGET"


class _StandardGate(function_params.FunctionParams, metaclass=MyMetaAngledClassModel):  # type: ignore[misc]
    _name: str = ""
    _num_target_qubits: pydantic.PositiveInt = pydantic.PrivateAttr(default=1)
    _num_ctrl_qubits: Optional[pydantic.PositiveInt] = pydantic.PrivateAttr(
        default=None
    )

    @pydantic.validator("*", pre=True)
    def validate_parameters(cls, value, field: pydantic.fields.ModelField):
        if field.name in _POSSIBLE_PARAMETERS:
            if isinstance(value, str):
                sympy.parse_expr(value)

            if isinstance(value, sympy.Expr):
                return str(value)

        return value

    def _create_ios(self) -> None:
        argument = RegisterUserInput(
            name=DEFAULT_STANDARD_GATE_ARG_NAME,
            size=self._num_target_qubits,
        )
        self._inputs = {DEFAULT_STANDARD_GATE_ARG_NAME: argument}
        self._outputs = {DEFAULT_STANDARD_GATE_ARG_NAME: argument}

    @property
    def name(self):
        # this is removing the Gate suffix from the classes name
        return self._name or self.__class__.__name__[:-4].lower()

    @property
    def num_ctrl_qubit(self):
        return self._num_ctrl_qubits

    @property
    def num_target_qubits(self):
        return self._num_target_qubits

    def __init_subclass__(cls, angles: List[str] = None, **kwargs):
        super().__init_subclass__()


class XGate(_StandardGate):
    """
    creates a X gate
    """

    def get_power_order(self) -> int:
        return 2


class YGate(_StandardGate):
    """
    creates a Y gate
    """

    def get_power_order(self) -> int:
        return 2


class ZGate(_StandardGate):
    """
    create a Z gate
    """

    def get_power_order(self) -> int:
        return 2


class HGate(_StandardGate):
    """
    creates a Hadamard gate
    """

    def get_power_order(self) -> int:
        return 2


class IGate(_StandardGate):
    """
    creates the identity gate
    """

    _name: str = "id"

    def get_power_order(self) -> int:
        return 1


class SGate(_StandardGate):
    """
    Z**0.5
    """

    def get_power_order(self) -> int:
        return 4


class SdgGate(_StandardGate):
    """
    creates the inverse S gate
    """

    def get_power_order(self) -> int:
        return 4


class SXGate(_StandardGate):
    """
    X**0.5
    """

    def get_power_order(self) -> int:
        return 4


class SXdgGate(_StandardGate):
    """
    creates the inverse SX gate
    """

    def get_power_order(self) -> int:
        return 4


class TGate(_StandardGate):
    """
    Z**0.25
    """

    def get_power_order(self) -> int:
        return 8


class TdgGate(_StandardGate):
    """
    creates the inverse T gate
    """

    def get_power_order(self) -> int:
        return 8


class SwapGate(_StandardGate):
    """
    Swaps between two qubit states
    """

    _num_target_qubits: pydantic.PositiveInt = pydantic.PrivateAttr(default=2)

    def get_power_order(self) -> int:
        return 2


class iSwapGate(_StandardGate):  # noqa: N801
    """
    Swaps between two qubit states and add phase of i to the amplitudes of |01> and |10>
    """

    _num_target_qubits: pydantic.PositiveInt = pydantic.PrivateAttr(default=2)

    def get_power_order(self) -> int:
        return 4
