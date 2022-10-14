import dataclasses
import graphlib

import graphviz
from makeit.core import DAG, _Task, _Artifact, Artifact, DataclassTask, SourceCodeOf, File

import re


def _(name: str):
    """ Try to shorten artifact labels """

    if name.startswith("makeit.core.SourceCodeOf"):
        name = name.removeprefix("makeit.core.SourceCodeOf")
        name = name.replace("__main__.", "")
        name = name.lstrip("(").rstrip(")")
    elif name.startswith("makeit.core.File"):
        name = name.removeprefix('makeit.core.File(')
        name = name.removesuffix(')')
        name = name

    # search for hashes
    if m := re.search(r"__([0-9]|[a-z]){32}", name):
        name = name.replace(m.group(), m.group()[:8] + ".." + m.group()[-1])

    name = name.replace(':', '')  # strange bug in Graphviz

    return graphviz.escape(name)


def task_style_by_label(label) -> dict:
    return dict(shape="oval")


def artifact_style_by_label(label, artifact: Artifact) -> dict:
    if label.startswith("makeit.core.SourceCodeOf"):
        return dict(shape="parallelogram", )
    elif label.startswith("makeit.core.File"):
        if isinstance(artifact, File):
            if artifact.exists():
                return dict(shape="tab", color='green')
            else:
                return dict(shape="tab", color='red')
        else:
            return dict(shape="tab", )

    return dict(shape="rectangle")


@dataclasses.dataclass
class FilterOutNodes:
    show_source_dep: bool

    def keep(self, node: _Task | _Artifact):
        if isinstance(node, _Artifact):
            if isinstance(node.obj, SourceCodeOf):
                return self.show_source_dep
            else:
                return True
        else:
            return True


def create_dot(tasks: list, dag_name="main", show_source_dep=False) -> graphviz.Digraph:
    dag = DAG(dag_name)
    rules = FilterOutNodes(show_source_dep)

    for task in tasks:
        dag.add(task)

    dot = graphviz.Digraph(dag_name)

    # check that shortening works well:
    seen = set()
    for label in dag.name2obj.keys():
        if _(label) in seen:
            raise RuntimeError(f"Unable to shorten labels in DAG: {label} -> {_(label)} clashes.")

        seen.add(_(label))

    for label, obj in dag.name2obj.items():
        if not rules.keep(obj):
            continue

        if isinstance(obj, _Task):
            dot.node(_(label), **task_style_by_label(label))
        elif isinstance(obj, _Artifact):
            dot.node(_(label), **artifact_style_by_label(label, obj.obj))

    for label, task in dag.tasks.items():
        if not rules.keep(task):
            continue

        for tar in task.tars.keys():
            if not rules.keep(dag.name2obj[tar]):
                continue

            dot.edge(_(label), _(tar), arrowhead="vee")

        for dep in task.deps.keys():
            if not rules.keep(dag.name2obj[dep]):
                continue

            dot.edge(_(dep), _(label), arrowhead="vee")

        if isinstance(task.obj, DataclassTask):
            for name, type_, o in task.obj.parameters():
                o = f"{o}"
                if len(o) > 10:
                    o = "..."
                parameter = f"{name}={o}"
                dot.node(parameter, shape="plain")
                dot.edge(parameter, _(label), arrowhead="none", style="dashed")

    # step 2: set ranks
    graph = dag.create_dep_graph()

    ts = graphlib.TopologicalSorter(graph.dep_graph)
    ts.prepare()

    while ts.is_active():
        nodes = ts.get_ready()

        c = graphviz.Digraph()
        c.attr(rank="same")

        for node in nodes:
            if rules.keep(dag.name2obj[node]):
                c.node(_(node))

            ts.done(node)

        dot.subgraph(c)

    return dot


def render_online(dot: graphviz.Digraph, service_url: str, open_url=True):
    """ Renders graphviz online.
        service_url -- can be used something similar to 'https://dreampuf.github.io/GraphvizOnline/#'
    """
    import urllib.parse
    import webbrowser

    url = service_url + urllib.parse.quote(dot.source, safe='')
    print(f'{url}')

    if open_url:
        webbrowser.open(url, )

