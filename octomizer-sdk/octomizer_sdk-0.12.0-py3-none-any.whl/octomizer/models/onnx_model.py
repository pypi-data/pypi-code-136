"""A wrapper for ONNX Models in the OctoML Platform."""
import typing

from octomizer import client, model, project


class ONNXModel(model.Model):
    """Represents a Model in ONNX format."""

    def __init__(
        self,
        client: client.OctomizerClient,
        name: str,
        model: typing.Optional[typing.Union[bytes, str]] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.List[str]] = None,
        project: typing.Optional[project.Project] = None,
        timeout: int = model.DEFAULT_JOB_TIMEOUT_SECONDS,
    ):
        """Creates a new ONNX model in the OctoML Platform.

        :param client: an instance of the OctoML client.
        :param name: the name of the model.
        :param model: The model in ONNX ModelProto format, or the name of
            a file containing the ONNX model.
        :param input_shapes: optional dict mapping input name to shape.
        :param input_dtypes: optional dict mapping input name to dtype.
        :param description: a description of the model.
        :param labels: optional tags for the Model.
        :param project: the Project that this Model belongs to. Optional.
        """
        super().__init__(
            client=client,
            name=name,
            model=model,
            description=description,
            labels=labels,
            model_format="onnx",
            project=project,
            timeout=timeout,
        )
