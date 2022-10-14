from poetry.packages.dependency_package import DependencyPackage
from poetry.core.packages.directory_dependency import DirectoryDependency
from unittest import mock
from poetry_workspace.commands.build import replace_dep
from poetry_plugin_export.command import ExportCommand as BaseExportCommand
from poetry_plugin_export import exporter
from poetry_plugin_export.exporter import get_project_dependency_packages as original_get_project_dependency_packages
from poetry.core.packages.package import Package


class ExportCommand(BaseExportCommand):
    def handle(self) -> int:
        from .build import patch_poetry_dependencies
        patch_poetry_dependencies(self, no_source_url=True)
        patch_poetry_dependencies(self, attribute_name_to_patch='all_requires', no_source_url=True)
        def wrap_get_project_dependency_packages(*args, **kwargs):
            for answer in original_get_project_dependency_packages(*args, **kwargs):
                if isinstance(answer._dependency, DirectoryDependency):
                    dependency = replace_dep(
                        poetry_instance=self,
                        dep=answer._dependency,
                        no_source_url=True
                    )

                    package = Package(
                        name=answer._package.name,
                        pretty_version=answer._package.pretty_version,
                        source_type=None,
                        source_url=None,
                        version=answer._package.version
                    )
                    answer = DependencyPackage(
                        dependency=dependency,
                        package=package
                    )

                yield answer

        with mock.patch.object(exporter, 'get_project_dependency_packages', wrap_get_project_dependency_packages):
            return super().handle() or 0