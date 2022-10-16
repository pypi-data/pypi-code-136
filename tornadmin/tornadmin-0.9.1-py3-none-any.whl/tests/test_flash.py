from unittest.mock import MagicMock
from tornado import testing, web, httputil
from tornadmin.flash import FlashMixin, flash_cookie_encoder, flash_cookie_decoder


flash_message = ('success', 'Success happend')


class TestHandler(web.RequestHandler, FlashMixin):
    """For testing with http client"""
    def get(self):
        """Sets flash messages.

        Query parameters to customise behaviour:

            num: specify the number of messages to flash
            redirect: specify the redirect location
            load_messages: whether to call get_flashed_messages method or not
            
        """
        num = int(self.get_query_argument('num', 1))
        redirect = self.get_query_argument('redirect', False)
        load_messages = self.get_query_argument('load_messages', False)

        for x in range(num):
            self.flash(*flash_message)

        if redirect:
            return self.redirect(redirect)

        if load_messages:
            self.get_flashed_messages()


class FlashMixinTests(testing.AsyncHTTPTestCase):
    def get_app(self):
        return web.Application(
            [
                (r'/', TestHandler),
            ]
        )

    def get_request(self, **kwargs):
        """Returns a request object to instantiate handler.
    
        kwargs are passed to the request.
        """
        defaults = {
            'method': 'GET',
            'uri': '/',
            'connection': MagicMock(),
        }

        defaults.update(kwargs)

        return httputil.HTTPServerRequest(**defaults)
        response = self.fetch('/')
        
        # test cookie is set
        self.assertIn('flash=', response.headers.get('set-cookie'))

        # test cookie value
        for cookie in response.headers.get_list('set-cookie'):
            cookie_dict = httputil.parse_cookie(cookie)
            if 'flash' in cookie_dict:
                break

        value = cookie_dict['flash']

        self.assertEqual(len(flash_cookie_decoder(value)), 1)
        self.assertEqual(flash_cookie_decoder(value)[0], flash_message)

    def test_flash_cookie_with_multiple_messages(self):
        response = self.fetch('/?num=2')
        
        for cookie in response.headers.get_list('set-cookie'):
            cookie_dict = httputil.parse_cookie(cookie)
            if 'flash' in cookie_dict:
                break

        value = cookie_dict['flash']

        self.assertEqual(len(flash_cookie_decoder(value)), 2)

    def test_cookie_is_cleared_when_messages_are_accessed(self):
        # 1. Test with existing cookie and new flash
        response = self.fetch('/?load_messages=True',
            headers={'Cookie': 'flash=%s' % flash_cookie_encoder([flash_message])}
        )

        self.assertIn('set-cookie', response.headers)
        self.assertIn('flash=', response.headers.get('set-cookie'))

        for cookie in response.headers.get_list('set-cookie'):
            cookie_dict = httputil.parse_cookie(cookie)
            if 'flash' in cookie_dict:
                break

        self.assertEqual(cookie_dict['flash'], '')

        # 2. Test with existing cookie but no new flash

        del cookie_dict

        response = self.fetch('/?num=0&load_messages=True',
            headers={'Cookie': 'flash=%s' % flash_cookie_encoder([flash_message])}
        )

        self.assertIn('set-cookie', response.headers)
        self.assertIn('flash=', response.headers.get('set-cookie'))

        for cookie in response.headers.get_list('set-cookie'):
            cookie_dict = httputil.parse_cookie(cookie)
            if 'flash' in cookie_dict:
                break

        self.assertEqual(cookie_dict['flash'], '')

    def test_cookie_is_not_cleared_unnecessarily_when_no_messages_are_set(self):
        """Ensure the server doesn't sent unnecessary empty Set-Cookie headers
        when the request didn't contain any cookies.
        """
        response = self.fetch('/?num=0&load_messages=True')

        self.assertNotIn('flash=', response.headers.get('set-cookie', ''))

    def test_error_handled_when_no_cookie(self):
        request = self.get_request()
        handler = TestHandler(self.get_app(), request)
        # messages must be empty if there's no cookie
        self.assertEqual(handler.get_flashed_messages(), [])

    def test_error_is_handled_when_invalid_cookie(self):
        request = self.get_request(headers={'Cookie': 'flash=hello'})
        handler = TestHandler(self.get_app(), request)
        # messages must be empty if the cookie is invalid
        self.assertEqual(handler.get_flashed_messages(), [])

    def test_message_is_accessible_in_same_request(self):
        """If a message is set on a response (i.e. current request),
        the cookie will be available in the next request.

        But we need those messages to be available in current request so that 
        they can be shown on templates in case there are no redirects.
        """
        request = self.get_request()
        handler = TestHandler(self.get_app(), request)
        handler.flash(*flash_message)
        self.assertEqual(handler.get_flashed_messages(), [flash_message])

    def test_existing_cookie_message_is_not_removed_when_flashing_new_message(self):
        request = self.get_request(headers={'Cookie': 'flash=%s' % flash_cookie_encoder([flash_message])})
        handler = TestHandler(self.get_app(), request)
        handler.flash(*flash_message)
        self.assertEqual(len(handler.get_flashed_messages()), 2)
