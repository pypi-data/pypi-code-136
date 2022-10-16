class StorageBackend:
    @property
    def name(self) -> str:
        raise NotImplementedError


class StorageEngine:
    def __init__(self, backend: StorageBackend):
        self._backend = backend

    @property
    def backend(self):
        return self._backend

    @property
    def is_async(self):
        raise NotImplementedError

    def new_connection(self):
        raise NotImplementedError

    def start(self):
        pass

    def stop(self):
        pass

    async def async_start(self):
        pass

    async def async_stop(self):
        pass
