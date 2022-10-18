from jinja2 import DebugUndefined
from jinja2 import StrictUndefined
from jinja2 import Template


def render(template: str, context: dict) -> str:
    return Template(template, undefined=StrictUndefined).render(**context)


def partial_render(template: str, context: dict) -> str:
    return Template(template, undefined=DebugUndefined).render(**context)
