# std
from __future__ import annotations
import os
from typing import Iterable, List, Optional as Opt

# internal
from tier.internal.graph import Graph, Vertex
from tier.internal.configs.pyproject import PyProject


class DependencyGraph(Graph[PyProject]):

    def __init__(self, *vertices: Vertex[PyProject]):
        super().__init__(*vertices)
        self.vertices_by_package_name = {
            v.data.get_build_system().get_package_name(): v for v in vertices
        }

    def __contains__(self, package_name: str) -> bool:
        return package_name in self.vertices_by_package_name

    def get_package_names(self) -> List[str]:
        return list(self.vertices_by_package_name.keys())

    def get_project(self, package_name: str) -> PyProject:
        return self.vertices_by_package_name[package_name].data

    def filter_internal_dependencies(self, dependency_names: Iterable[str]) -> List[str]:
        return [name for name in dependency_names if name in self]

    def get_internal_dependency_names(
            self,
            package_name: str,
            group_name: Opt[str] = None,
    ) -> List[str]:
        bs = self.get_project(package_name).get_build_system()
        return self.filter_internal_dependencies(bs.get_dependencies(group_name))

    def get_internal_dependency_vertices(
            self,
            package_name: str,
            group_name: Opt[str] = None,
    ) -> List[Vertex]:
        return [
            self.vertices_by_package_name[d]
            for d in self.get_internal_dependency_names(package_name, group_name)
        ]

    def get_internal_dependency_projects(
            self,
            package_name: str,
            group_name: Opt[str] = None,
    ) -> List[PyProject]:
        return [v.data for v in self.get_internal_dependency_vertices(package_name, group_name)]

    @classmethod
    def create(cls, dirpath: Opt[str] = None) -> DependencyGraph:
        dirpath = dirpath or os.getcwd()
        vertices = {
            project.get_build_system().get_package_name(): Vertex(project)
            for project in PyProject.find_recursively(dirpath)
        }
        graph = DependencyGraph(*vertices.values())
        for package_name, package_vertex in vertices.items():
            for dependency_name in graph.get_internal_dependency_names(package_name):
                if dependency_name in vertices:
                    dependency_vertex = vertices[dependency_name]
                    graph.add_edge(package_vertex, dependency_vertex)
        return graph
