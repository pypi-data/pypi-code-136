"""Main module."""
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.edge_names = []

    def add_edge(self, node):
        self.edges.append(node)

    def add_edge_name(self, node):
        self.edge_names.append(node)

    def to_string(self):
        return f"{self.name} -> {[edge.name for edge in self.edges]}"


class DependencyResolver:
    def __init__(self):
        self.node_list = []
        self.resolved_list = []

    def process_dependency_list(self, dependency_list):
        for nod in dependency_list:
            n = Node(nod.get('id'))

            for dependency in nod.get('dependencies'):
                n.add_edge_name(dependency)

            self.node_list.append(n)

        for node in self.node_list:
            for name in node.edge_names:
                dep_node = self.get_node(name)
                if dep_node:
                    node.add_edge(dep_node)
                else:
                    node.add_edge(Node(name))

    def get_node(self, node_name):
        for node in self.node_list:
            if node.name == node_name:
                return node

    def dep_resolve(self, node: Node, resolved, unresolved):
        unresolved.append(node)
        for edge in node.edges:
            if edge not in resolved:
                if edge in unresolved:
                    print(f'Circular reference detected: {node.name} -> {edge.name}')
                self.dep_resolve(edge, resolved, unresolved)
        resolved.append(node)
        unresolved.remove(node)

    def simple_resolution(self, dependency_list):
        """
        format [{"id": 1, "dependencies": [1,2,3]}]
        """
        self.process_dependency_list(dependency_list)
        resolved = []
        for node in self.node_list:
            if node.name not in [r.name for r in resolved]:
                self.dep_resolve(node, resolved, [])

        clean_resolved = [r for r in resolved if r.name in [s.name for s in self.node_list]]

        return clean_resolved
