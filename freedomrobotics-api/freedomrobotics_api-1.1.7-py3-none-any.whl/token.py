import logging

from .entity import Entity

logger = logging.getLogger(__name__)


class Token(Entity):
    pk = 'token'

    def __init__(self, _id, _data=None, account_id=None, *args, **kwargs):
        super(Token, self).__init__(_id, _data=_data, *args, **kwargs)
        self.account_id = account_id

    @property
    def url_base(self):
        if getattr(self, 'account_id', None) is None:
            return '/tokens'
        else:
            return '/accounts/{}/tokens'.format(self.account_id)

    @property
    def allowed_actions(self):
        return self._data['allowed_actions']

    @property
    def accounts(self):
        return self._data['accounts']

    @property
    def devices(self):
        return self._data['devices']

    @property
    def expiration_utc_secs(self):
        return self._data.get('expiration_utc_secs')

    @expiration_utc_secs.setter
    def expiration_utc_secs(self, value):
        self._data['expiration_utc_secs'] = value
