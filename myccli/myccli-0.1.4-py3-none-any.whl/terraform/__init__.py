from myccli.terraform.common import ETF
from myccli.terraform.provider import TerraformProvider, TerraformProviderRegistry
from myccli.terraform.resources.aws import AWSTerraformResource
from myccli.terraform.resources.base import TerraformResource, TerraformItem
from myccli.terraform.writer import TerraformWriter

DEFAULT_MIN_TERRAFORM_VERSION = '1.2.0'


class TerraformFile:
    """
    Represents a terraform configuration file.
    """

    def __init__(self, all_provider_registry: TerraformProviderRegistry):
        self._provider_registry = all_provider_registry
        self._required_provider_registry = TerraformProviderRegistry()

        self._items = []
        self._data_sources = []

    def add_provider(self, p: TerraformProvider):
        self._required_provider_registry.add_provider(p)

    def add_item(self, item: TerraformItem):
        self._items.append(item)

        for req in item.required_providers():
            p = self._provider_registry.get_provider(req.name, req.version)
            if p is not None:
                self.add_provider(p)

        return item

    def dump(self, f):
        """
        Emits the Terraform config to a .tf file.
        """
        writer = TerraformWriter(f)

        writer.write_terraform_block(
            required_version=f'>= {DEFAULT_MIN_TERRAFORM_VERSION}',
            providers=list(self._required_provider_registry),
        )

        for p in self._required_provider_registry:
            writer.write_provider_block(p)

        for r in self._items:
            writer.write_item_block(r)
