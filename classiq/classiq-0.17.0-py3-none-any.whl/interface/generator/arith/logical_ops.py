from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Union

import pydantic

from classiq.interface.generator.arith.arithmetic_operations import (
    ArithmeticOperationParams,
)
from classiq.interface.generator.arith.fix_point_number import FixPointNumber
from classiq.interface.generator.arith.register_user_input import RegisterUserInput

LogicalOpsArg = Union[RegisterUserInput, FixPointNumber, int, float]
DEFAULT_ARG_NAME = "in_arg"


class LogicalOps(ArithmeticOperationParams):
    args: List[LogicalOpsArg]
    target: Optional[RegisterUserInput]
    _should_invert_node_list: List[str] = pydantic.PrivateAttr(default_factory=list)

    def update_should_invert_node_list(self, invert_args: List[str]):
        self._should_invert_node_list.extend(invert_args)

    @pydantic.validator("output_size")
    def _validate_output_size(cls, output_size: Optional[int]) -> int:
        if output_size is not None and output_size != 1:
            raise ValueError("logical operation output size must be 1")
        return 1

    @pydantic.validator("args")
    def validate_inputs_sizes(cls, args):
        for arg in args:
            if isinstance(arg, RegisterUserInput) and (
                arg.size != 1 or arg.fraction_places != 0
            ):
                raise ValueError(
                    f"All inputs to logical and must be of size 1 | {arg.name}"
                )
        return args

    @pydantic.validator("args")
    def set_inputs_names(cls, args):
        for i, arg in enumerate(args):
            if isinstance(arg, RegisterUserInput):
                arg.name = arg.name if arg.name else DEFAULT_ARG_NAME + str(i)
        return args

    @pydantic.validator("target", always=True)
    def _validate_target(
        cls, target: Optional[RegisterUserInput], values: Dict[str, Any]
    ) -> Optional[RegisterUserInput]:
        if target:
            cls._assert_boolean_register(target)
            target.name = target.name or values.get("output_name", "")
        return target

    def _get_result_register(self) -> RegisterUserInput:
        return RegisterUserInput(size=1, name=self.output_name)

    def _create_ios(self) -> None:
        args = {
            arg.name: arg for arg in self.args if isinstance(arg, RegisterUserInput)
        }
        self._inputs = {**args}
        self._outputs = {**args, self.output_name: self.result_register}
        if self.target:
            self._inputs[self.target.name] = self.target

    @staticmethod
    def _assert_boolean_register(reg: RegisterUserInput) -> None:
        if reg.is_signed or (reg.size != 1) or (reg.fraction_places != 0):
            raise ValueError("Register doesn't match a boolean variable")

    def is_inplaced(self) -> bool:
        return False

    def get_params_inplace_options(self) -> Iterable[LogicalOps]:
        return ()

    class Config:
        arbitrary_types_allowed = True


class LogicalAnd(LogicalOps):
    output_name: str = "and"
    pass


class LogicalOr(LogicalOps):
    output_name: str = "or"
    pass
