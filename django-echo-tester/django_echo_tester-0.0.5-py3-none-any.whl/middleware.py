from echo_tester.store import StoreManager
from echo_tester.settings import recorder_settings


class TesterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.store = StoreManager()

    def send_to_recorder(self, request, response):
        # handle recorder
        is_skip = any(map(request.path.startswith, recorder_settings.SKIP_PATH))
        if is_skip:
            return

        self.store.save(request, response)

    def __call__(self, request):
        response = self.get_response(request)
        try:
            self.send_to_recorder(request, response)
        except Exception as e:
            if recorder_settings.RAISE_ERRORS:
                raise e

        return response

