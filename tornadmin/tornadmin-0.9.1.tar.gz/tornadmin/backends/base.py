class BaseModelAdmin:
    list_headers = []
    items_per_page = 20
    fields = []
    exclude = []
    prefetch_fields = []
    readonly_fields = []
    actions = []
    filters = []
    order_by = []

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('Implement in subclass')

    def get_list_headers(self):
        raise NotImplementedError('Implement in subclass')

    async def get_list(self, request_handler, page_num, q, o):
        raise NotImplementedError('Implement in subclass')

    async def get_object(self, request_handler, id):
        raise NotImplementedError('Implement in subclass')

    async def get_form_data(self, obj):
        raise NotImplementedError('Implement in subclass')

    def get_form(self, request_handler):
        raise NotImplementedError('Implement in subclass')

    async def save_model(self, request_handler, form, obj=None):
        raise NotImplementedError('Implement in subclass')

    def get_absolute_url(self, request_handler, obj):
        return None

    async def get_action_queryset(self, request_handler, action_name, selected, selected_all):
        raise NotImplementedError('Implement in subclass')

    def get_actions(self, request_handler):
        actions = []

        for action in self.actions:
            if isinstance(action, str):
                actions.append(getattr(self, action))
            else:
                actions.append(action)

        return actions

    def get_action(self, request_handler, name):
        actions = self.get_actions(request_handler)

        for action in actions:
            if action.__name__ == name:
                return action

    async def get_filters(self, request_handler):
        return self.filters

    async def get_fitlered_results(self, request_handler, filters):
        raise NotImplementedError('Implement in subclass')

    def get_order_by(self, request_handler):
        return self.order_by
