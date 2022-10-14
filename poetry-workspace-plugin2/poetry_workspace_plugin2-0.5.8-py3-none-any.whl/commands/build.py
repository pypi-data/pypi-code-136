from poetry.console.commands.build import BuildCommand as BaseBuildCommand
from poetry.core.packages.dependency import Dependency
from poetry.core.packages.directory_dependency import DirectoryDependency
from poetry.core.pyproject.toml import PyProjectTOML


class RepositoryDependency(Dependency):
    def is_url(self):
        return True


def replace_dep(poetry_instance, dep, *, no_source_url=False):
    pyproject_toml = PyProjectTOML(dep.full_path / "pyproject.toml")
    if pyproject_toml.is_poetry_project():
        version = pyproject_toml.poetry_config.get("version")
        if not version:
            poetry_instance.io.write_line(
                f"<warning>No version property in project {dep.full_path}, using version '*'</warning>"
            )
            version = "*"
    else:
        poetry_instance.io.write_line(f"<warning>Not a Poetry project {dep.full_path}, using version '*'</warning>")
        version = "*"
    

    optional_kwargs = {}
    class_to_call = Dependency
    if no_source_url is False:
        optional_kwargs['source_url'] = dep.source_url
        optional_kwargs['source_reference'] = dep.source_reference
        optional_kwargs['source_resolved_reference'] = dep.source_resolved_reference
        optional_kwargs['source_type'] = dep.source_type
        optional_kwargs['constraint'] = version
    else:
        optional_kwargs['constraint'] = '*'
        class_to_call = RepositoryDependency
    return class_to_call(
        name=dep.name,
        optional=dep.is_optional(),
        groups=list(dep.groups),
        allows_prereleases=dep.allows_prereleases(),
        extras=dep.extras,
        **optional_kwargs
    )


def patch_poetry_dependencies(poetry_instance, attribute_name_to_patch='requires', no_source_url=False):
    # Replace directory dependencies specified by a path with one specified
    # by a version constraint.
    object_to_patch = getattr(poetry_instance.poetry.package, attribute_name_to_patch)
    for i, dep in enumerate(object_to_patch):
        if not isinstance(dep, DirectoryDependency):
            continue
        object_to_patch[i] = replace_dep(poetry_instance=poetry_instance, dep=dep, no_source_url=no_source_url)


class BuildCommand(BaseBuildCommand):
    def handle(self) -> int:
        patch_poetry_dependencies(self, no_source_url=True)
        return super().handle() or 0
