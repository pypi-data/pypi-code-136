from typing import Dict, List

from myccli.terraform.common import InlineBlock, ProviderRequirement, ETFRaw
from myccli.terraform.resources.base import TerraformResource, TerraformDataSource


class TFBuildDockerImage(TerraformResource):
    def __init__(self, tf_name: str, *, name: str, context_path: str, tags: List[str]):
        super().__init__('docker_image', tf_name)
        self._name = name
        self._context_path = context_path
        self._tags = tags

    def get_self_ref(self):
        raise NotImplementedError

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self._name,
            'build': InlineBlock(
                path=self._context_path,
                tag=self._tags,
            ),
            'triggers': {
                'dir_sha1': ETFRaw(rf'sha1(join("", [for f in fileset("{self._context_path}", "**") : filesha1(join("/", ["{self._context_path}", f]))]))'),
            }
        }

    def required_providers(self) -> List[ProviderRequirement]:
        return [ProviderRequirement('docker')]


