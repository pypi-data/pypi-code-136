# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modal(Component):
    """A Modal component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Provide the contents of your Modal.

- id (string; optional):
    Specify the DOM element ID of the top-level node.

- alert (boolean; optional):
    Specify whether the Modal is displaying an alert, error or warning
    Should go hand in hand with the danger prop.

- className (string; optional):
    Specify an optional className to be applied to the modal root
    node.

- closeButtonLabel (string; optional):
    Specify an label for the close button of the modal; defaults to
    close.

- close_n_clicks (number; default 0):
    Number of times close button has been clicked.

- danger (boolean; optional):
    Specify whether the Modal is for dangerous actions.

- hasScrollingContent (boolean; optional):
    Specify whether the modal contains scrolling content.

- modalAriaLabel (string; optional):
    Specify a label to be read by screen readers on the modal root
    node.

- modalHeading (a list of or a singular dash component, string or number; optional):
    Specify the content of the modal header title.

- modalLabel (a list of or a singular dash component, string or number; optional):
    Specify the content of the modal header label.

- open (boolean; optional):
    Specify whether the Modal is currently open.

- passiveModal (boolean; optional):
    Specify whether the modal should be button-less.

- preventCloseOnClickOutside (boolean; optional):
    Prevent closing on click outside of modal.

- primaryButtonDisabled (boolean; optional):
    Specify whether the Button should be disabled, or not.

- primaryButtonText (a list of or a singular dash component, string or number; optional):
    Specify the text for the primary button.

- secondaryButtonText (a list of or a singular dash component, string or number; optional):
    Specify the text for the secondary button.

- secondary_submit_n_clicks (number; default 0):
    Number of times secondary submit button has been clicked.

- selectorPrimaryFocus (string; optional):
    Specify a CSS selector that matches the DOM element that should be
    focused when the Modal opens.

- selectorsFloatingMenus (list of strings; optional):
    Specify CSS selectors that match DOM elements working as floating
    menus. Focusing on those elements won't trigger \"focus-wrap\"
    behavior.

- shouldSubmitOnEnter (boolean; optional):
    Specify if Enter key should be used as \"submit\" action.

- size (a value equal to: 'xs', 'sm', 'md', 'lg'; optional):
    Specify the size variant.

- submit_n_clicks (number; default 0):
    Number of times submit button has been clicked."""
    _children_props = ['modalHeading', 'modalLabel', 'primaryButtonText', 'secondaryButtonText']
    _base_nodes = ['modalHeading', 'modalLabel', 'primaryButtonText', 'secondaryButtonText', 'children']
    _namespace = 'dash_carbon_components'
    _type = 'Modal'
    @_explicitize_args
    def __init__(self, children=None, alert=Component.UNDEFINED, className=Component.UNDEFINED, closeButtonLabel=Component.UNDEFINED, danger=Component.UNDEFINED, hasScrollingContent=Component.UNDEFINED, id=Component.UNDEFINED, modalAriaLabel=Component.UNDEFINED, modalHeading=Component.UNDEFINED, modalLabel=Component.UNDEFINED, open=Component.UNDEFINED, passiveModal=Component.UNDEFINED, preventCloseOnClickOutside=Component.UNDEFINED, primaryButtonDisabled=Component.UNDEFINED, primaryButtonText=Component.UNDEFINED, secondaryButtonText=Component.UNDEFINED, selectorPrimaryFocus=Component.UNDEFINED, selectorsFloatingMenus=Component.UNDEFINED, shouldSubmitOnEnter=Component.UNDEFINED, size=Component.UNDEFINED, close_n_clicks=Component.UNDEFINED, submit_n_clicks=Component.UNDEFINED, secondary_submit_n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'alert', 'className', 'closeButtonLabel', 'close_n_clicks', 'danger', 'hasScrollingContent', 'modalAriaLabel', 'modalHeading', 'modalLabel', 'open', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'secondary_submit_n_clicks', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'shouldSubmitOnEnter', 'size', 'submit_n_clicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alert', 'className', 'closeButtonLabel', 'close_n_clicks', 'danger', 'hasScrollingContent', 'modalAriaLabel', 'modalHeading', 'modalLabel', 'open', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'secondary_submit_n_clicks', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'shouldSubmitOnEnter', 'size', 'submit_n_clicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Modal, self).__init__(children=children, **args)
