from tornado import web


class SideNav(web.UIModule):
    def render(self, handler):
        """menu structure:

            {
                app_name: [ModelAdmin1, ModelAdmin2, ...],
                ...
            }
        """
        menu = {}

        _registry = handler.admin_site.get_registry()

        if handler.path_kwargs:
            # :TODO: Use BaseAdminSite's get_registry_key method to generate key
            active_key = '%s.%s' % (handler.path_kwargs['app_slug'], handler.path_kwargs['model_slug'])
        else:
            active_key = ''
        active_item = None # Home

        for index, (key, admin) in enumerate(_registry.items()):
            if admin.app not in menu:
                menu[admin.app] = []

            menu[admin.app].append(admin)
            if key == active_key:
                active_item = admin

        return self.render_string('modules/side-nav.html', menu=menu, active_item=active_item)
