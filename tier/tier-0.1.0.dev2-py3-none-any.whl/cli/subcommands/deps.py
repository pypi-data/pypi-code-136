# std
from typing import List

# internal
from tier.internal.logging import log
from tier.internal.tier import Tier
from tier.internal.configs.pyproject import PyProject


def deps():
    log.debug('tier deps')
    tier = Tier()
    projects: List[PyProject] = list(reversed(tier.projects()))
    print('.')
    for i, project in enumerate(projects):
        package_name = project.get_build_system().get_package_name()
        if i < len(projects) - 1:
            print(f'├── {package_name}')
        else:
            print(f'└── {package_name}')
        dependencies = tier.graph.get_internal_dependency_names(package_name)
        for group_name in project.get_build_system().get_group_names():
            group_dependencies = tier.graph.get_internal_dependency_names(package_name, group_name)
            dependencies.extend(group_dependencies)
        for j, dependency_name in enumerate(dependencies):
            if j < len(dependencies) - 1:
                print(f'│   ├── {dependency_name}')
            else:
                print(f'│   └── {dependency_name}')
