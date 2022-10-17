from web_foundation.environment.services.service import Service
from web_foundation.environment.workers.web.ext.addons_loader import AddonsLoader


class ApiAddonsService(Service):
    addons_loader: AddonsLoader

    def __init__(self, addons_loader: AddonsLoader):
        self.addons_loader = addons_loader

    async def add_new_middleware(self, filename: str):
        await self.addons_loader.add_new_middleware(filename)

    async def delete_middleware(self, filename: str):
        await self.addons_loader.delete_middleware(filename)
