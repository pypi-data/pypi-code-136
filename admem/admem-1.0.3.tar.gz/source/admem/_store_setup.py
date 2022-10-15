# Copyright (c) 2022 Mario S. Könz; License: MIT
import collections
import contextlib
import io
import typing as tp

import django
from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.db import connections

from ._decorator import BACKEND_LINKER
from ._django_store import DjangoStore
from ._protocols import StoreProtocol

__all__ = ["set_store", "set_store_for_django", "ACTIVE_STORES"]

ACTIVE_STORES: collections.OrderedDict[str, StoreProtocol] = collections.OrderedDict()


def set_store(
    identifier: str = "first", flavor: str = "sqlite3", **kwgs: tp.Any
) -> None:
    if not settings.configured:
        settings.configure(
            DATABASES={"default": {"ENGINE": "django.db.backends.dummy"}},
            TIME_ZONE="UTC",
            USE_TZ=True,
            DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
        )
        django.setup()

    assert identifier != "default"
    databases = settings.DATABASES
    if flavor == "sqlite3":
        assert identifier not in databases
        databases[identifier] = dict(
            NAME=kwgs["path"],
            ENGINE="django.db.backends.sqlite3",
            TIME_ZONE="UTC",
            USE_TZ=True,
        )
        ACTIVE_STORES[identifier] = DjangoStore(identifier)
    else:
        raise NotImplementedError(flavor)

    apps.apps_ready = apps.models_ready = apps.loading = apps.ready = False
    apps.clear_cache()
    for app_label in BACKEND_LINKER.app_labels:
        if app_label not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS.append(app_label)

    apps.populate(settings.INSTALLED_APPS)
    connections.configure_settings(databases)

    call_command("makemigrations")
    with contextlib.redirect_stdout(io.StringIO()):
        call_command("migrate", database=identifier)


def set_store_for_django(identifier: str = "default") -> None:
    ACTIVE_STORES[identifier] = DjangoStore(identifier)
