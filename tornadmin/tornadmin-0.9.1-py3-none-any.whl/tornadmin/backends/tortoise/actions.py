from tornadmin.decorators import action
from tornadmin.utils.text import pluralize


@action(
    label='Delete selected',
    require_confirmation=True,
    modal_title='Delete selected?',
    modal_body='Are you sure you want to permanently delete selected items? This action can\'t be undone.',
    modal_button_label='Delete',
    modal_button_class='outline-danger'
)
async def delete_selected(admin, request_handler, queryset):
    count = await queryset.count()
    if count:
        await queryset.delete()
        request_handler.flash('success', 'Successfully deleted %s %s' % (count, pluralize('item', 'items', count)))
