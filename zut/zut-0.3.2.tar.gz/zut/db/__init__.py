from __future__ import annotations
import logging
from enum import Enum
from pathlib import Path
from ..format import slugen

try: # usage with Django
    from django.db import router, connections
    from django.core.exceptions import ImproperlyConfigured
    from django.apps import apps
    with_django = True
except: # usage without Django
    with_django = False


logger = logging.getLogger(__name__)

ZUT_DB_BASE_DIR = Path(__file__).parent

class Backend(Enum):
    POSTGRESQL = 1


class BackendNotSupported(ValueError):
    def __init__(self, info: Backend|type):
        if isinstance(info, Backend):
            message = f"backend not supported: {info.name}"
        elif isinstance(info, type):
            message = f"connection type not supported: {info.__module__}.{info.__name__}"
        else:
            message = info
        super().__init__(message)


def get_backend(connection):
    search = type(connection).__module__ + "." + type(connection).__name__
    if search == "django.utils.connection.ConnectionProxy":
        search = connection._connections[connection._alias].vendor
    elif hasattr(connection, "vendor"):
        # e.g. django.db.backends.postgresql.base.DatabaseWrapper, django.contrib.gis.db.backends.postgis.base.DatabaseWrapper
        search = connection.vendor

    if search in ["postgresql", "psycopg2.extensions.connection"]:
        return Backend.POSTGRESQL
    else:
        raise BackendNotSupported(type(connection))


def get_connection(connection = None, model: type = None, for_write: bool = False):
    if connection:
        if model:
            raise ValueError("connection and model options cannot be both used")
        if not isinstance(connection, str):
            return connection

    if not with_django:
        raise ValueError("usage without connection option requires Django")

    try:
        if isinstance(connection, str):
            alias = connection

        elif model:
            if not hasattr(model, "objects"):
                raise ValueError(f"type {model.__name__} does not seem to be a Django model")

            alias = router.db_for_write(model) if for_write else router.db_for_read(model)
            if not alias:
                alias = "default"

        else:
            alias = "default"

        return connections[alias]

    except ImproperlyConfigured as err:
        raise ValueError(f"Django improperly configured: please provide \"connection\" option")


def dictfetchall(cursor) -> list[dict]:
    """
    Return all rows from a cursor as a dict.
    """ 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]


def call_procedure(*names: str, connection = None):
    connection = get_connection(connection=connection)
    backend = get_backend(connection)

    for name in names:
        if backend == Backend.POSTGRESQL:
            from psycopg2.sql import SQL, Identifier
            sql = SQL("call {}()").format(Identifier(name))
        else:
            raise BackendNotSupported(backend)

        with connection.cursor() as cursor:
            logger.info("call %s", name)
            cursor.execute(sql)


def truncate_table(*names: str|type, connection = None):
    for name in names:
        if isinstance(name, str):
            model = None
            db_table = name
        else:
            # 'name' is assumed to be a model class    
            model = name
            db_table = model._meta.db_table
        
        connection = get_connection(connection=connection, model=model, for_write=True)
        backend = get_backend(connection)
        if backend == Backend.POSTGRESQL:
            from psycopg2.sql import SQL, Identifier
            sql = SQL("truncate table {}").format(Identifier(db_table))
        else:
            raise BackendNotSupported(backend)
        
        with connection.cursor() as cursor:
            logger.info(f"truncate table {db_table}")
            cursor.execute(sql)


def seed_from_enum(model: type, enum: type|str = "Values", value_field: str="id", name_field: str="name", slug_field: str="slug", attr_fields: list[str]=None):
    if not hasattr(model, "objects"):
        raise ValueError(f"type {model.__name__} does not seem to be a Django model")
    if isinstance(enum, str):
        enum = getattr(model, enum, None)
        if not enum:
            raise ValueError("model %s has no %s attribute" % (model, enum))
    if not isinstance(enum, type):
        raise ValueError(f"invalid type for enum: {type(enum).__name__}")
    if not issubclass(enum, Enum):
        raise ValueError(f"not a subclass of Enum: {enum.__name__}")

    has_slug_field = False
    fields = model._meta.get_fields()
    for field in fields:
        if field.name == slug_field:
            has_slug_field = True
            break

    logger.info(f"seed {model.__module__}.{model.__name__}.{enum.__name__}")
    for literal in enum:
        name = literal.name.lower().replace("_", " ").capitalize()

        defaults = {
            name_field: name
        }

        if has_slug_field:
            defaults[slug_field] = slugen(name)

        if attr_fields:
            for attr, field in attr_fields.items():
                defaults[field] = getattr(literal, attr)

        kwargs = {
            value_field: literal.value,
            "defaults": defaults
        }
        
        model.objects.get_or_create(**kwargs)


def seed_from_enums(*app_names: str):
    if not with_django:
        raise ValueError("Django required")

    for app in apps.get_app_configs():
        if app_names and app.name not in app_names:
            continue

        for model in app.get_models():
            if hasattr(model, "Values"):
                seed_from_enum(model)


def deploy_sql(*paths: Path|str, encoding = "utf-8", connection = None):
    connection = get_connection(connection=connection)

    actual_paths: list[Path] = []
    for path in paths:
        if isinstance(path, str):
            path = Path(path)
        actual_paths.append(path)

    actual_paths.sort()

    for path in actual_paths:
        if path.is_dir():
            subpaths = sorted(path.iterdir())
            deploy_sql(*subpaths, encoding=encoding, connection=connection)

        elif not path.name.endswith(".sql"):
            continue # ignore

        elif path.name.endswith("_revert.sql"):
            continue # ignore

        else:
            logger.info("execute %s", path)
            sql = path.read_text(encoding=encoding)
            with connection.cursor() as cursor:
                cursor.execute(sql)


def revert_sql(*paths: Path|str, encoding = "utf-8", connection=None):
    connection = get_connection(connection=connection)

    actual_paths: list[Path] = []
    for path in paths:
        if isinstance(path, str):
            path = Path(path)
        actual_paths.append(path)

    actual_paths.sort(reverse=True)

    for path in actual_paths:
        if path.is_dir():
            subpaths = sorted(path.iterdir())
            revert_sql(*subpaths, encoding=encoding, connection=connection)

        elif not path.name.endswith("_revert.sql"):
            continue # ignore

        else:
            logger.info("execute %s", path)
            sql = path.read_text(encoding=encoding)
            with connection.cursor() as cursor:
                cursor.execute(sql)
