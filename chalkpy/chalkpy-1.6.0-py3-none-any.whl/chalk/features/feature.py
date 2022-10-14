from __future__ import annotations

import collections.abc
import copy
import dataclasses
import types
from datetime import datetime, timedelta
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

from sqlalchemy.types import TypeEngine

from chalk.utils.collection_type import GenericAlias
from chalk.utils.collections import ensure_tuple, get_unique_item
from chalk.utils.duration import Duration

if TYPE_CHECKING:
    from chalk.features.dataframe import DataFrame


U = TypeVar("U")
JsonValue = TypeVar("JsonValue")


class FeatureTypeAnnotation:
    def __init__(
        self,
        features_cls: Optional[Type[Features]] = None,
        attribute_name: Optional[str] = None,
        *,
        underlying: Optional[type] = None,
    ) -> None:
        # Either pass in the underlying -- if it is already parsed -- or pass in the feature cls and attribute name
        self._features_cls = features_cls
        self._attribute_name = attribute_name
        self._is_nullable: Optional[bool] = None
        self._is_dataframe: Optional[bool] = None
        self._collection_type: Optional[GenericAlias] = None
        self._is_scalar: Optional[bool] = None
        self._underlying = None
        self._parsed_annotation = None
        if underlying is not None:
            if features_cls is not None and attribute_name is not None:
                raise ValueError("If specifying the underlying, do not specify (features_cls, attribute_name)")
            self._parse_type(underlying)
        else:
            if features_cls is None or attribute_name is None:
                raise ValueError(
                    "If not specifying the underlying, then both the (features_cls, attribute_name) must be provided"
                )
        # Store the class and attribute name so we can later use typing.get_type_hints to
        # resolve any forward references in the type annotations
        # Resolution happens lazily -- after everything is imported -- to avoid circular imports

    @property
    def is_parsed(self) -> bool:
        return self._underlying is not None

    @property
    def annotation(self) -> Union[str, type]:
        """Return the type annotation, without parsing the underlying type if it is not yet already parsed."""
        if self._parsed_annotation is not None:
            # It is already parsed. Return it.
            return self._parsed_annotation
        assert self._features_cls is not None
        assert self._attribute_name is not None
        return self._features_cls.__annotations__[self._attribute_name]

    @property
    def parsed_annotation(self) -> type:
        """The parsed type annotation. It will be parsed if needed.

        Unlike :attr:`underlying`, parsed annotation contains any container or optional types, such as
        list, dataframe, or Optional.
        """
        if self._parsed_annotation is None:
            self._parse_annotation()
        assert self._parsed_annotation is not None
        return self._parsed_annotation

    def __str__(self):
        if isinstance(self.annotation, type):
            return self.annotation.__name__
        else:
            return str(self.annotation)

    def _parse_annotation(self):
        assert self._features_cls is not None
        assert self._attribute_name is not None
        hints = get_type_hints(self._features_cls)
        parsed_annotation = hints[self._attribute_name]
        self._parse_type(parsed_annotation)

    def _parse_type(self, annotation: Optional[type]):
        from chalk.features.dataframe import DataFrame

        assert self._parsed_annotation is None, "The annotation was already parsed"
        self._parsed_annotation = annotation
        origin = get_origin(annotation)
        self._is_nullable = False
        if self._features_cls is not None and self._attribute_name is not None:
            # Return a more helpful error message, since we have context
            error_ctx = f" {self._features_cls.__name__}.{self._attribute_name}"
        else:
            error_ctx = ""
        if origin in (
            Union,
            getattr(types, "UnionType", Union),
        ):  # using getattr as UnionType was introduced in python 3.10
            args = get_args(annotation)
            # If it's a union, then the only supported union is for nullable features. Validate this
            if len(args) != 2 or (None not in args and type(None) not in args):
                raise TypeError(
                    f"Invalid annotation for feature{error_ctx}: Unions with non-None types are not allowed"
                )
            annotation = args[0] if args[1] in (None, type(None)) else args[1]
            self._is_nullable = True

        # The only allowed collections here are Set, List, or DataFrame
        if origin in (set, Set):
            args = get_args(annotation)
            assert len(args) == 1, "typing.Set takes just one arg"
            annotation = args[0]
            self._collection_type = Set[annotation]

        if origin in (list, List):
            args = get_args(annotation)
            assert len(args) == 1, "typing.List takes just one arg"
            annotation = args[0]
            self._collection_type = List[annotation]

        self._is_dataframe = False
        if annotation is not None and issubclass(annotation, DataFrame):
            self._is_dataframe = True
            # For features, annotations like DataFrame[User.id] are not allowed
            # Annotations like these are only allowed in resolvers
            # So, error here.
            # if annotation.references_feature_set is None:
            #     raise TypeError("DF has no underlying type")
            annotation = annotation.references_feature_set

        self._is_scalar = annotation is not None and not issubclass(annotation, Features)

        if self._collection_type is not None and not self._is_scalar:
            raise TypeError(
                f"Invalid type annotation for feature {error_ctx}: "
                f"{str(self._collection_type)} must be of scalar types, "
                f"not {self._parsed_annotation}"
            )
        if self._is_dataframe and self._is_scalar:
            raise TypeError(
                f"Invalid type annotation for feature{error_ctx}: Dataframes must be of Features types, not {self._parsed_annotation}"
            )

        self._underlying = annotation

    @property
    def is_nullable(self) -> bool:
        """Whether the type annotation is nullable."""
        if self._parsed_annotation is None:
            self._parse_annotation()
        assert self._is_nullable is not None
        return self._is_nullable

    @property
    def underlying(self) -> type:
        """The underlying type annotation from the annotation."""
        if self.parsed_annotation is None:
            self._parse_annotation()
        if self._underlying is None:
            raise TypeError("There is no underlying type")
        return self._underlying

    @underlying.setter
    def underlying(self, underlying: Optional[type]):
        self._underlying = underlying

    @property
    def is_dataframe(self) -> bool:
        """Whether the type annotation is a dataframe."""
        if self._parsed_annotation is None:
            self._parse_annotation()
        assert self._is_dataframe is not None
        return self._is_dataframe

    @property
    def collection_type(self) -> Optional[GenericAlias]:
        if self._parsed_annotation is None:
            self._parse_annotation()
        return self._collection_type

    @property
    def is_scalar(self) -> bool:
        """Whether the type annotation is a scalar type (i.e. not a Features type)."""
        if self._parsed_annotation is None:
            self._parse_annotation()
        assert self._is_scalar is not None
        return self._is_scalar


@dataclasses.dataclass
class HasOnePathObj:
    parent: Feature
    child: Feature
    parent_to_child_attribute_name: str


class FeatureWrapper:
    """
    FeatureWrapper emulates DataFrames and
    nested has-one relationships when used
    as a type annotation or within a filter.
    """

    # def __call__(self, *args, **kwargs):
    #     # Only Windowed[T] should invoke call
    #     #   class User:
    #     #     logins: Windowed[int] = windowed("10m")
    #     #
    #     #   def fn(x: User.logins("10m")) -> ...
    #     return self._chalk_feature.typ.underlying(*args, **kwargs)

    def __init__(self, feature: Feature) -> None:
        # Binding as a private variable as not to have naming conflicts user's use of __getattr__
        self._chalk_feature = feature

    def __hash__(self):
        return hash(self._chalk_feature)

    def __gt__(self, other: object):
        return Filter(self._chalk_feature, ">", other)

    def __ge__(self, other: object):
        return Filter(self._chalk_feature, ">=", other)

    def __lt__(self, other: object):
        return Filter(self._chalk_feature, "<", other)

    def __le__(self, other: object):
        return Filter(self._chalk_feature, "<=", other)

    def _cmp(self, op: str, other: object):
        if isinstance(other, Feature):
            # If comparing against a feature directly, then we know it's not being used in a join condition
            # Since join conditions would be against another FeatureWrapper or a literal value
            is_eq = self._chalk_feature == other
            # They are the same feature. Short-circuit and return a boolean
            if op == "==" and is_eq:
                return True
            if op == "!=" and not is_eq:
                return False
            return NotImplemented  # GT / LT doesn't really make sense otherwise
        return Filter(self._chalk_feature, op, other)

    def __ne__(self, other: object):
        return self._cmp("!=", other)

    def __eq__(self, other: object):
        return self._cmp("==", other)

    def __and__(self, other: object):
        return self._cmp("and", other)

    def __or__(self, other: object):
        return self._cmp("or", other)

    def __repr__(self):
        return f"FeatureWrapper(fqn={self._chalk_feature.namespace}.{self._chalk_feature.name}, typ={self._chalk_feature.typ})"

    def __str__(self):
        return str(self._chalk_feature)

    def in_(self, examples: Iterable):
        return self._cmp("in", examples)

    def __getitem__(self, item: Any):
        from chalk.features.dataframe import DataFrame

        if self._chalk_feature.typ is not None and issubclass(self._chalk_feature.typ.parsed_annotation, DataFrame):
            f_copy = FeatureWrapper(copy.copy(self._chalk_feature))

            f_copy._chalk_feature.typ = FeatureTypeAnnotation(
                underlying=self._chalk_feature.typ.parsed_annotation[item]
            )

            return f_copy
        raise TypeError(f"Feature {self} does not support subscripting")

    def __getattr__(self, item: str):
        # Passing through __getattr__ on has_one features, as users can use getattr
        # notation in annotations for resolvers
        if item.startswith("__"):
            # Short-circuiting on the dunders to be compatible with copy.copy
            raise AttributeError(item)
        if self._chalk_feature.typ is not None and issubclass(self._chalk_feature.typ.underlying, Features):
            for f in self._chalk_feature.typ.underlying.features:
                assert isinstance(f, Feature), f"HasOne feature {f} does not inherit from FeaturesBase"
                if f.attribute_name == item:
                    return FeatureWrapper(self._chalk_feature.copy_with_path(f))
        raise AttributeError(item)


def unwrap_feature_or_none(maybe_feature_wrapper: Any) -> Optional[Feature]:
    return maybe_feature_wrapper._chalk_feature if isinstance(maybe_feature_wrapper, FeatureWrapper) else None


def unwrap_feature(maybe_feature_wrapper: Any) -> Feature:
    """Unwrap a class-annotated FeatureWrapper instance into the underlying feature.

    For example:

    .. code-block::

        @features
        class FooBar:
            foo: str
            bar: int

        type(FooBar.foo) is FeatureWrapper
        type(unwrap_feature(FooBar.foo)) is Feature
    """
    if isinstance(maybe_feature_wrapper, FeatureWrapper):
        return maybe_feature_wrapper._chalk_feature
    raise TypeError(
        f"{maybe_feature_wrapper} is of type {type(maybe_feature_wrapper).__name__}, expecting type FeatureWrapper"
    )


def unwrap_features_or_none(maybe_features: Any) -> Optional[Type[Features]]:
    if isinstance(maybe_features, type) and issubclass(maybe_features, Features):
        return maybe_features
    return None


def unwrap_features(maybe_features: Any) -> Type[Features]:
    features = unwrap_features_or_none(maybe_features)
    if features is None:
        raise TypeError(
            f"{maybe_features} is of type {type(maybe_features).__name__}, expecting a class decorated with @features"
        )
    return features


T = TypeVar("T")


def process_unwrapped(
    feature_or_feature_set, if_features: Callable[[Type[Features]], T], if_feature: Callable[[Feature], T]
) -> T:
    fs = unwrap_features_or_none(feature_or_feature_set)
    if fs is not None:
        return if_features(fs)

    ff = unwrap_feature_or_none(feature_or_feature_set)
    if ff is not None:
        return if_feature(ff)

    raise TypeError(
        f"{feature_or_feature_set} is of type {type(feature_or_feature_set).__name__}, expecting a class decorated with @features or an annotated member of "
        f"such a class"
    )


class Feature:
    def __init__(
        self,
        name: Optional[str] = None,
        attribute_name: Optional[str] = None,
        namespace: Optional[str] = None,
        features_cls: Optional[Type[Features]] = None,
        typ: Optional[Union[FeatureTypeAnnotation, type]] = None,
        version: Optional[int] = None,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        tags: Optional[List[str]] = None,
        primary: bool = False,
        max_staleness: Optional[Duration] = None,
        etl_offline_to_online: bool = False,
        encoder: Optional[Callable[[Any], JsonValue]] = None,
        decoder: Optional[Callable[[JsonValue], Any]] = None,
        pandas_dtype: Optional[str] = None,
        sqlalchemy_dtype: Optional[Union[TypeEngine, Type[TypeEngine]]] = None,
        join: Optional[Union[Callable[[], Filter], Filter]] = None,
        path: Tuple[HasOnePathObj, ...] = (),
        is_feature_time: bool = False,
    ):
        self.typ = FeatureTypeAnnotation(underlying=typ) if isinstance(typ, type) else typ
        self.features_cls = features_cls
        self.name = name
        self.attribute_name = attribute_name  # the attribute name for the feature in the @features class (in case if the name is specified differently)
        self.namespace = namespace
        self.path = path
        self.version = version
        self.description = description
        self.owner = owner
        self.tags = tags
        self.primary = primary
        self.max_staleness = max_staleness
        self.etl_offline_to_online = etl_offline_to_online
        self.encoder = encoder
        self.decoder = decoder
        self.pandas_dtype = pandas_dtype
        self.sqlalchemy_dtype = sqlalchemy_dtype
        self.is_feature_time = is_feature_time
        self._join = join

    def __str__(self):
        return self.root_fqn

    @classmethod
    def from_root_fqn(cls, root_fqn: str) -> Feature:
        """Convert a Root FQN into a feature.

        Args:
            root_fqn: The root fqn of the feature

        Returns:
            The feature for that root_fqn.
        """
        for x in PSEUDOFEATURES:
            if root_fqn == x.root_fqn or root_fqn == x.name:
                return x
        split_fqn = root_fqn.split(".")
        root_ns = split_fqn[0]
        split_fqn = split_fqn[1:]
        features_cls = FeatureSetBase.registry[root_ns]

        # FQNs are by name, so must lookup the feature in features_cls.features instead of using getattr
        feature: Optional[Feature] = None

        while len(split_fqn) > 0:
            feature_name = split_fqn[0]
            split_fqn = split_fqn[1:]

            found_feature = False

            for x in features_cls.features:
                assert isinstance(x, Feature)
                if x.name == feature_name:
                    assert x.attribute_name is not None
                    found_feature = True
                    if feature is None:
                        feature = x
                    else:
                        feature = feature.copy_with_path(x)
                    if len(split_fqn) > 0:
                        # Going to recurse, so validate that the feature is something that we can recurse on.
                        if not x.is_has_one:
                            raise TypeError(
                                (
                                    f"Feature {features_cls.__name__}.{feature_name}.{'.'.join(split_fqn)} does not exist "
                                    f"as {features_cls.__name__}.{feature_name} is not a has-one"
                                )
                            )
                        assert x.typ is not None
                        assert issubclass(x.typ.underlying, Features)
                        features_cls = x.typ.underlying
                    break
            if not found_feature:
                raise ValueError(f"Did not find feature named {feature_name} in features cls {features_cls.__name__}")
        assert feature is not None
        return feature

    @property
    def root_namespace(self) -> str:
        if len(self.path) > 0:
            assert self.path[0].parent.namespace is not None
            return self.path[0].parent.namespace
        assert self.namespace is not None
        return self.namespace

    @property
    def root_fqn(self):
        assert self.name is not None
        if len(self.path) > 0:
            return ".".join([self.root_namespace] + [cast(str, x.parent.name) for x in self.path] + [self.name])
        return f"{self.namespace}.{self.name}"

    def __hash__(self) -> int:
        return hash(self.root_fqn)

    def __eq__(self, other: object):
        if self.is_has_many:
            # For equality checks on a has-many, we would also need to compare the columns and types
            # For now, ignoring.
            return NotImplemented
        if isinstance(other, Feature):
            other = other.root_fqn
        if isinstance(other, str):
            return self.root_fqn == other
        return NotImplemented

    def __repr__(self):
        return f"Feature(fqn={self.namespace}.{self.name}, typ={self.typ})"

    @property
    def fqn(self) -> str:
        return ".".join((x for x in [self.namespace, self.name] if isinstance(x, str)))

    @property
    def is_has_one(self):
        # A feature is a has-one relationship if the type is another singleton features cls and there is a join condition
        assert self.typ is not None
        # Need to short-circuit if it is a dataframe, as datafames might not have an underlying
        return not self.typ.is_dataframe and self.join is not None

    @property
    def is_has_many(self):
        assert self.typ is not None
        return self.typ.is_dataframe and self.join is not None

    @property
    def has_resolved_join(self):
        return self._join is not None

    @property
    def join(self) -> Optional[Filter]:
        if self._join is not None:
            # Join was explicitly specified
            return self._join() if callable(self._join) else self._join
        # Attempt to extract the join condition from the foreign feature
        assert self.typ is not None
        foreign_features = self.typ.underlying
        if not issubclass(foreign_features, Features):
            return None
        assert self.features_cls is not None
        joins: List[Tuple[str, Filter]] = []  # Tuple of (name, Join)
        for f in foreign_features.features:
            assert isinstance(f, Feature)
            assert f.typ is not None
            if f.typ.underlying is self.features_cls and f.has_resolved_join:
                assert f.join is not None
                assert f.name is not None
                join = f.join() if callable(f.join) else f.join
                joins.append((f.name, join))
        if len(joins) == 0:
            # It's a nested feature
            return None
        # TODO(Ravi): Enable this check. But let's see if we can be smarter about which join to automatically use, if there are multiple
        # if len(joins) > 1:
        #     assert self.features_cls is not None
        #     raise ValueError(
        #         f"Multiple join conditions exist for {self.features_cls.__name__} and {foreign_features.__name__} on keys: "
        #         + f", ".join(f'{foreign_features.__name__}.{name}' for (name, _) in joins)
        #     )
        join = joins[0][1]
        if callable(join):
            join = join()
        self._join = join
        return join

    def copy_with_path(
        self,
        child: Feature,
    ):
        child_copy = copy.copy(child)
        assert child.attribute_name is not None
        child_copy.path = tuple(
            (
                *self.path,
                HasOnePathObj(
                    parent=self,
                    child=child,
                    parent_to_child_attribute_name=child.attribute_name,
                ),
            )
        )
        return child_copy


class Filter:
    def __init__(
        self,
        lhs: Any,  # think of this as "LHS"
        operation: str,
        rhs: Any,  # think of this as "RHS", a feature or a constant
    ) -> None:
        # Feature or other could be another feature, filter, featuretime, literal
        # Other could also be a sequence (in the case of operation = "in")
        self.operation = operation
        if isinstance(lhs, FeatureWrapper):
            lhs = unwrap_feature(lhs)
        self.lhs = lhs
        if self.operation == "in":
            if not isinstance(rhs, collections.abc.Iterable):
                raise ValueError("The RHS must be an iterable for operation='in'")
            rhs = {unwrap_feature(x) if isinstance(x, FeatureWrapper) else x for x in rhs}
        else:
            if isinstance(rhs, FeatureWrapper):
                rhs = unwrap_feature(rhs)
        self.rhs = rhs

    def __hash__(self) -> int:
        return hash((self.lhs, self.operation, self.rhs))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Filter):
            return NotImplemented
        return self.lhs == other.lhs and self.operation == other.operation and self.rhs == other.rhs

    def __and__(self, other: object):
        return Filter(self, "and", other)

    def __or__(self, other: object):
        return Filter(self, "or", other)

    def __invert__(self):
        return Filter(self, "not", None)

    def __bool__(self):
        # If the operation is == or !=, then compare the underlying filters or features
        # If x and y are features, then (x == y) is overloaded to return a Filter
        # This allows bool(x == y) to return True iff the x is y, while (x == y) is still a Filter instance
        # If either side is a FeatureWrapper
        # If either side is a Filter or a FeatureWrapper,
        if self.operation == "==":
            return self.lhs == self.rhs
        if self.operation == "!=":
            return self.lhs != self.rhs
        # Non-equality comparisons must be evaluated manually -- e.g. if x and y are Features
        # (x < y) would return a Filter, but bool(x < y) doesn't really make sense. So, raise.
        raise TypeError(f"Operation {self.operation} on a Filter is undefined")

    def referenced_features(self) -> Set[Feature]:

        result = set()
        if isinstance(self.lhs, Feature):
            result.add(self.lhs)

        if isinstance(self.rhs, Feature):
            result.add(self.rhs)

        return result

    def __repr__(self):
        return f"Filter({self.lhs} {self.operation} {self.rhs})"


class FeatureSetBase:
    """Registry containing all @features classes."""

    registry: Dict[str, Type[Features]] = {}  # mapping of fqn to Features cls

    def __init__(self) -> None:
        raise RuntimeError("FeatureSetBase should never be instantiated")


class FeaturesMeta(type):
    """Metaclass for classes decorated with ``@features``.

    This metaclass allows for:

    1.  Classes annotated with @features to pass the
        ``isinstance(x, Features)`` and ``issubclass(X, Features)`` checks.
    2.  ``Features[Feature1, Feature2]`` annotations to return subclasses of Features, so they can be used as proper type annotations.
    """

    def __subclasscheck__(self, subcls: type) -> bool:
        if not isinstance(subcls, type):
            raise TypeError(f"{subcls} is not a type")
        if hasattr(subcls, "__is_features__"):
            return getattr(subcls, "__is_features__")
        return False

    def __instancecheck__(self, instance: object) -> bool:
        return self.__subclasscheck__(type(instance))

    def __getitem__(cls, item: Any) -> Type:
        # This lets us subscript by the features
        # Annotating the return type as Type[Any] as instances of @features classes are
        # not recognized as being subclasses of Features by the type checker (even though at runtime they would be)
        from chalk.features.dataframe import DataFrame

        # Typing the `__getitem__` as any, since the @features members are typed as the underlying data structure
        # But, they should always be features or a tuple of features
        if isinstance(item, type) and issubclass(item, Features):
            item = [f for f in item.features if isinstance(f, (Feature, FeatureWrapper))]
        item = ensure_tuple(item)
        item = tuple(x._chalk_feature if isinstance(x, FeatureWrapper) else x for x in item)
        for x in item:
            if isinstance(x, str):
                raise TypeError(
                    f'String features like {cls.__name__}["{x}"] are unsupported. Instead, replace with "{cls.__name__}[{x}]"'
                )
            if isinstance(x, Feature) or (isinstance(x, type) and issubclass(x, DataFrame)):
                continue

            raise TypeError(f"Invalid feature {x} of type {type(x).__name__}")
        cls = cast(Type[Features], cls)

        new_features = tuple([*cls.features, *item])
        assert len(new_features) > 0

        class SubFeatures(cls):
            features = new_features

        return SubFeatures

    def __repr__(cls) -> str:
        cls = cast(Type[Features], cls)
        return f"Features[{', '.join(str(f) for f in cls.features)}]"

    @property
    def namespace(cls):
        cls = cast(Type[Features], cls)
        namespaces = [x.namespace for x in cls.features]
        return get_unique_item(namespaces, name=f"{cls.__name__} feature namespaces")


class Features(metaclass=FeaturesMeta):
    """Features base class.

    This class is never instantiated or directly inherited. However, classes
    annotated with @features can be thought of as inheriting from this class.
    It can be used with `isinstance()` and ``issubclass`` checks, as well as for
    typing.
    """

    def __new__(cls, *args: object, **kwargs: object):
        raise RuntimeError("Instances features cls should never be directly created. Instead, use Features[User.id]")

    # Internally, the Features class is instantiated when results come through, and
    # results are bound to instances of this class via attributes
    __chalk_primary__: ClassVar[Optional[Feature]]  # The primary key feature
    __chalk_owner__: ClassVar[Optional[str]]
    __chalk_tags__: ClassVar[List[str]]
    __chalk_ts__: ClassVar[Optional[Feature]]  # The timestamp feature
    features: Tuple[Union[Feature, Type[DataFrame]], ...] = ()
    __is_features__: bool = True

    # When constructing results, this class is instantiated


@dataclasses.dataclass(frozen=True)
class TimeDelta:
    weeks_ago: int = 0
    days_ago: int = 0
    hours_ago: int = 0
    minutes_ago: int = 0
    seconds_ago: int = 0
    milliseconds_ago: int = 0
    microseconds_ago: int = 0

    def to_std(self) -> timedelta:
        # Returning the negative inverse since the feature is defined in the past (e.g. days **ago**)
        return -timedelta(
            weeks=self.weeks_ago,
            days=self.days_ago,
            hours=self.hours_ago,
            minutes=self.minutes_ago,
            seconds=self.seconds_ago,
            milliseconds=self.milliseconds_ago,
            microseconds=self.microseconds_ago,
        )


CHALK_TS_FEATURE = Feature(name="CHALK_TS", namespace="__chalk__", typ=datetime)
ID_FEATURE = Feature(name="__id__", namespace="__chalk__", typ=str)
OBSERVED_AT_FEATURE = Feature(name="__observed_at__", namespace="__chalk__", typ=datetime)
REPLACED_OBSERVED_AT_FEATURE = Feature(name="__replaced_observed_at__", namespace="__chalk__", typ=datetime)

PSEUDOFEATURES = [CHALK_TS_FEATURE, ID_FEATURE, OBSERVED_AT_FEATURE, REPLACED_OBSERVED_AT_FEATURE]

ChalkTime = CHALK_TS_FEATURE


def before(
    weeks_ago: int = 0,
    days_ago: int = 0,
    hours_ago: int = 0,
    minutes_ago: int = 0,
    seconds_ago: int = 0,
    milliseconds_ago: int = 0,
    microseconds_ago: int = 0,
) -> Any:
    return Filter(
        lhs=CHALK_TS_FEATURE,
        operation="<=",
        rhs=TimeDelta(
            weeks_ago=weeks_ago,
            days_ago=days_ago,
            hours_ago=hours_ago,
            minutes_ago=minutes_ago,
            seconds_ago=seconds_ago,
            milliseconds_ago=milliseconds_ago,
            microseconds_ago=microseconds_ago,
        ),
    )


def after(
    weeks_ago: int = 0,
    days_ago: int = 0,
    hours_ago: int = 0,
    minutes_ago: int = 0,
    seconds_ago: int = 0,
    milliseconds_ago: int = 0,
    microseconds_ago: int = 0,
) -> Any:
    return Filter(
        lhs=CHALK_TS_FEATURE,
        operation=">=",
        rhs=TimeDelta(
            weeks_ago=weeks_ago,
            days_ago=days_ago,
            hours_ago=hours_ago,
            minutes_ago=minutes_ago,
            seconds_ago=seconds_ago,
            milliseconds_ago=milliseconds_ago,
            microseconds_ago=microseconds_ago,
        ),
    )


UNPARSED_TIMESTAMP = Feature(typ=datetime)
