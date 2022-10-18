from typing import List, Tuple, Union

import pydantic
from typing_extensions import Literal

from classiq.interface.finance.function_input import FinanceFunctionInput
from classiq.interface.finance.gaussian_model_input import GaussianModelInput
from classiq.interface.finance.model_input import FinanceModelInput
from classiq.interface.generator import function_params
from classiq.interface.generator.arith.register_user_input import RegisterUserInput
from classiq.interface.generator.function_params import ParamMetadata

DEFAULT_OUT_NAME = "out"


class Finance(function_params.FunctionParams):
    model: FinanceModelInput = pydantic.Field(description="Load a financial model")
    finance_function: Union[FinanceFunctionInput] = pydantic.Field(
        description="The finance function to solve the model"
    )

    def get_metadata(self) -> "FinanceMetadata":
        return FinanceMetadata(**self.dict())

    def _create_ios(self) -> None:
        self._inputs = dict()
        self._outputs = {
            DEFAULT_OUT_NAME: RegisterUserInput(
                name=DEFAULT_OUT_NAME, size=self.model.params.num_model_qubits
            )
        }


class FinanceMetadata(ParamMetadata, Finance):
    metadata_type: Literal["finance"] = "finance"


class FinanceModelMetadata(ParamMetadata):
    metadata_type: Literal["finance_model"] = "finance_model"
    num_model_qubits: int
    distribution_range: List[float]


DEFAULT_INPUT_NAME = "in"
DEFAULT_OUTPUT_NAME = "out"
DEFAULT_BERNOULLI_OUTPUT_NAME = "bernoulli_random_variables"


class FinanceModels(function_params.FunctionParams):
    model: FinanceModelInput = pydantic.Field(description="Load a financial model")

    def _create_ios(self) -> None:
        self._inputs = {
            DEFAULT_INPUT_NAME: RegisterUserInput(
                name=DEFAULT_INPUT_NAME, size=self.get_metadata().num_model_qubits
            )
        }
        self._outputs = {
            DEFAULT_OUTPUT_NAME: RegisterUserInput(
                name=DEFAULT_OUTPUT_NAME, size=self.model.params.num_output_qubits
            )
        }
        if isinstance(self.model.params, GaussianModelInput):
            self._outputs[DEFAULT_BERNOULLI_OUTPUT_NAME] = RegisterUserInput(
                name=DEFAULT_BERNOULLI_OUTPUT_NAME,
                size=self.model.params.num_bernoulli_qubits,
            )

    def get_metadata(self) -> FinanceModelMetadata:
        return FinanceModelMetadata(
            num_model_qubits=self.model.params.num_model_qubits,
            distribution_range=self.model.params.distribution_range,
        )


class FinancePayoff(function_params.FunctionParams):
    finance_function: FinanceFunctionInput = pydantic.Field(
        description="The finance function to solve the model"
    )
    num_qubits: pydantic.PositiveInt
    distribution_range: Tuple[float, float]

    def _create_ios(self) -> None:
        self._inputs = {
            DEFAULT_INPUT_NAME: RegisterUserInput(
                name=DEFAULT_INPUT_NAME, size=self.num_qubits
            )
        }
        self._outputs = {
            DEFAULT_OUTPUT_NAME: RegisterUserInput(name=DEFAULT_OUTPUT_NAME, size=1),
            DEFAULT_INPUT_NAME: RegisterUserInput(
                name=DEFAULT_INPUT_NAME, size=self.num_qubits
            ),
        }
