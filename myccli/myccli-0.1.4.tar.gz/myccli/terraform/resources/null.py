from typing import List, Dict

from myccli.terraform import TerraformResource
from myccli.terraform.common import ProviderRequirement, InlineBlock, TaggedInlineBlock


class TFNull(TerraformResource):
    """ Null resource. """
    def __init__(self, tf_name: str, *, commands: List[str] = None):
        super().__init__('null_resource', tf_name)
        self.commands = commands or []
        self._triggers = {}

    def get_self_ref(self):
        raise NotImplementedError

    def required_providers(self) -> List[ProviderRequirement]:
        return [ProviderRequirement('null')]

    def add_trigger(self, name: str, value: any):
        assert name not in self._triggers
        self._triggers[name] = value

    def get_args(self) -> Dict[str, any]:
        args = {}

        if self.commands:
            args['provisioner'] = [
                TaggedInlineBlock(tags=['local-exec'], block=InlineBlock(command=command))
                for command in self.commands
            ]

        if self._triggers:
            args['triggers'] = self._triggers

        return args
