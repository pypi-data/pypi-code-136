import asyncio
from unittest import IsolatedAsyncioTestCase

from aiohttp import web

from async_url_validator.url_validator import URLValidator
from async_url_validator.status_assigner import StatusAssigner, Status


class TestURLValidator(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        status_assigner = StatusAssigner(page_text='not available')
        request_method = (status_assigner.page_text and 'GET') or 'HEAD'
        self.validator = URLValidator(timeout=1, request_method=request_method, status_assigner=status_assigner)
        await self._start_server()

    async def asyncTearDown(self) -> None:
        await self._runner.cleanup()

    async def _start_server(self):
        app = web.Application()
        app.add_routes([web.get('/', handle_ok),
                        web.get('/not_available/', handle_not_available),
                        web.get('/page_not_found/', handle_page_not_found),
                        web.get('/timeout/', handle_timeout),
                        web.get('/redirect/', handle_redirect),
                        web.get('/bad_redirect/', handle_bad_redirect),
                        ])
        self._runner = web.AppRunner(app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, 'localhost', port=8081)
        await site.start()

    async def test_ok(self):
        ok_url = 'http://localhost:8081'
        async for status in self.validator.validate(ok_url):
            self.assertEqual(status, Status.OK)

    async def test_bad_query_string(self):
        bad_redirect_url = 'http://localhost:8081/bad_redirect/'
        async for status in self.validator.validate(bad_redirect_url):
            self.assertEqual(status, Status.BAD_QUERY_STRING)

    async def test_redirect(self):
        redirect_url = 'http://localhost:8081/redirect/'
        async for status in self.validator.validate(redirect_url):
            self.assertEqual(status, Status.REDIRECT)

    async def test_text_found(self):
        not_available_url = 'http://localhost:8081/not_available/'
        async for status in self.validator.validate(not_available_url):
            self.assertEqual(status, Status.TEXT_FOUND)

    async def test_bad_status(self):
        bad_url = 'http://localhost:8081/bad/'
        async for status in self.validator.validate(bad_url):
            self.assertEqual(status, Status.BAD_STATUS)

    async def test_timeout(self):
        timeout_url = 'http://localhost:8081/timeout/'
        async for status in self.validator.validate(timeout_url):
            self.assertEqual(status, Status.TIMEOUT)


async def handle_ok(request):
    return web.Response(text='ok')


async def handle_not_available(request):
    return web.Response(text='not available')


async def handle_page_not_found(request):
    return web.Response(status=404)


async def handle_timeout(request):
    await asyncio.sleep(2)
    return web.Response(text='timeout')


async def handle_redirect(request):
    new_location = request.url.with_path('/').update_query(request.url.query)
    return web.HTTPFound(new_location)


async def handle_bad_redirect(request):
    return web.HTTPFound('/')
