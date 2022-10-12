import typing

from octoml.octomizer.v1 import model_inputs_pb2


def inputs_to_input_proto(
    input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
    input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
) -> model_inputs_pb2.ModelInputs:
    """Constructs ModelInputs message from input_shapes, input_dtypes dicts

    :param input_shapes: optional dict of input name to input shape.
    :param input_dtypes: optional dict of input name to input dtype.
    :return: ModelInputs proto constructed from the input dicts.
    """

    input_fields = []
    input_shapes = input_shapes or {}
    input_dtypes = input_dtypes or {}
    for iname, ishape in input_shapes.items():
        idtype = input_dtypes.get(iname)
        input_fields.append(
            model_inputs_pb2.InputField(
                input_name=iname,
                input_shape=ishape,
                input_dtype=idtype,
            )
        )
    model_inputs = model_inputs_pb2.ModelInputs(input_fields=input_fields)
    return model_inputs


def inputs_are_valid(
    input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]],
    input_dtypes: typing.Optional[typing.Dict[str, str]],
) -> typing.Optional[str]:
    """Returns None when this model's inputs are valid, otherwise returns
    a message indicating what updates are necessary to fix the inputs.
    """
    if not input_shapes:
        return "No input_shapes provided"
    if not input_dtypes:
        return "No input_dtypes provided"
    if len(input_shapes) != len(input_dtypes):
        return "Number of entries in input_shapes doesn't match input_dtypes"
    for iname, ishape in input_shapes.items():
        if not all(dim >= 0 for dim in ishape):
            return f"-1 values in the shape for input '{iname}' require disambiguation"
        elif iname not in input_dtypes:
            return f"input '{iname}' present in input_shapes but not input_dtypes"
    return None


def inputs_are_dynamic(
    input_shapes: typing.Dict[str, typing.List[int]],
) -> bool:
    """Returns True if inputs are dynamic, i.e. at least one shape is -1."""
    dynamic = False
    for ishape in input_shapes.values():
        if any(dim == -1 for dim in ishape):
            dynamic = True
    return dynamic
