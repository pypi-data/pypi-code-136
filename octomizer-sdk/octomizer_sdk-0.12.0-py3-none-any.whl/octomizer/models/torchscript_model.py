"""A wrapper for Torchscript Models in the OctoML Platform."""
import re
import typing

from octomizer import client, model, project


class TorchscriptModel(model.Model):
    """Represents a Model in Torchscript format."""

    def __init__(
        self,
        client: client.OctomizerClient,
        name: str,
        model: typing.Optional[typing.Union[bytes, str]] = None,
        model_input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        model_input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.List[str]] = None,
        project: typing.Optional[project.Project] = None,
        timeout: int = model.DEFAULT_JOB_TIMEOUT_SECONDS,
    ):
        """Creates a new Torchscript model in the OctoML Platform.

        :param client: an instance of the OctoML client.
        :param name: the name of the model.
        :param model: The model bytes, or the name of a file containing the Torchscript model.
        :param model_input_shapes: The model's input shapes in key, value format. Note that input names
            must end with '__{input_index}', e.g. {"input__0": [1, 3, 224, 224], "input__1": [1, 3]}.
        :param model_input_dtypes: The model's input dtypes in key, value format. e.g. {"input__0": "float32", "input__1": "float32"}.
        :param description: a description of the model.
        :param labels: optional tags for the Model.
        :param project: the Project that this Model belongs to. Optional.
        """
        super().__init__(
            client=client,
            name=name,
            model=model,
            model_input_shapes=model_input_shapes,
            model_input_dtypes=model_input_dtypes,
            description=description,
            labels=labels,
            model_format="torchscript",
            project=project,
            timeout=timeout,
        )

    def _validate_inputs(
        self,
        model_input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]],
        model_input_dtypes: typing.Optional[typing.Dict[str, str]],
    ) -> None:
        super()._validate_inputs(model_input_shapes, model_input_dtypes)

        input_shape_name_re = re.compile(
            r"^(?!.*(?:__.+){2,})(?:[a-zA-Z0-9]+)(?:_[a-zA-Z0-9]+)*__(\d+)$"
        )

        if model_input_shapes is None:
            model_input_shapes = {}

        # We rely on Python 3.7+ guarantees that dict key orders are preserved.
        for (input_shape_idx, input_shape_name) in enumerate(model_input_shapes.keys()):
            match = re.fullmatch(input_shape_name_re, input_shape_name)

            if (
                match is None
                or len(match.groups()) != 1
                or str(input_shape_idx) != match[1]
            ):
                raise model.InvalidInputError(
                    f"input name '{input_shape_name}' must end with __{input_shape_idx}"
                )
