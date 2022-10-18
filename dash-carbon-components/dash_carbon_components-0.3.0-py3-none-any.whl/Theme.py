# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Theme(Component):
    """A Theme component.


Keyword arguments:

- children (optional):
    Provide the contents of your GlobalTheme.

- id (optional):
    Specify the DOM element ID of the top-level node.

- as (optional):
    Specify a custom component or element to be rendered as the
    top-level element in the component.

- className (optional):
    Provide a custom class name to be used on the outermost element
    rendered by the component.

- theme (optional):
    Specify the theme for your entire project."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_carbon_components'
    _type = 'Theme'
    @_explicitize_args
    def __init__(self, children=None, theme=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'as', 'className', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as', 'className', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Theme, self).__init__(children=children, **args)
