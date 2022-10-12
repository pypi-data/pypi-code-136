import networkx as nx

from typing import List, Union

from orkg import ORKG


def subgraph(client: ORKG, thing_id: str, blacklist: Union[str, List[str]] = '', max_level: int = -1) -> nx.DiGraph:
    """
    Obtains a networkx directed graph representation of any ORKG component given by its thing_id.
    E.g. of ORKG components: Paper, Contribution, Comparison, Template

    It starts from the thing_id resource and traverses the graph until all literals are reached.

    :param client: orkg.ORKG client used to connect with ORKG backend.
    :param thing_id: Any subject, object or predicate ID in the ORKG.
    :param blacklist: Class(es) to be excluded from the subgraph. E.g. 'ResearchField'
        (see `orkgc:ResearchField <https://orkg.org/class/ResearchField>`_).
        Note that the first subgraph level will always be included.
    :param max_level: Deepest subgraph's level to traverse.
    """
    blacklist = [blacklist] if isinstance(blacklist, str) else blacklist

    response = client.statements.bundle(thing_id, params={
        'includeFirst': 'true',
        'blacklist': ','.join(blacklist),
        'maxLevel': max_level
    })

    if not response.succeeded:
        raise ValueError('Something went wrong while connecting to ORKG backend with host {}'.format(client.host))

    statements = response.content['statements']

    if not statements:
        raise ValueError('Nothing found for the provided ID: {}'.format(thing_id))

    return _construct_subgraph(nx.DiGraph(), statements)


def _construct_subgraph(subgraph: nx.DiGraph, statements: list) -> nx.DiGraph:
    """
    Constructs a subgraph represented by the given RDF ``statements``.

    :param subgraph: Initial networkx.DiGraph to extend with nodes and edges.
    :param statements: List of all RDF statements describing the subgraph.
    """
    for statement in statements:
        # NetworkX does not create a node or an edge double, therefore, the following implementation works :)
        start_node = _create_node_from_thing(subgraph, statement['subject'])
        target_node = _create_node_from_thing(subgraph, statement['object'])
        _create_edge(subgraph, start_node, target_node, statement['predicate'])

    return subgraph


def _create_node_from_thing(subgraph: nx.DiGraph, thing: dict) -> str:
    subgraph.add_node(
        node_for_adding=thing['id'],
        id=thing['id'],
        label=thing['label'],
        class_=thing['_class'],
        classes=thing.get('classes', []),
        description=thing.get('description', ''),
        datatype=thing.get('datatype', '')
    )
    return thing['id']


def _create_edge(subgraph: nx.DiGraph, root_node: str, target_node: str, predicate) -> None:
    subgraph.add_edge(
        root_node,
        target_node,
        id=predicate['id'],
        label=predicate['label'],
        class_=predicate['_class'],
    )
