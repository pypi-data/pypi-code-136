from tornadmin.utils.text import get_display_name


def action(
    function=None,
    *,
    label=None,
    new_tab=False,
    require_selection=True,
    require_confirmation=False,
    modal_title=None,
    modal_body=None,
    modal_button_label=None,
    modal_button_class='primary'
):
    def decorator(func):
        nonlocal label
        
        if label is None:
            label = get_display_name(func.__name__)

        func.label = label
        func.new_tab = new_tab
        func.require_selection = require_selection
        func.require_confirmation = require_confirmation

        if require_confirmation:
            func.modal_title = modal_title or label
            func.modal_body = modal_body or modal_title or label
            func.modal_button_label = modal_button_label or label
            func.modal_button_class = modal_button_class

        return func

    if function:
        return decorator(function)

    return decorator
