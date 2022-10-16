import os
from tornado import web
from multidict import MultiDict
from tornadmin.utils.template import get_value, get_chained_attr, get_list_display
from tornadmin.utils.text import replace_qs, pluralize, get_display_name
from tornadmin.utils.escape import conditional_xhtml_escape, mark_safe
from tornadmin.flash import FlashMixin


BASE_DIR = os.path.dirname(__file__)


class AdminUser:
    def __init__(self, username, **kwargs):
        self.username = username
        self.display_name = kwargs.get('display_name', username)

    def __bool__(self):
        if self.username:
            return True
        return False


class BaseHandler(web.RequestHandler, FlashMixin):
    admin_site = None

    async def prepare(self):
        auth_data = await self.admin_site.authenticate(self)
        if not auth_data:
            auth_data = {'username': None}

        self.current_user = AdminUser(**auth_data)

        if not self.current_user and getattr(self, 'login_required', True):
            return self.redirect(self.reverse_url('admin:login'))

    def redirect(self, url, *args, **kwargs):
        """Override handler's redirect method to be able to 
        redirect using url names.

        args will be passed to reversing function.
        kwargs will be passed to redirect function.
        """
        if (':' in url):
            # url is a route name
            url = self.reverse_url(url, *args)

        return super().redirect(url, **kwargs)

    def reverse_url(self, name, *args):
        """Override handler's reverse_url to strip question mark
        from the reversed url.
        """

        reversed_url = self.application.reverse_url(name, *[arg for arg in args if arg])
        return reversed_url.strip('?')

    def get_template_path(self):
        return os.path.join(os.path.dirname(__file__), 'templates')

    def get_template_namespace(self):
        namespace = super().get_template_namespace()
        namespace.update({
            'admin_site': self.admin_site,
            'get_value': get_value,
            'get_chained_attr': get_chained_attr,
            'replace_qs': replace_qs,
            'pluralize': pluralize,
            'get_list_display': get_list_display,
            'conditional_xhtml_escape': conditional_xhtml_escape,
            'mark_safe': mark_safe,
            'get_display_name': get_display_name,
        })
        return namespace

    def static_url(self, path, include_host=None, **kwargs):
        """We override RequestHandler's `static_url` to
        use our own static directory path instead of
        the value from `static_path` appication setting.

        :TODO: Provide a setting called `admin_static_path` so user can
        configure admin static files location.
        """
        if path.startswith('tornadmin'):

            get_url = self.settings.get(
                "static_handler_class", StaticFileHandler
            ).make_static_url

            if include_host is None:
                include_host = getattr(self, "include_host", False)

            if include_host:
                base = self.request.protocol + "://" + self.request.host + self.admin_site.base_url
            else:
                base = self.admin_site.base_url

            fake_settings = {
                'static_path': os.path.join(BASE_DIR, 'static'),
            }

            return base + get_url(fake_settings, path, **kwargs)

        else:
            return super().static_url(path, include_host, *args, **kwargs)

    def _static_url(self, path, *args, **kwargs):
        url = super().static_url(path, *args, **kwargs)
        if path.startswith('tornadmin'):
            url = self.admin_site.base_url + url
        return url


class StaticFileHandler(web.StaticFileHandler):
    def initialize(self):
        super().initialize(path=os.path.join(BASE_DIR, 'static'))


class LoginHandler(BaseHandler):
    login_required = False

    async def get(self):
        if self.current_user:
            return self.redirect('admin:index')

        namespace = {
            'error': False,
            'username': ''
        }

        self.render('login.html', **namespace)

    async def post(self):
        if self.current_user:
            return self.redirect('admin:index')

        success = await self.admin_site.login(self)

        if isinstance(success, tuple):
            success, message = success
        else:
            message = 'Wrong username or password'

        if success:
            self.clear_cookie("_xsrf") # OWASP recommends to reset XSRF token after login
            return self.redirect('admin:index')

        namespace = {
            'error': True,
            'message': message,
            'username': self.get_body_argument('username', '')
        }

        self.render('login.html', **namespace)

class LogoutHandler(BaseHandler):
    login_required = False

    async def post(self):
        if not self.current_user:
            return self.redirect('admin:login')

        success = await self.admin_site.logout(self)
        if success:
            return self.redirect('admin:login')

        self.redirect('admin:index')


class IndexHandler(BaseHandler):
    def get(self):
        registry = []

        _registry = self.admin_site.get_registry()

        for key, admin in _registry.items():
            registry.append(admin)

        namespace = {
            'registry': registry,
        }
        self.render('index.html', **namespace)


class ListHandler(BaseHandler):
    async def get(self, app_slug, model_slug):
        admin = self.admin_site.get_registered(app_slug, model_slug)

        page_num = self.get_query_argument('page', 1)
        q = self.get_query_argument('q', '')
        o = self.get_query_argument('o', '')

        filters = await admin.get_filters(self)

        filters_map = {}

        for filter_ in filters:
            indices = self.get_query_arguments(filter_['name'], [])

            for index in indices:
                if not indices:
                    continue

                try:
                    index = int(index)
                except ValueError:
                    continue

                value = filter_['options'][index][1]

                if value == '':
                    continue

                if filter_['type'] == 'checkbox':
                    if filter_['name'] not in filters_map:
                        filters_map[filter_['name']] = []
                    filters_map[filter_['name']].append(filter_['options'][index][1])
                else:
                    if filter_['name'] not in filters_map:
                        filters_map[filter_['name']] = filter_['options'][index][1]

        list_items, page = await admin.get_list(self, page_num=page_num, q=q, o=o, filters=filters_map)

        selected_filters = {}

        for key, value in filters_map.items():
            if not isinstance(value, list):
                value = [value]

            selected_filters[key] = value

        namespace = {
            'admin': admin,
            'headers': admin.get_list_headers(),
            'list_items': list_items,
            'page': page,
            'q': q,
            'o': o,
            'filters': filters,
            'selected_filters': selected_filters,
        }

        self.render('list.html', **namespace)

    async def post(self, app_slug, model_slug):
        admin = self.admin_site.get_registered(app_slug, model_slug)

        action_name = self.get_body_argument('_action')
        selected = self.get_body_arguments('_selected')
        selected_all = self.get_body_argument('_selected_all', False)

        action = admin.get_action(self, action_name)

        if action:
            if action.require_selection and (not selected and not selected_all) :
                self.flash('warning', 'Please select items to run this action. No action was performed.')
            else:
                queryset = await admin.get_action_queryset(self, action_name, selected, selected_all)

                if hasattr(admin, action_name):
                    await action(self, queryset)
                else:
                    await action(admin, self, queryset)

                if self._finished:
                    return
        else:
            self.flash('error', 'This action is not available')

        next_url = self.reverse_url('admin:list', app_slug, model_slug)
        if self.request.query:
            next_url += '?%s' % self.request.query
        return self.redirect(next_url)


class CreateHandler(BaseHandler):
    async def get(self, app_slug, model_slug):
        admin = self.admin_site.get_registered(app_slug, model_slug)
        form_class = admin.get_form(self)
        form = form_class()
        await form.set_field_choices(self)
        namespace = {
            'obj': None,
            'admin': admin,
            'form': form,
        }
        self.render('create.html', **namespace)

    async def post(self, app_slug, model_slug,):
        admin = self.admin_site.get_registered(app_slug, model_slug)
        form_class = admin.get_form(self)
        
        data = MultiDict()

        for field_name in form_class._fields:
            value = self.get_body_arguments(field_name, None)
            if value:
                data.extend(list(zip([field_name] * len(value), value)))
            else:
                data[field_name] = ''

        form = form_class(formdata=data)

        await form.set_field_choices(self)

        if form.validate():
            obj = await admin.save_model(self, form)
            self.flash('success', '1 item was created successfully')
            self.redirect('admin:detail', app_slug, model_slug, obj.id)
            return

        namespace = {
            'obj': None,
            'admin': admin,
            'form': form,
        }
        self.render('create.html', **namespace)



class DetailHandler(BaseHandler):
    async def get(self, app_slug, model_slug, id):
        admin = self.admin_site.get_registered(app_slug, model_slug)
        form_class = admin.get_form(self)
        obj = await admin.get_object(self, id)
        data = await admin.get_form_data(obj)

        form = form_class(data=data)
        await form.set_field_choices(self, obj=obj)

        namespace = {
            'obj': obj,
            'admin': admin,
            'form': form,
        }

        self.render('create.html', **namespace)

    async def post(self, app_slug, model_slug, id):
        admin = self.admin_site.get_registered(app_slug, model_slug)
        form_class = admin.get_form(self)
        obj = await admin.get_object(self, id)

        data = MultiDict()

        for field_name in form_class._fields:
            value = self.get_body_arguments(field_name, None)
            if value:
                data.extend(list(zip([field_name] * len(value), value)))
            else:
                data[field_name] = ''

        form = form_class(formdata=data)
        await form.set_field_choices(self, obj=obj)

        if form.validate():
            await admin.save_model(self, form, obj)
            self.flash('success', 'Item was changed successfully')
            if self.get_body_argument('_addanother', False):
                self.redirect('admin:create', app_slug, model_slug)
            else:
                self.redirect('admin:detail', app_slug, model_slug, obj.id)
            return

        namespace = {
            'obj': obj,
            'admin': admin,
            'form': form,
        }

        self.render('create.html', **namespace)


class DeleteHandler(BaseHandler):
    async def post(self, app_slug, model_slug, id):
        admin = self.admin_site.get_registered(app_slug, model_slug)
        form_class = admin.get_form(self)
        obj = await admin.get_object(self, id)

        # :TODO: check if user has delete permission
        await obj.delete()
        self.flash('success', '1 item was deleted successfully')

        self.redirect('admin:list', app_slug, model_slug)