# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SpillthebeansThreejs(Component):
    """A SpillthebeansThreejs component.


Keyword arguments:

- id (string; required):
    The ID used to identify the container for the IFC viewer
    component.

- canAngle (number; required)

- rotation (number; default 0.01)

- scale (number; default 0.5)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'spillthebeans_threejs'
    _type = 'SpillthebeansThreejs'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, canAngle=Component.REQUIRED, scale=Component.UNDEFINED, rotation=Component.UNDEFINED, axis=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'canAngle', 'rotation', 'scale']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'canAngle', 'rotation', 'scale']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'canAngle']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(SpillthebeansThreejs, self).__init__(**args)
