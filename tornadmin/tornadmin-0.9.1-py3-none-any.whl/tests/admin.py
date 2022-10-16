"""Admin class for tests"""
from tornadmin.backends.base import BaseModelAdmin
from tornadmin.utils.text import split_camel, slugify

class TestModelAdmin(BaseModelAdmin):
    def __init__(self, model, **kwargs):
        name = model.__name__

        self.model = model
        self.name = kwargs.get('name', ' '.join(split_camel(name)))
        self.slug = kwargs.get('slug', name.lower())
        self.app = kwargs['app']
        self.app_slug = slugify(self.app)
