from datapac.package.artefact import Artefact
from datapac.package.package import match_files
from datapac.package.path import format
from datapac.rcave.sources.postgres import client
from datapac.rcave.utils.graph import PostgresNode
from datapac.utils import templating
from datapac.utils.environment import Environment
from datapac.utils.json import append_json
from datapac.utils.json import read_json


class PostgresArtefact(Artefact):
    source = "postgres"

    table: str
    data: dict

    def __str__(self):
        return f"postgres({self.table})"

    @property
    def output_path(self):
        return format(get_output_path(), table=self.table)

    def write(self, path: str):
        append_json(path, self.data)

    def map(self, variables):
        def render(v):
            if type(v) == str:
                return templating.render(v, variables)

            return v

        return PostgresArtefact(
            table=self.table,
            data={k: render(v) for k, v in self.data.items()},
        )


def load_artefacts(path: str):
    files = match_files(path, get_output_path())

    for path, kwargs in files:
        for item in read_json(path):
            yield PostgresArtefact(data=item, **kwargs)


def get_output_path() -> str:
    return "artefacts/postgres/{table}.json"


def pull_node(env: Environment, node: PostgresNode, variables: dict):
    with client.connect(env.postgres_url) as conn:
        where_compiled = {
            k: templating.render(v, variables) for k, v in node.where.items()
        }

        for result in client.select(conn, node.table, where_compiled):
            artefact = PostgresArtefact(
                table=node.table,
                data=result,
            )

            print(f"[source:postgres] pulling {artefact} artefact")

            yield artefact


def push_artefacts(env: Environment, artefacts: list[PostgresArtefact]):
    with client.connect(env.postgres_url) as conn:
        with client.disabled_contraints(conn):
            for artefact in artefacts:
                print(f"importing {artefact.table}")
                client.insert(conn, artefact.table, artefact.data)

        conn.commit()
