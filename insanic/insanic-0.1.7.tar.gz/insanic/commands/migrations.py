import os
import warnings
from pathlib import Path
import sys
from typing import Any

from insanic.db import get_db_connection, in_transaction
from insanic.commands import AsyncCommand, SyncCommand, CommandParser
from insanic.utils import read_file_content

MIGRATIONS_TABLE = 'db_migrations'
MIGRATIONS_LOCATION = Path('migrations')

MIGRATION_UP_MARKER = '-- upgrade --'
MIGRATION_DOWN_MARKER = '-- downgrade --'
MIGRATIONS_TEMPLATE = f"""
{MIGRATION_UP_MARKER}

{MIGRATION_DOWN_MARKER}
"""

class Migration:
    STATE_APPLIED: str = '*'
    STATE_PLANNED: str = ' '
    STATE_MISSING: str = '?'

    name: str
    state: str | None

    def __init__(self, name: str, state: str | None = None) -> None:
        self.name = name
        self.state = state

async def create_migrations_table() -> None:
    connection = get_db_connection()

    # @FIXME: Ugly hack to prevent "Warning: Table 'db_migrations' already exists"
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        await connection.execute_query(f'''
            CREATE TABLE IF NOT EXISTS `{MIGRATIONS_TABLE}` (
                `name` varchar(255) NOT NULL,
                `upgrade_sql` text NOT NULL,
                `downgrade_sql` text NULL DEFAULT NULL,

                PRIMARY KEY (`name`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
        ''')

async def get_applied_migrations() -> list[str]:
    connection = get_db_connection()
    await create_migrations_table()

    _, query_result = await connection.execute_query(f'SELECT `name` FROM `{MIGRATIONS_TABLE}`')
    return [ row['name'] for row in query_result ]

def get_migrations_files() -> list[str]:
    return list(sorted(filter(lambda x: x.endswith('sql'), os.listdir(MIGRATIONS_LOCATION))))

async def get_migrations_list() -> list[Migration]:
    applied_migrations = await get_applied_migrations()
    migrations_files = get_migrations_files()

    migrations = []
    for applied_migration in applied_migrations:
        migration = Migration(applied_migration, state=Migration.STATE_MISSING)

        if applied_migration in migrations_files:
            migration.state = Migration.STATE_APPLIED
            migrations_files.remove(applied_migration)

        migrations.append(migration)

    for migration_file in migrations_files:
        migrations.append(Migration(migration_file, state=Migration.STATE_PLANNED))

    return sorted(migrations, key=lambda migration: migration.name)

async def apply_migration_file(file_name: str) -> None:
    migration_instructions = read_file_content(Path(MIGRATIONS_LOCATION, file_name))

    upgrade_queries_index = migration_instructions.index(MIGRATION_UP_MARKER) + len(MIGRATION_UP_MARKER)
    try:
        downgrade_queries_index = migration_instructions.index(MIGRATION_DOWN_MARKER) + len(MIGRATION_DOWN_MARKER)
    except ValueError:
        downgrade_queries_index = len(migration_instructions) - 1

    upgrade_queries = migration_instructions[upgrade_queries_index:downgrade_queries_index].strip()
    downgrade_queries = migration_instructions[downgrade_queries_index:].strip()

    async with in_transaction() as connection:
        await connection.execute_script(upgrade_queries)
        await connection.execute_insert(f'INSERT INTO `{MIGRATIONS_TABLE}` VALUES (%s, %s, %s)', [
            file_name, upgrade_queries, downgrade_queries,
        ])

async def rollback_migration(migration_name: str) -> None:
    connection = get_db_connection()

    migrations_list = await connection.execute_query_dict(
        f'SELECT * FROM `{MIGRATIONS_TABLE}` WHERE `name` = %s LIMIT 1',
        [migration_name]
    )
    migration = migrations_list[0]

    async with in_transaction() as connection:
        await connection.execute_script(migration['downgrade_sql'])
        await connection.execute_insert(f'DELETE FROM `{MIGRATIONS_TABLE}` WHERE `name` = %s', [migration_name])


class MigrationsListCommand(AsyncCommand):
    help = 'Lists all available migrations'

    async def execute(self, **kwargs: Any) -> None:
        migrations = await get_migrations_list()

        print('List of migrations:')
        print('Status | Migration')

        for migration in migrations:
            print(f'     {migration.state} | {migration.name}')

class MigrationsApplyCommand(AsyncCommand):
    help = 'Applies all planned migrations'

    async def execute(self, **kwargs: Any) -> None:
        migrations = await get_migrations_list()
        planned_migrations_count = len(list(filter(lambda x: x.state == Migration.STATE_PLANNED, migrations)))

        print(f'Planned migrations count: {planned_migrations_count}')

        for migration in migrations:
            if migration.state == Migration.STATE_APPLIED:
                continue

            print(f'Migration "{migration.name}": ', end='')

            if migration.state == Migration.STATE_PLANNED:
                print('Applying... ', end='')
                sys.stdout.flush()

                await apply_migration_file(migration.name)
                print('OK')
                continue

            if migration.state == Migration.STATE_MISSING:
                print('Rolling back... ', end='')
                sys.stdout.flush()

                await rollback_migration(migration.name)
                print('OK')
                continue

class MigrationsGenerateCommand(SyncCommand):
    help = 'Generates a new migration file'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('filename', nargs='?', default='migration')

    def generate_migration_number(self) -> int:  # pylint: disable=no-self-use
        migration_files = get_migrations_files()

        if len(migration_files) == 0:
            return 0

        return int(migration_files[-1][0:4])

    def execute(self, filename: str, **kwargs: Any) -> None:  # type: ignore[override] # pylint: disable=arguments-differ
        migration_number = self.generate_migration_number() + 1
        migration_filename = Path(MIGRATIONS_LOCATION, f'{migration_number:04d}_{filename}.sql')

        with open(migration_filename, 'wt', encoding='utf-8') as file:
            file.write(MIGRATIONS_TEMPLATE)

        print(f'Migration file "{migration_filename} is generated...')
