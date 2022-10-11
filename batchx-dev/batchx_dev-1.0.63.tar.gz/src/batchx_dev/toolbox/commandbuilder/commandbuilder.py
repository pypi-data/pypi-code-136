from ..parsers import Input, Manifest
from ..utils import FileSystem
from .actions import ActionMixin
from .constraints import ConstraintMixin
from .kinds import CommandKindMixin


class CommandBuilder(ActionMixin, ConstraintMixin, CommandKindMixin):
    def __init__(
        self,
        manifest: Manifest,
        tool: str = "toolname",
        filesystem: FileSystem | None = None,
        verbose=True,
        default_prefix="--",
        default_kind="keyval",
    ):

        self.tool = tool
        self.fs = filesystem if filesystem is not None else FileSystem(tool=tool)
        self.default_prefix = default_prefix
        self.default_kind = default_kind

        self.verbose = verbose
        self.manifest = manifest

        self.active_key = None

        self.kinds = dict(
            keyval=set([]), flag=set([]), argument=set([])
        )  # kind -> set of keys
        self.actions = dict()  # key -> list of actions
        self.commands = dict()  # key -> cmd str
        self.constraints = dict()  # key -> list of constraints
        return

    def add_command(
        self,
        cmd: str = "",
        key: str | None = None,
        prefix: str | None = None,
        kind: str | None = None,
    ):
        # assign defaults in absence of explicit values
        if key is None:
            key = self.active_key

        if prefix is None:
            prefix = self.default_prefix  # fallback on default

        if kind is None:
            kind = self.default_kind  # fallback on default

        # generate command part (i.e., a string) and add to dict
        self.commands[key] = "{prefix}{command}".format(prefix=prefix, command=cmd)

        self.active_key = key

        if kind is not None:
            return self.add_kind(kind=kind)
        else:
            return self

    def build_command(self, input: Input):
        return " ".join(self.get_cmd(input)).strip()

    # properties
    @property
    def manifest(self):
        return getattr(self, "_manifest", None)

    @manifest.setter
    def manifest(self, value):
        if isinstance(value, Manifest):
            self._manifest = value
        else:
            raise ValueError("manifest attribute only accepts Manifest object.")

    @property
    def fs(self):
        return getattr(self, "_fs", None)

    @fs.setter
    def fs(self, value):
        if isinstance(value, FileSystem):
            self._fs = value
        else:
            raise ValueError("fs attribute only accepts FileSystem object.")
