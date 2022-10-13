from pathlib import Path


from .dotdict import DotDict
from .json_mixin import JSONLoaderMixin
from .readme_mixin import ReadMeMixin


class Manifest(DotDict, JSONLoaderMixin, ReadMeMixin):
    def __init__(self, manifest_fp: str | Path, jsonpaths: bool = False):
        self.fp = manifest_fp
        self.load()  # ensures existence of self.json attribute
        super().__init__(self.json, name="Manifest", jsonpaths=jsonpaths)
        return

    # PARAMETERS
    @property
    def parameters(self):
        return {**self.inputs, **self.outputs}

    # INPUTS
    @property
    def inputs(self):
        return self.schema.input.properties  # shortcut

    @property
    def required_inputs(self) -> list[str]:
        return [
            i
            for i in self.input_names
            if (
                (getattr(self.inputs, i).required)
                or (i in getattr(self.schema.input, "required", []))
            )
        ]

    @property
    def optional_inputs(self) -> list[str]:
        return [i for i in self.input_names if i not in self.required_inputs]

    @property
    def input_names(self):
        return self.inputs.keys()

    @property
    def default_inputs(self):
        return {k: v.get("default", None) for k, v in self.inputs.items()}

    # OUTPUTS
    @property
    def outputs(self):
        return self.schema.output.properties  # shortcut

    @property
    def required_outputs(self):
        return [
            o
            for o in self.output_names
            if (
                (getattr(self.outputs, o).required)
                or (o in getattr(self.schema.output, "required", []))
            )
        ]

    @property
    def optional_outputs(self):
        return [o for o in self.output_names if o not in self.required_outputs]

    @property
    def output_names(self):
        return self.outputs.keys()

    @property
    def default_outputs(self):
        return {k: v.get("default", None) for k, v in self.outputs.items()}

    # PIPELINE
    @property
    def is_pipeline(self):
        return self.pipeline is not None

    @property
    def sample(self):
        if self.is_pipeline:
            return self.schema.input.properties.sample.properties  # shortcut
        else:
            return None

    @property
    def tools(self):
        if self.is_pipeline:
            return self.schema.input.properties.tools.properties  # shortcut
        else:
            return None
