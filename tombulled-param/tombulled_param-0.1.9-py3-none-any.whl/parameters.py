from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional, Set, Union

from pydantic.fields import FieldInfo, Undefined, UndefinedType

from .typing import Supplier


class BaseParam(FieldInfo):
    def has_default(self) -> bool:
        return self.default is not Undefined or self.default_factory is not None

    def get_default(self) -> Any:
        if self.default_factory is not None:
            return self.default_factory()
        else:
            return self.default


@dataclass(init=False)
class Param(BaseParam):
    default: Union[Any, UndefinedType]
    default_factory: Optional[Supplier[Any]]
    alias: Optional[str]
    title: Optional[str]
    description: Optional[str]
    exclude: Union[Set[Union[int, str]], Mapping[Union[int, str], Any], Any]
    include: Union[Set[Union[int, str]], Mapping[Union[int, str], Any], Any]
    const: Optional[bool]
    gt: Optional[float]
    ge: Optional[float]
    lt: Optional[float]
    le: Optional[float]
    multiple_of: Optional[float]
    allow_inf_nan: Optional[bool]
    max_digits: Optional[int]
    decimal_places: Optional[int]
    min_items: Optional[int]
    max_items: Optional[int]
    unique_items: Optional[bool]
    min_length: Optional[int]
    max_length: Optional[int]
    allow_mutation: bool
    regex: Optional[str]
    discriminator: Optional[str]
    repr: bool
    extra: Dict[str, Any]

    def __init__(
        self,
        default: Union[Any, UndefinedType] = Undefined,
        *,
        default_factory: Optional[Supplier[Any]] = None,
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        exclude: Union[Set[Union[int, str]], Mapping[Union[int, str], Any], Any] = None,
        include: Union[Set[Union[int, str]], Mapping[Union[int, str], Any], Any] = None,
        const: Optional[bool] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        multiple_of: Optional[float] = None,
        allow_inf_nan: Optional[bool] = None,
        max_digits: Optional[int] = None,
        decimal_places: Optional[int] = None,
        min_items: Optional[int] = None,
        max_items: Optional[int] = None,
        unique_items: Optional[bool] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allow_mutation: bool = True,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        repr: bool = True,
        **extra: Any,
    ):
        super().__init__(
            default,
            default_factory=default_factory,
            alias=alias,
            title=title,
            description=description,
            exclude=exclude,
            include=include,
            const=const,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            multiple_of=multiple_of,
            allow_inf_nan=allow_inf_nan,
            max_digits=max_digits,
            decimal_places=decimal_places,
            min_items=min_items,
            max_items=max_items,
            unique_items=unique_items,
            min_length=min_length,
            max_length=max_length,
            allow_mutation=allow_mutation,
            regex=regex,
            discriminator=discriminator,
            repr=repr,
            **extra,
        )
