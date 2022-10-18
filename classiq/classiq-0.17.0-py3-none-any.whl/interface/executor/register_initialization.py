from typing import Collection, Dict, Union

import pydantic

from classiq.interface.generator.arith.fix_point_number import FixPointNumber
from classiq.interface.generator.synthesis_metrics import MetricsRegister

from classiq.exceptions import ClassiqStateInitializationError

Number = Union[FixPointNumber, dict, float, int]


class RegisterInitialization(pydantic.BaseModel):
    register_data: MetricsRegister = pydantic.Field(
        description="The register information."
    )
    initial_condition: FixPointNumber = pydantic.Field(
        description="The initial state of the register ."
    )

    @pydantic.validator("initial_condition", pre=True)
    def _validate_initial_condition(cls, value) -> Union[FixPointNumber, dict]:
        if isinstance(value, (dict, FixPointNumber)):
            return value
        else:
            return FixPointNumber(float_value=value)

    @pydantic.root_validator()
    def _validate_register_initialization(cls, values: dict) -> dict:
        register_data: MetricsRegister = values["register_data"]
        initial_condition: FixPointNumber = values["initial_condition"]

        initial_condition_length = initial_condition.size
        register_length = len(register_data.qubit_indexes_absolute)
        if initial_condition_length > register_length:
            raise ClassiqStateInitializationError(
                f"Register {register_data.name} has {register_length} qubits, which is not enough to represent the number {initial_condition.float_value}."
            )
        return values

    @classmethod
    def initialize_registers(
        cls,
        registers: Collection[MetricsRegister],
        initial_conditions: Collection[Number],
    ) -> Dict[str, "RegisterInitialization"]:
        return {
            register.name: cls(
                register_data=register,
                initial_condition=initial_condition,
            )
            for register, initial_condition in zip(registers, initial_conditions)
        }
