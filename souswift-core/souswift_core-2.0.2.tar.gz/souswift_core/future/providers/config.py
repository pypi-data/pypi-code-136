import typing
from types import NoneType

from pydantic.fields import FieldInfo, ModelField, Undefined

from souswift_core.future import config as future_config
from souswift_core.future import models

NOT_FOUND = object()

ProviderConfigT = typing.TypeVar('ProviderConfigT', bound='ProviderConfig')


class ProviderConfig(models.Model):
    _prefix_: str = ''
    _no_prefix_: typing.Sequence[str] = ()

    class Config(models.Model.Config):
        arbitrary_types_allowed = True
        alias_generator = str.upper


def from_env(
    cls: type[ProviderConfigT],
    __config__: future_config.ConfigLike = future_config.Config(),
    __ignore_none__: bool = True,
    **fields,
) -> ProviderConfigT:
    if __ignore_none__:
        fields = {
            key: value for key, value in fields.items() if value is not None
        }
    config_from_field = _config_getter(cls._prefix_, cls._no_prefix_)
    args = {
        field.name: config_from_field(field, __config__)
        for field in cls.__fields__.values()
        if field.name not in fields
    }
    return cls.parse_obj(args | fields)


def _config_getter(prefix: str, no_prefix: typing.Sequence[str]):
    def _config_from_field(
        field: ModelField, config: future_config.ConfigLike
    ):
        default = _get_default(field.field_info)
        type_, optional = _get_type(field.outer_type_)
        names = _get_env_names(field, prefix, no_prefix)
        if not optional:
            return _get_config(config, names, default, field.type_)
        value = _get_config(config, names, default)
        return type_(value) if value else None

    return _config_from_field


def _get_config(
    config: future_config.ConfigLike,
    names: tuple[str, str],
    default: typing.Any,
    cast: future_config.CastType = lambda a: a,
):
    main_name, fallback = names

    def _skip_key_error(name: str):
        try:
            value = config.get(name, cast=cast)
        except KeyError:
            return NOT_FOUND
        else:
            return value

    value, name_value = _skip_key_error(main_name), _skip_key_error(fallback)
    if value is not NOT_FOUND:
        return value
    if name_value is not NOT_FOUND:
        return name_value
    if default is not future_config.MISSING:
        return default
    return future_config.MissingNameError(main_name)


def _get_env_names(
    field: ModelField, prefix: str, no_prefix: typing.Sequence
) -> tuple[str, typing.Any]:
    def _get_env_name(name: str):
        if prefix and name not in no_prefix:
            name = f'{prefix.removesuffix("_")}_{name}'
        return name.upper()

    return _get_env_name(field.alias), _get_env_name(field.name)


def _get_default(field_info: FieldInfo):
    if field_info.default is not Undefined:
        return field_info.default
    if field_info.default_factory is not None:
        return field_info.default_factory()
    return future_config.MISSING


def _get_type(field_type: type) -> tuple[type, bool]:
    is_union = typing.get_origin(field_type) is typing.Union
    if not is_union:
        return field_type, False
    args = typing.get_args(field_type)
    if len(args) != 2 or args[1] is not NoneType:
        raise NotImplementedError(
            f'from env does not support non optional union: <{field_type!r}>'
        )
    return args[0], True
