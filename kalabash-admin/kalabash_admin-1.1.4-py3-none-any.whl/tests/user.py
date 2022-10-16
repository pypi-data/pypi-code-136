from django.core.urlresolvers import reverse

from kalabash.core.models import User
from kalabash.lib.tests import KalmonakTestCase

from ..factories import populate_database
from ..models import Alias


class ForwardTestCase(KalmonakTestCase):

    def setUp(self):
        super(ForwardTestCase, self).setUp()
        populate_database()

    def test_forward_permissions(self):
        self.clt.logout()
        self.clt.login(username='user@test.com', password='toto')
        self.ajax_post(
            reverse('user_forward'),
            {'dest': 'user@extdomain.com', 'keepcopies': True}
        )
        forward = Alias.objects.get(address='user@test.com', internal=False)
        sadmin = User.objects.get(username='admin')
        self.assertTrue(sadmin.can_access(forward))
        domadmin = User.objects.get(username='admin@test.com')
        self.assertTrue(domadmin.can_access(forward))
