from string import Formatter


class PathFormatter(Formatter):
    def format_field(self, value, format_spec):
        if format_spec != "/" and format_spec != "":
            raise ValueError(f"unknown path format_spec [{format_spec}]")

        return value


def format(pattern: str, *args, **kwargs):
    return PathFormatter().format(pattern, *args, **kwargs)


def parse(pattern: str) -> dict[str, str | None]:
    return {
        name: spec
        for _, name, spec, _ in PathFormatter().parse(pattern)
        if name is not None
    }
