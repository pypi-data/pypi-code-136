import asyncio
from enum import Enum
from typing import List, Optional

from databases import Database
import typer


class QueryType(str, Enum):
    fetch = "fetch"
    execute = "execute"


def query_main(
    host: str,
    files: Optional[List[typer.FileText]] = typer.Argument(None),
    ssl: Optional[bool] = False,
    query_type: QueryType = QueryType.fetch
):
    if not files:
        print("No provided files")
        raise typer.Abort()

    database = Database(host)
    asyncio.run(database.connect())
    for f in files:
        query = f.read()
        if query_type == QueryType.fetch:
            typer.echo(asyncio.run(database.fetch_all(query)))
        else:
            typer.echo(asyncio.run(database.execute(query)))


def main():
    typer.run(query_main)


if __name__ == "__main__":
    main()
