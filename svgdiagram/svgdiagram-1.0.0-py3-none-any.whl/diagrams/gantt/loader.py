from .gantt_content import GanttGroup, GanttContent
from .swimlane import Swimlane
import os


class GanttLoader:
    def __init__(self):
        self.file_pathes = []
        self.groups = []
        self.swimlanes = []
        self.dependencies = []

    def walk_dir(self, dir):
        for path, _, filenames in os.walk(dir):
            for filename in filenames:
                if filename.endswith('.json'):
                    self.file_pathes.append(os.path.join(path, filename))

    def _append_for_groups(self, groups):
        swimlanes = {}
        swimlane_order = []

        for group in groups:
            if group.swimlane_order:
                assert not swimlane_order, \
                    "Multiple Swimlane Orders Provided!"
                swimlane_order = group.swimlane_order
            for swimlane in group.swimlanes:
                curr_swimlane = swimlanes.get(
                    swimlane.name,
                    Swimlane(name=swimlane.name),
                )
                curr_swimlane.milestones.extend(swimlane.milestones)
                curr_swimlane.tasks.extend(swimlane.tasks)
                swimlanes[swimlane.name] = curr_swimlane

            self.dependencies.extend(group.dependencies)

        if swimlane_order:
            for name in swimlane_order:
                self.swimlanes.append(swimlanes[name])
        else:
            self.swimlanes.extend(swimlanes.values())

    def create_content(self):
        file_pathes = sorted(self.file_pathes)
        for file_path in file_pathes:
            self.groups.append(GanttGroup.parse_file(file_path))

        group_ids = list(map(lambda x: x.group_id, self.groups))
        has_group_id = list(map(lambda x: bool(x), group_ids))
        no_group_id = list(map(lambda x: not bool(x), group_ids))

        assert all(has_group_id) or all(no_group_id), \
            "Either all groups must have group_id or none!"

        if all(has_group_id):
            unique_group_ids = sorted(list(set(group_ids)))

            for group_id in unique_group_ids:
                group_groups = list(filter(
                    lambda x: x.group_id == group_id,
                    self.groups,
                ))
                self._append_for_groups(group_groups)
        else:
            self._append_for_groups(self.groups)

        return GanttContent(
            swimlanes=self.swimlanes,
            dependencies=self.dependencies
        )
