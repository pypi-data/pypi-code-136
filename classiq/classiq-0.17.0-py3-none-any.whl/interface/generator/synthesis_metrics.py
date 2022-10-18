import enum
from typing import Callable, Dict, List, Optional, Union

import pydantic
from pydantic import BaseModel

ParameterName = str


class SynthesisStepDurations(BaseModel):
    preprocessing: Optional[float] = None
    solving: Optional[float] = None
    conversion_to_circuit: Optional[float] = None
    postprocessing: Optional[float] = None

    def total_time(self) -> float:
        return sum(
            time if time is not None else 0
            for time in (
                self.preprocessing,
                self.solving,
                self.conversion_to_circuit,
                self.postprocessing,
            )
        )


class MetricsRegisterRole(str, enum.Enum):
    INPUT = "input"
    OUTPUT = "output"
    AUXILIARY = "auxiliary"
    ZERO = "zero"


class MetricsRegister(BaseModel):
    role: MetricsRegisterRole
    name: str
    qubit_indexes_relative: List[int]
    qubit_indexes_absolute: List[int] = list()

    def __len__(self) -> int:
        return self.qubit_indexes_relative.__len__()

    @property
    def width(self) -> int:
        return len(self)


class FunctionMetrics(BaseModel):
    name: str
    registers: List[MetricsRegister] = list()
    depth: Optional[int]
    width: Optional[int]
    released_auxiliary_qubits: List[int] = list()

    def __getitem__(self, key: Union[int, str]) -> MetricsRegister:
        if type(key) is int:
            return self.registers[key]
        if type(key) is str:
            for register in self.registers:
                if key == register.name:
                    return register
        raise KeyError(key)

    def _update_registers(self, absolute_index_getter: Callable[[int], int]) -> None:
        for r in self.registers:
            r.qubit_indexes_absolute = list(
                map(absolute_index_getter, r.qubit_indexes_relative)
            )


class SynthesisMetrics(BaseModel):
    function_metrics: List[FunctionMetrics] = pydantic.Field(default_factory=list)
    topological_sort: Optional[List[str]]
    _function_mapping: Dict[Union[int, str], FunctionMetrics] = pydantic.PrivateAttr(
        default_factory=dict
    )
    circuit_parameters: List[ParameterName] = pydantic.Field(default_factory=list)
    failure_reason: Optional[str]
    step_durations: Optional[SynthesisStepDurations] = None
    width: Optional[int] = pydantic.Field(default=None)

    def _fill_function_mapping(self) -> None:
        if self._function_mapping:
            return
        for idx, fm in enumerate(self.function_metrics):
            self._function_mapping[idx] = fm
            self._function_mapping[fm.name] = fm

    def __getitem__(self, key: Union[int, str]) -> FunctionMetrics:
        self._fill_function_mapping()
        if key not in self._function_mapping:
            raise KeyError(f"No function named {key}")
        return self._function_mapping[key]

    def __len__(self) -> int:
        return self.function_metrics.__len__()

    def __iter__(self):
        if not self.topological_sort:
            return
        yield from (self[function_name] for function_name in self.topological_sort)

    def _update_registers(self, qubit_absolute_indexes: Dict[str, List[int]]) -> None:
        for fm in self.function_metrics:
            absolute_index_getter = qubit_absolute_indexes[fm.name].__getitem__
            fm._update_registers(absolute_index_getter)

    def pprint(self) -> None:
        print("Circuit Synthesis Metrics")
        if self.step_durations is not None:
            print(f"    Generation took {self.step_durations.total_time()} seconds")
        if self.failure_reason:
            print("Generation failed :(")
            print(f"Failure reason: {self.failure_reason}")
            return
        print(f"The circuit has {len(self.function_metrics)} functions:")
        for index, fm in enumerate(self.function_metrics):
            print(f"{index}) {fm.name}")
            print(
                f"  depth: {fm.depth} ; "
                f"width: {fm.width} ; "
                f"registers: {len(fm.registers)}"
            )
            for reg_index, register in enumerate(fm.registers):
                print(
                    f"  {reg_index}) {register.role.value} - {register.name} ; "
                    f"qubits: {register.qubit_indexes_absolute}"
                )
