from typing import Collection, Dict, Iterator, List

from classiq.interface.executor.register_initialization import Number
from classiq.interface.generator.synthesis_metrics import (
    FunctionMetrics,
    MetricsRegister,
)

from classiq.exceptions import ClassiqStateInitializationError

RegisterName = str
InitialConditions = Dict[RegisterName, Number]


def get_registers_from_function_metrics(
    function_metrics: List[FunctionMetrics], register_names: Collection[RegisterName]
) -> List[MetricsRegister]:
    registers: List[MetricsRegister] = list()
    remain_register = list(register_names)

    for register in _relevant_registers(
        function_metrics=function_metrics, remain_register=remain_register
    ):
        registers.append(register)
        remain_register.remove(register.name)
        if not remain_register:
            return registers

    raise ClassiqStateInitializationError(
        f"The circuit doesn't contain registers that match: {', '.join(remain_register)}."
    )


def _relevant_registers(
    function_metrics: List[FunctionMetrics], remain_register: List[RegisterName]
) -> Iterator[MetricsRegister]:
    return iter(
        register
        for function_metric in function_metrics
        for register in function_metric.registers
        if register.name in remain_register
    )
