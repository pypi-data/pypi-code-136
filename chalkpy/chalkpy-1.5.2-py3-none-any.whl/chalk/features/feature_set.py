import ast
import functools
import inspect
import re
import sys
import textwrap
import threading
import types
from datetime import datetime
from typing import (
    Any,
    Callable,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    overload,
)

from chalk.features.feature import Feature, Features, FeatureSetBase, FeatureTypeAnnotation, FeatureWrapper
from chalk.features.tag import Tags
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import Duration
from chalk.utils.metaprogramming import MISSING, create_fn, field_assign, set_new_attribute
from chalk.utils.string import removeprefix, to_snake_case

T = TypeVar("T")
U = TypeVar("U")
JsonValue = TypeVar("JsonValue")


def feature(
    description: Optional[str] = None,
    owner: Optional[str] = None,
    tags: Optional[Tags] = None,
    name: Optional[str] = None,
    version: Optional[int] = None,
    primary: bool = False,
    max_staleness: Optional[Duration] = None,
    etl_offline_to_online: bool = False,
    encoder: Optional[Callable[[T], JsonValue]] = None,
    decoder: Optional[Callable[[JsonValue], T]] = None,
) -> T:
    return cast(
        T,
        Feature(
            name=name,
            version=version,
            owner=owner,
            tags=None if tags is None else list(ensure_tuple(tags)),
            description=description,
            primary=primary,
            max_staleness=max_staleness,
            etl_offline_to_online=etl_offline_to_online,
            encoder=encoder,
            decoder=decoder,
        ),
    )


def feature_time() -> Any:
    return Feature(typ=datetime, is_feature_time=True)


def has_one(f: Callable[[], Any]) -> Any:
    return Feature(join=f)


def has_many(f: Callable[[], Any]) -> Any:
    return Feature(join=f)


def _discover_feature(cls: Type[Features], name: str, *conditions: Callable[[Feature], bool]):
    for cond in conditions:
        features = [c for c in cls.features if isinstance(c, Feature) and cond(c)]
        if len(features) == 1:
            return features[0]
        if len(features) > 1:
            raise ValueError(
                f"Multiple {name} features are not supported in {cls.__name__}: "
                + ", ".join(f"{cls.__name__}.{x.name}" for x in features)
            )
    return None


@overload
def features(
    *,
    owner: Optional[str] = None,
    tags: Optional[Tags] = None,
) -> Callable[[Type[T]], Type[T]]:
    ...


@overload
def features(cls: Type[T]) -> Type[T]:
    ...


def features(
    cls: Optional[Type[T]] = None,
    *,
    owner: Optional[str] = None,
    tags: Optional[Tags] = None,
) -> Union[Callable[[Type[T]], Type[T]], Type[T]]:
    """Returns the same class as was passed in, with dunder methods
    added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.
    """

    def wrap(c: Type[T]) -> Type[T]:
        updated_class = _process_class(c, owner, ensure_tuple(tags))
        set_new_attribute(
            cls=updated_class,
            name="namespace",
            value=to_snake_case(updated_class.__name__),
        )
        assert issubclass(updated_class, Features)
        FeatureSetBase.registry[updated_class.namespace] = updated_class

        primary_feature = _discover_feature(
            updated_class,
            "primary",
            lambda f: f.primary,
            lambda f: f.name == "id" and not f.has_resolved_join and not f.is_feature_time,
        )
        if primary_feature is not None:
            primary_feature.primary = True

        timestamp_feature = _discover_feature(
            updated_class,
            "feature time",
            lambda f: f.is_feature_time,
            lambda f: f.name == "ts" and not f.has_resolved_join,
        )
        set_new_attribute(cls=updated_class, name="__chalk_primary__", value=primary_feature)
        set_new_attribute(cls=updated_class, name="__chalk_ts__", value=timestamp_feature)

        return cast(Type[T], updated_class)

    # See if we're being called as @features or @features().
    if cls is None:
        # We're called with parens.
        return wrap

    # We're called as @features without parens.
    return wrap(cls)


def _init_param(f: Feature):
    # Return the __init__ parameter string for this field.  For
    # example, the equivalent of 'x:int=3' (except instead of 'int',
    # reference a variable set to int, and instead of '3', reference a
    # variable set to 3).
    return f"{f.name}:_type_{f.name}=MISSING"


def _init_fn(fields: List[Feature], self_name: str, _globals: Mapping[str, Any]):
    # fields contains both real fields and InitVar pseudo-fields.

    # Make sure we don't have fields without defaults following fields
    # with defaults.  This actually would be caught when exec-ing the
    # function source code, but catching it here gives a better error
    # message, and future-proofs us in case we build up the function
    # using ast.

    _locals: MutableMapping[str, Any] = {f"_type_{f.name}": f.typ and f.typ.annotation for f in fields}
    _locals.update(
        {
            "MISSING": MISSING,
            # '_HAS_DEFAULT_FACTORY': _HAS_DEFAULT_FACTORY,
        }
    )

    body_lines = []
    for f in fields:
        assert f.name is not None
        line = field_assign(f.name, f.name, self_name)
        # line is None means that this field doesn't require
        # initialization (it's a pseudo-field).  Just skip it.
        if line:
            body_lines.append(line)

    # If no body lines, use 'pass'.
    if not body_lines:
        body_lines = ["pass"]

    # Add the keyword-only args.  Because the * can only be added if
    # there's at least one keyword-only arg, there needs to be a test here
    # (instead of just concatenting the lists together).
    _init_params = [_init_param(f) for f in fields]
    return create_fn(
        "__init__",
        [self_name] + _init_params,
        body_lines,
        _locals=_locals,
        _globals=_globals,
        return_type=None,
    )


def _parse_tags(ts: str) -> List[str]:
    ts = re.sub(",", " ", ts)
    ts = re.sub(" +", " ", ts.strip())
    return [xx.strip() for xx in ts.split(" ")]


def _get_field(
    cls: Type,
    annotation_name: str,
    comments: Mapping[str, str],
    class_owner: Optional[str],
    class_tags: Optional[Tuple[str, ...]],
):
    # Return a Field object for this field name and type.  ClassVars and
    # InitVars are also returned, but marked as such (see f._field_type).
    # default_kw_only is the value of kw_only to use if there isn't a field()
    # that defines it.

    # If the default value isn't derived from Field, then it's only a
    # normal default value.  Convert it to a Field().
    default = getattr(cls, annotation_name, MISSING)

    if isinstance(default, Feature):
        f = default
    else:
        if isinstance(default, types.MemberDescriptorType):
            # This is a field in __slots__, so it has no default value.
            default = MISSING
        f = Feature(name=annotation_name, namespace=to_snake_case(cls.__name__))

    # Only at this point do we know the name and the type.  Set them.
    f.namespace = to_snake_case(cls.__name__)
    if f.name is None:
        # if there is a name set by the `feature()` method, use that
        f.name = annotation_name

    comment_for_feature = comments.get(annotation_name)
    comment_based_description = None
    comment_based_owner = None
    comment_based_tags = None

    if comment_for_feature is not None:
        comment_lines = []
        for line in comment_for_feature.splitlines():
            stripped_line = line.strip()
            if stripped_line.startswith(":owner:"):
                comment_based_owner = removeprefix(stripped_line, ":owner:").strip()
            elif stripped_line.startswith(":tags:"):
                parsed = _parse_tags(removeprefix(stripped_line, ":tags:"))
                if len(parsed) > 0:
                    if comment_based_tags is None:
                        comment_based_tags = parsed
                    else:
                        comment_based_tags.extend(parsed)
            else:
                comment_lines.append(line)

        comment_based_description = "\n".join(comment_lines)

    if f.description is None and comment_based_description is not None:
        f.description = comment_based_description

    if comment_based_tags is not None:
        if f.tags is None:
            f.tags = comment_based_tags
        else:
            f.tags.extend(comment_based_tags)

    if class_tags is not None:
        if f.tags is None:
            f.tags = list(class_tags)
        else:
            f.tags.extend(class_tags)

    if f.owner is not None and comment_based_owner is not None:
        raise ValueError(
            (
                f"Owner for {f.namespace}.{f.name} specified both on the feature and in the comment. "
                f"Please use only one of these two."
            )
        )
    elif f.owner is None:
        f.owner = comment_based_owner or class_owner

    f.typ = FeatureTypeAnnotation(cls, annotation_name)
    f.features_cls = cls
    f.attribute_name = annotation_name
    return f


def _recursive_repr(user_function: Callable[[T], str]) -> Callable[[T], str]:
    # Decorator to make a repr function return "..." for a recursive
    # call.
    repr_running = set()

    @functools.wraps(user_function)
    def wrapper(self: T):
        key = id(self), threading.get_ident()
        if key in repr_running:
            return "..."
        repr_running.add(key)
        try:
            result = user_function(self)
        finally:
            repr_running.discard(key)
        return result

    return wrapper


def _repr_fn(fields: List[Feature], _globals: Mapping[str, Any]):
    fn = create_fn(
        name="__repr__",
        args=["self"],
        body=[
            'return self.__class__.__qualname__ + f"('
            + ", ".join([f"{f.name}={{self.{f.name}!r}}" for f in fields])
            + ')"'
        ],
        _globals=_globals,
    )
    return _recursive_repr(fn)


def _tuple_str(obj_name: str, fields: Sequence[Feature]):
    # Return a string representing each field of obj_name as a tuple
    # member.  So, if fields is ['x', 'y'] and obj_name is "self",
    # return "(self.x,self.y)".

    # Special case for the 0-tuple.
    if not fields:
        return "()"
    # Note the trailing comma, needed if this turns out to be a 1-tuple.
    return f'({",".join([f"{obj_name}.{f.name}" for f in fields])},)'


def _cmp_fn(name: str, op: str, self_tuple: str, other_tuple: str, _globals: Mapping[str, Any]):
    # Create a comparison function.  If the fields in the object are
    # named 'x' and 'y', then self_tuple is the string
    # '(self.x,self.y)' and other_tuple is the string
    # '(other.x,other.y)'.

    return create_fn(
        name=name,
        args=["self", "other"],
        body=[
            "if other.__class__ is self.__class__:",
            f" return {self_tuple}{op}{other_tuple}",
            "return NotImplemented",
        ],
        _globals=_globals,
    )


def _eq_fn(fields: List[Feature], _globals: Mapping[str, Any]):
    self_tuple = _tuple_str("self", fields)
    other_tuple = _tuple_str("other", fields)
    return _cmp_fn("__eq__", "==", self_tuple, other_tuple, _globals=_globals)


def _iter_fn(fields: List[Feature], _globals: Mapping[str, Any]):
    return create_fn(
        "__iter__",
        args=["self"],
        body=[
            f"for __chalk_f__ in self.features:",
            f"    if getattr(self, __chalk_f__.attribute_name) != MISSING and type(__chalk_f__).__name__ == 'Feature' and not __chalk_f__.is_has_one and not __chalk_f__.is_has_many:",
            f"        yield __chalk_f__.fqn, getattr(self, __chalk_f__.attribute_name)",
        ],
    )


def _parse_annotation_comments(cls: Type[T]) -> Mapping[str, str]:
    source = textwrap.dedent(inspect.getsource(cls))

    source_lines = source.splitlines()
    tree = ast.parse(source)
    comments_for_annotations = {}
    if len(tree.body) != 1:
        return comments_for_annotations

    class_def = tree.body[0]
    if isinstance(class_def, ast.ClassDef):
        for stmt in class_def.body:
            if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                line = stmt.lineno - 2
                comments: List[str] = []
                while line >= 0 and source_lines[line].strip().startswith("#"):
                    comment = source_lines[line].strip().strip("#").strip()
                    comments.insert(0, comment)
                    line -= 1

                if len(comments) > 0:
                    comments_for_annotations[stmt.target.id] = textwrap.dedent("\n".join(comments))

    return comments_for_annotations


def _process_class(cls: Type[T], owner: Optional[str], tags: Tuple[str, ...]) -> Type[T]:
    cls_annotations = cls.__dict__.get("__annotations__", {})

    if cls.__module__ in sys.modules:
        _globals = sys.modules[cls.__module__].__dict__
    else:
        _globals = {}

    # Find feature times that weren't annotated.
    for (name, member) in inspect.getmembers(cls):
        if name not in cls_annotations and isinstance(member, Feature):
            # All feature types need annotations, except for datetimes, which we can automatically infer
            if member.typ is not None and member.typ.is_parsed and issubclass(member.typ.underlying, datetime):
                cls_annotations[name] = datetime
            else:
                raise TypeError(f"Member {name} is missing an annotation")

    # If we pass this function something that isn't a class, it could raise
    try:
        comments = _parse_annotation_comments(cls)
    except:
        comments = {}

    cls_fields = [
        _get_field(
            cls=cls,
            annotation_name=name,
            comments=comments,
            class_owner=owner,
            class_tags=tags,
        )
        for name in cls_annotations
    ]

    set_new_attribute(
        cls=cls,
        name="__init__",
        value=_init_fn(
            fields=cls_fields,
            # The name to use for the "self"
            # param in __init__.  Use "self"
            # if possible.
            self_name="self",
            _globals=_globals,
        ),
    )

    set_new_attribute(cls=cls, name="__repr__", value=_repr_fn(fields=cls_fields, _globals=_globals))

    set_new_attribute(cls=cls, name="__eq__", value=_eq_fn(fields=cls_fields, _globals=_globals))
    set_new_attribute(cls=cls, name="__hash__", value=None)
    set_new_attribute(cls=cls, name="__iter__", value=_iter_fn(fields=cls_fields, _globals=_globals))

    namespace = to_snake_case(cls.__name__)
    set_new_attribute(cls=cls, name="__chalk_namespace__", value=namespace)
    set_new_attribute(cls=cls, name="__chalk_owner__", value=owner)
    set_new_attribute(cls=cls, name="__chalk_tags__", value=list(tags))
    set_new_attribute(cls=cls, name="features", value=cls_fields)
    set_new_attribute(cls=cls, name="__is_features__", value=True)

    for f in cls_fields:
        assert f.attribute_name is not None
        # Wrap all class features with FeatureWrapper
        setattr(cls, f.attribute_name, FeatureWrapper(f))

    return cls
