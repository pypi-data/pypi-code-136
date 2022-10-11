"""Utility functions."""
import os

from copy import deepcopy
from jinja2 import Environment


def merge_settings(base: dict, new: dict) -> dict:
    """Return a new dictionary created by merging the settings from ``new`` into ``base``.

    :param base: The base dictionary to merge into
    :type base: ``dict``
    :param new: The new dictionary to merge
    :type new: ``dict``
    :return: A new merged dictionary
    :rtype: ``dict``
    """
    result = {}

    for base_key, base_value in list(base.items()):
        if base_key not in new:
            result[base_key] = deepcopy(base_value)
        else:
            if isinstance(base_value, list):
                result[base_key] = list(base_value + new[base_key])
            elif isinstance(base_value, dict):
                result[base_key] = merge_settings(base_value, new[base_key])
            else:
                result[base_key] = new[base_key]
    for new_key, new_value in list(new.items()):
        if new_key not in base:
            result[new_key] = deepcopy(new_value)
    return result


def render_template(context: str, env: Environment, template_path: str, output_path: str, variables: dict) -> None:
    """Render a jinja2 template.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param template_path: The path to the template to render
    :type template_path: str
    :param output_path: The path to output the result to
    :type output_path: str
    :param variables: The variables to pass to the template
    :type variables: dict
    """
    target_path = os.path.join(context, output_path)
    if not os.path.exists(os.path.dirname(target_path)):
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w') as out_f:
        tmpl = env.get_template(template_path)
        rendered = tmpl.render(**variables)
        if not rendered.endswith('\n'):
            rendered = f'{rendered}\n'
        out_f.write(rendered)
