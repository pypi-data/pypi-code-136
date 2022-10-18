from typing import Any, List


class ModelStringManager(object):
    def __init__(self, delimeter: str = ".", equals_sign: str = "=") -> None:
        self.delimeter = delimeter
        self.equals_sign = equals_sign

    def _parameter_setting_to_string(self, name: str, value: Any) -> str:
        return f"{name}{self.equals_sign}{value}"

    def parse_model_string(self, model_string: str) -> dict:
        parameters = {}
        for paramsetting in model_string.split(self.delimeter):
            parameter, parameter_value = paramsetting.split(self.equals_sign)
            parameters[parameter] = parameter_value
        return parameters

    def make_model_string(self, parameters: dict) -> str:
        parameter_names = list(parameters.keys())
        parameter_names.sort()  # make order predicable
        names_and_values: List[str] = []
        for parameter_name in parameter_names:
            portion_of_model_string = self._parameter_setting_to_string(
                name=parameter_name, value=parameters[parameter_name]
            )
            names_and_values.append(portion_of_model_string)
        return self.delimeter.join(names_and_values)


if __name__ == "__main__":
    mgr = ModelStringManager()
    params = {"k": 4, "z": 4}
    model: str = mgr.make_model_string(params)
    params_recovered = mgr.parse_model_string(model)
    for k, v in params_recovered.items():
        assert k in params
        assert str(params[k]) == str(v)
