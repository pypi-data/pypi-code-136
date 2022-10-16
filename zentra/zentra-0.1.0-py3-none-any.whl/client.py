import asyncio
import json
import logging
from typing import Literal

import httpx
import websockets

from zentra import Message

log = logging.getLogger(__name__)


# TODO Error handle routes
class Client:
    def __init__(self, name: str, *, call_on_message=None):
        """

        Parameters
        ----------
        name: str
            The name you wish to chat as.
        call_on_message
            An async function that will be called with each new
            :py:class:`zentra.Message` object as it arrives.
        """
        self._name: str = name
        self._nonce: str | None = None
        self._connection_id: str | None = None
        self._ws_url: str = "wss://api.zentra.live/ws"
        self._base_url: str = "https://api.zentra.live"
        self._call_on_message = call_on_message
        self._connection_future: asyncio.Future = asyncio.Future()

    @property
    def _headers(self) -> dict:
        if not self._nonce or not self._connection_id:
            raise RuntimeError("Please connect to the websocket before doing anything.")

        return {"X-CONNECTION-ID": self._connection_id, "X-NONCE": self._nonce}

    async def connect(self):
        asyncio.create_task(self._connect())
        await self._connection_future
        log.info(
            "Successfully connected to the gateway with connection id %s",
            self._connection_id,
        )

    async def _connect(self):
        try:
            async with websockets.connect(f"{self._ws_url}/{self._name}") as websocket:
                while True:
                    d = await websocket.recv()
                    data: dict = json.loads(d)
                    ws_type: Literal["HELLO", "PING", "NEW_MESSAGE"] = data["type"]

                    if ws_type == "HELLO":
                        log.debug("Received HELLO event")
                        self._nonce = str(data["data"]["nonce"])
                        self._connection_id = str(data["data"]["connection_id"])
                        self._connection_future.set_result(None)

                    elif ws_type == "PING":
                        log.debug("Received PING event")
                        await websocket.send(
                            json.dumps({"type": "PONG", "data": data["data"]})
                        )
                        log.debug("Sent PONG event")

                    elif ws_type == "NEW_MESSAGE":
                        log.debug("Received NEW_MESSAGE event")
                        if self._call_on_message:
                            await self._call_on_message(Message(**data["data"]))

                    else:
                        log.warning("Received unknown event %s", ws_type)
        except:
            self._connection_future = asyncio.Future()
            raise

    async def fetch_conversation_ids(self) -> list[int]:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self._base_url}/conversations/ids")
            assert r.status_code == 200
            return r.json()["data"]

    async def fetch_messages(self, conversation_id: int) -> list[Message]:
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"{self._base_url}/conversations/{conversation_id}/messages"
            )
            assert r.status_code == 200
            d = r.json()["data"]
            data = []
            for i in d:
                data.append(Message(**i))

            return data

    async def fetch_latest_message(self, conversation_id: int) -> Message:
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"{self._base_url}/conversations/{conversation_id}/messages/latest"
            )
            assert r.status_code == 200
            d = r.json()["data"]
            return Message(**d)

    async def fetch_all_latest_messages(self) -> list[Message]:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self._base_url}/conversations/all/messages/latest")
            assert r.status_code == 200
            d = r.json()["data"]
            data = []
            for i in d:
                data.append(Message(**i))

            return data

    async def send_message(self, *, content: str, conversation_id: int) -> None:
        async with httpx.AsyncClient() as client:
            r = await client.post(
                f"{self._base_url}/conversations/{conversation_id}/messages",
                headers=self._headers,
                json={"content": content},
            )
            assert r.status_code == 204
