import functools
from dataclasses import dataclass
from typing import Dict, List, Optional

from myccli.terraform import ETF
from myccli.terraform.common import ProviderRequirement, InlineBlock


@dataclass
class TerraformResourceLifecycle:
    create_before_destroy: Optional[bool] = None
    prevent_destroy: Optional[bool] = None

    def __bool__(self):
        return (self.create_before_destroy is not None) or (self.prevent_destroy is not None)

    def to_dict(self) -> dict:
        result = dict(
            create_before_destroy=self.create_before_destroy,
            prevent_destroy=self.prevent_destroy
        )

        result = {k: v for k, v in result.items() if v is not None}
        return result


class TerraformItem:
    def __init__(self, kind: str, tf_name: str):
        self._kind = kind
        self._tf_name = tf_name
        self._deps = []
        self.lifecycle = TerraformResourceLifecycle()

    @property
    def kind(self) -> str:
        return self._kind

    @property
    def tf_name(self) -> str:
        return self._tf_name

    @property
    def dependencies(self) -> List['TerraformItem']:
        return self._deps

    def get_args(self) -> Dict[str, any]:
        raise NotImplementedError

    def get_arg_ref(self, name: str) -> 'TerraformArgumentRef':
        return TerraformArgumentRef(self, name)

    def get_self_ref(self):
        raise NotImplementedError

    def add_dependency(self, other: 'TerraformItem'):
        self._deps.append(other)

    def required_providers(self) -> List[ProviderRequirement]:
        """ Returns a list of providers required by this resource. """
        return []


class TerraformResource(TerraformItem):
    pass


class TerraformDataSource(TerraformItem):
    pass


@dataclass
class TerraformArgumentRef(ETF):
    item: TerraformItem
    arg: str

    def render(self) -> str:
        result = f'{self.item.kind}.{self.item.tf_name}.{self.arg}'
        if isinstance(self.item, TerraformDataSource):
            return 'data.' + result
        return result


def basic_terraform_item(cls):
    """ Class decorator that creates Terraform resources/data sources from their annotations. """

    class BasicTerraformItem(cls):
        def __init__(self, tf_name: str, **kwargs):
            super().__init__(cls.__kind__, tf_name)

            self._kwargs = kwargs
            for key, value in self.__annotations__.items():
                if key not in self._kwargs:
                    # check for default value
                    arg_value = getattr(cls, key, None)
                    if value is not None:
                        self._kwargs[key] = arg_value
                    else:
                        raise ValueError(f'Terraform resource of type "{cls.__kind__}" missing required argument: "{key}"')
                else:
                    arg_value = self._kwargs[key]

                setattr(self, key, arg_value)

        def get_self_ref(self):
            raise NotImplementedError

        def get_args(self) -> Dict[str, any]:
            args = {}

            override_args_fn = getattr(self, 'override_args')
            override_args = override_args_fn() if override_args_fn is not None else {}

            keys = set(override_args.keys()) | set(self.__annotations__.keys())
            for key in keys:
                value = override_args.get(key, self._kwargs.get(key))
                if value is not None:
                    args[key] = value

            return args

    return BasicTerraformItem
