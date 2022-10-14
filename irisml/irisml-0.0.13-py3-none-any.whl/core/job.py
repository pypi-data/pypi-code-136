import itertools
from .task import Task


class Job:
    def __init__(self, description):
        self._description = description
        self._tasks = [Task(t) for t in description.tasks]
        self._on_error = [Task(t) for t in description.on_error] if description.on_error else []

        # Assign uniqe names to the tasks.
        used_names = set()
        for t in itertools.chain(self._tasks, self._on_error):
            if t.name in used_names:
                count = int(t.name.split('@')[1]) if '@' in t.name else 1
                while True:
                    count += 1
                    new_name = t.name.split('@')[0] + f'@{count}'
                    if new_name not in used_names:
                        break
                t.name = new_name
            used_names.add(t.name)

    @property
    def tasks(self):
        for t in self._tasks:
            yield t

    @property
    def on_error(self):
        for t in self._on_error:
            yield t

    def load_modules(self):
        for t in itertools.chain(self.tasks, self.on_error):
            try:
                t.load_module()
            except Exception as e:
                raise RuntimeError(f"Failed to load {t.name}") from e

    def __str__(self):
        return "Job {\n" + '\n'.join([f"  {t}" for t in self.tasks]) + '\n}'
