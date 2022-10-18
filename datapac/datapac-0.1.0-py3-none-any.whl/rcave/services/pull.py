from datapac.package.package import Package
from datapac.rcave.sources.postgres import source as postgres
from datapac.rcave.sources.s3 import source as s3
from datapac.rcave.utils.graph import Graph
from datapac.rcave.utils.graph import PostgresNode
from datapac.rcave.utils.graph import S3Node
from datapac.utils.environment import Environment


def pull(
    env: Environment,
    graph: Graph,
    variables: dict,
    pkg: Package,
):
    for artefact in crawl(env, graph, variables):
        pkg.add_artefact(artefact)


def crawl(env: Environment, node: Graph, variables: dict):
    if isinstance(node, PostgresNode):
        for result in postgres.pull_node(env, node, variables):
            yield result

            for child in node.relationships:
                yield from crawl(env, child, variables | {"parent": result.data})
    elif isinstance(node, S3Node):
        yield s3.pull_node(env, node, variables)
    else:
        raise ValueError(f"unknown node: {node}")
