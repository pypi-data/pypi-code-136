from typing import cast

from chalk.features import features
from chalk.sql import PostgreSQLSource
from chalk.sql.integrations.postgres import PostgreSQLSourceImpl


@features
class UserFeatures:
    id: str


@features
class LibraryFeatures:
    id: str


def test_table_builder():
    source: PostgreSQLSourceImpl = cast(
        PostgreSQLSourceImpl,
        PostgreSQLSource()
        .with_table(name="users", features=UserFeatures)
        .with_table(name="libraries", features=LibraryFeatures),
    )
    assert len(source.ingested_tables) == 2
