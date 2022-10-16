from unittest.mock import MagicMock
from tornado import testing, web, httputil
from tornadmin import BaseAdminSite, AdminRouter, uimodules

from admin import TestModelAdmin


class UserAdmin(TestModelAdmin):
    pass

class UserModel(MagicMock):
    __name__ = 'User'


class AdminSite(BaseAdminSite):
    pass

admin_site = AdminSite(base_url='/admin')

admin_site.register(UserAdmin(model=UserModel, app='general', slug='user'))



app = web.Application(
    [AdminRouter(admin_site)],
    ui_modules=[uimodules],
    debut=True,
)


class CommonHandlerTests(testing.AsyncHTTPTestCase):
    def setUp(self):
        list_route = '/admin/general/user/'
        create_route = '/admin/general/user/add/'
        delete_route = '/admin/general/'


class ListHandlerTests(testing.AsyncHTTPTestCase):
    def get_app(self):
        return app

    def _test_list_headers(self):
        # Must work with callables, string fields and methods
        self.fetch('/admin/general/user')
