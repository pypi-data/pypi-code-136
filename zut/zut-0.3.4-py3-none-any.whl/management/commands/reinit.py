from __future__ import annotations
import logging, re, sys, os
from pathlib import Path
from psycopg2.sql import SQL, Literal
from django.conf import settings
from django.db import connection
from django.core.management import base, call_command, get_commands
from zut.env import get_venv
from zut.db import get_backend, Backend, BackendNotSupported

logger = logging.getLogger(__name__)

_migration_name_re = re.compile(r"^(\d+)_")

class Command(base.BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--drop", dest="action", action="store_const", const="drop")
        parser.add_argument("--bak", dest="action", action="store_const", const="bak")
        parser.add_argument("--bak-to", dest="action")
        parser.add_argument("remake_migrations_for_apps", nargs="*", help="apps for which migrations are remade")

    def handle(self, action: str = None, remake_migrations_for_apps: list[str] = [], **kwargs):
        if not settings.DEBUG:
            raise ValueError("reinit may be used only in DEBUG mode")
        if not action:
            raise ValueError("please confirm what to do with current data: --drop, --bak or --bak-to")

        backend = get_backend(connection=connection)
        if backend != Backend.POSTGRESQL:
            raise BackendNotSupported(backend)

        self.REMAKE_MIGRATIONS_AFTER: dict[str,int] = getattr(settings, "REMAKE_MIGRATIONS_AFTER", {})
        self.BASE_DIR: Path = settings.BASE_DIR
        self.remake_migrations_for_apps = remake_migrations_for_apps

        if action == "drop":
            self.drop()
        else:
            self.move_to_schema(action)

        self.delete_nonmanual_migrations()
        self.rename_manual_migrations()

        logger.info("make migrations")
        call_command("makemigrations")

        self.restore_renamed_migrations()
        
        logger.info("migrate")
        call_command("migrate")

        logger.info("createsuperuser")
        call_command("createsuperuser", "--noinput")

        defined_commands = get_commands()

        if "seed" in defined_commands:
            logger.info("seed")
            call_command("seed")


    def move_to_schema(self, new_schema, old_schema="public"):
        sql = """do language plpgsql
    $$declare
        old_schema name = {};
        new_schema name = {};
        sql_query text;
    begin
        sql_query = format('create schema %I', new_schema);

        raise notice 'applying %', sql_query;
        execute sql_query;
    
        for sql_query in
            select
                format('alter %s %I.%I set schema %I', case when table_type = 'VIEW' then 'view' else 'table' end, table_schema, table_name, new_schema)
            from information_schema.tables
            where table_schema = old_schema
            and table_name not in ('geography_columns', 'geometry_columns', 'spatial_ref_sys') -- postgis
        loop
            raise notice 'applying %', sql_query;
            execute sql_query;
        end loop;
    end;$$;
    """

        with connection.cursor() as cursor:
            cursor.execute(SQL(sql).format(Literal(old_schema), Literal(new_schema if new_schema else "public")))


    def drop(self, schema="public"):
        sql = """do language plpgsql
    $$declare
        old_schema name = {};
        sql_query text;
    begin
        -- First, remove foreign-key constraints
        for sql_query in
            select
                format('alter table %I.%I drop constraint %I', table_schema, table_name, constraint_name)
            from information_schema.table_constraints
            where table_schema = old_schema and constraint_type = 'FOREIGN KEY'
            and table_name not in ('geography_columns', 'geometry_columns', 'spatial_ref_sys') -- postgis
        loop
            raise notice 'applying %', sql_query;
            execute sql_query;
        end loop;

        -- Then, drop tables
        for sql_query in
            select
                format('drop %s if exists %I.%I cascade'
                    ,case when table_type = 'VIEW' then 'view' else 'table' end
                    ,table_schema
                    ,table_name
                )
            from information_schema.tables
            where table_schema = old_schema
            and table_name not in ('geography_columns', 'geometry_columns', 'spatial_ref_sys') -- postgis
        loop
            raise notice 'applying %', sql_query;
            execute sql_query;
        end loop;
    end;$$;
    """

        with connection.cursor() as cursor:
            cursor.execute(SQL(sql).format(Literal(schema)))

    def should_remake_migration(self, path: Path, remake_manuals=False):
        if not remake_manuals and path.name.endswith("_manual.py"):
            return False

        if get_venv() in path.parents:
            # exclude migrations located in ".venv" directory
            return False

        app_name = path.parent.parent.name
        if self.remake_migrations_for_apps and not app_name in self.remake_migrations_for_apps:
            return False

        if self.REMAKE_MIGRATIONS_AFTER and app_name in self.REMAKE_MIGRATIONS_AFTER:
            m = _migration_name_re.match(path.name)
            if not m:
                return False

            migration_number = int(m.group(1))
            if migration_number <= self.REMAKE_MIGRATIONS_AFTER[app_name]:
                return False
        
            else:
                return True

        elif self.remake_migrations_for_apps and app_name in self.remake_migrations_for_apps:
            return True

        else:
            return False

    def delete_nonmanual_migrations(self):
        """ Delete non-manual migrations """
        for path in self.BASE_DIR.glob("*/migrations/0*.py"):
            if self.should_remake_migration(path):
                logger.info(f"delete {path}")
                path.unlink()
            else:
                logger.info(f"preserve {path}")

    def rename_manual_migrations(self):
        self.renamed: dict[Path,Path] = {}

        """ Rename manual migrations to py~ """
        for path in self.BASE_DIR.glob("*/migrations/*_manual.py"):
            if self.should_remake_migration(path, remake_manuals=True):
                target = path.with_name(f"{path.name}~")
                logger.info(f"rename {path} to {target}")
                path.rename(target)
                self.renamed[path] = target
            else:
                logger.info(f"preserve {path}")
    
    def restore_renamed_migrations(self):
        """ Restore migrations from py~ """
        for origin, renamed in self.renamed.items():
            logger.info(f"rename {renamed} to {origin}")
            renamed.rename(origin)
