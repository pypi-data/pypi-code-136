import abc
import functools
import inspect
import typing

from aws_cdk import App, Stack, Tags
from constructs import Construct

from cdk_resources.utils import (
    combine_configurations,
    app_context,
    get_environment,
)


__all__ = ["Resource", "ResourceType", "ResourceTagMixin"]


ResourceType = typing.TypeVar("ResourceType")


class Resource(typing.Generic[ResourceType], abc.ABC):
    """ """

    # Main Construct (Required)
    @classmethod
    @abc.abstractmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> ResourceType:
        pass

    # Environment Props
    environment_props = None

    def __new__(
        cls,
        scope: typing.Optional[Stack] = None,
        construct_id: typing.Optional[str] = None,
        force_lookup: bool = False,
        **kwargs,
    ) -> ResourceType:
        if hasattr(cls, "construct_cache") and force_lookup is False:
            return cls
        scope = scope or app_context["current_stack"]
        assert isinstance(scope, Stack), "Scope is required"
        assert isinstance(construct_id, str), "construct_id is required"
        construct = cls.create(scope, construct_id, **kwargs)
        setattr(cls, "construct_cache", construct)
        return cls

    @classmethod
    def get(cls) -> ResourceType:
        construct_cache = getattr(cls, "construct_cache", None)
        assert construct_cache is not None, f"{cls} has not being initializated"
        return construct_cache

    @classmethod
    def create(cls, scope: Stack, construct_id: str, **kwargs) -> ResourceType:
        kwargs = dict(scope=scope, id=construct_id, **kwargs)
        # Environment Props
        environment_props = cls.get_environment_props()
        cls.pre_create(environment_props)
        kwargs.update(environment_props)
        # Create
        environment_construct = getattr(
            cls, f"construct_{cls.environment}", None
        )
        construct_method = (
            environment_construct
            if callable(environment_construct)
            else cls.construct
        )
        construct = construct_method(**kwargs)
        # Post Create
        cls.post_create(construct)
        return construct

    @classmethod
    def get_environment_props(cls) -> dict:
        environment_props = cls.environment_props or {}
        if callable(environment_props):
            environment_props = environment_props()
        environment_props = combine_configurations(environment_props)
        return environment_props

    @classmethod
    def pre_create(cls, environment_props: dict) -> None:
        pass

    @classmethod
    def post_create(cls, construct: ResourceType) -> None:
        pass

    @classmethod
    @property
    def environment(cls):
        return get_environment()


class ResourceTagMixin:
    construct_tags = None

    @classmethod
    def post_create(cls, construct: ResourceType) -> None:
        super().post_create(construct)
        for key, value in cls.construct_tags or []:
            value = value if isinstance(value, str) else value()
            Tags.of(construct).add(key, value)
