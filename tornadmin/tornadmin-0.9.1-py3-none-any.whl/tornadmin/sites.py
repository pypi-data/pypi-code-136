import copy


class BaseAdminSite:
    """The class is responsible for generating the admin site."""
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.site_name = kwargs.get('site_name', 'Tornadmin')

        self._registry = {}

    async def authenticate(self, handler):
        """Returns the authenticated user for the current request.

        By default, we return a fake user to make the site
        accessible which is useful for quickstarting.

        Override it in subclass with custom logic.

        It must return None or False if the user doesn't authenticate,
        or return a dict containing at least a username key
        set to a truthy value:

            {
                'username': <username> or True,
                'desplay_name': <display name>, # optional
            }
        """
        return {'username': 'tornadmin_test_user', 'display_name': 'Test User'}

    async def login(self, handler):
        """Method responsible for logging a user in.

        Override this in subclass.

        It must return a boolean:

        - True if login succeeds or
        - False if it fails

        You can also supply custom error message when login fails by returning a tuple:
        - False, 'Custom error message'
        """
        pass

    async def logout(self, handler):
        """Method responsible for logging a user out.

        Override this in subclass.

        It must return a boolean:

        - True if logout succeeds or
        - False if it fails
        """
        pass

    @classmethod
    def get_registry_key(cls, model_admin):
        """Returns the key used in self._registry dict for the given model"""
        return '.'.join([model_admin.app_slug, model_admin.slug]).strip('.')

    def register(self, model_admin):
        key = self.get_registry_key(model_admin)

        if key in self._registry:
            return

        self._registry[key] = model_admin

    def get_registry(self):
        return copy.deepcopy(self._registry)

    def get_registered(self, app_slug, model_slug):
        key = '.'.join([app_slug, model_slug]).strip('.')
        return self._registry.get(key, (None, None))
