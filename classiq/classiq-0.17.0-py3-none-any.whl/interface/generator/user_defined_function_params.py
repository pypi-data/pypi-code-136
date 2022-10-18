from typing import Mapping, Optional

import pydantic

from classiq.interface.generator.arith.register_user_input import RegisterUserInput
from classiq.interface.generator.function_params import FunctionParams


class CustomFunction(FunctionParams):
    """
    A user-defined custom function parameters object.
    """

    name: str = pydantic.Field(description="The name of a custom function")

    def generate_ios(
        self,
        inputs: Mapping[str, Optional[RegisterUserInput]],
        outputs: Mapping[str, Optional[RegisterUserInput]],
    ) -> None:
        self._inputs = dict(inputs)
        self._outputs = dict(outputs)
