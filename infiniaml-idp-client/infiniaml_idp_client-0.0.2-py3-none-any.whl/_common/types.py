from typing import Protocol


class TokenCredential(Protocol):
    def get_token(self) -> str:
        ...


class AsyncTokenCredential(Protocol):
    async def get_token(self) -> str:
        ...
