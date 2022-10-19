import aiohttp
from typing import List as ListT

from .models import Action, Bot, BotPost, List, ListUpdate

BASE_URL = "https://catnip.metrobots.xyz"
"""The base URL for the Metro API."""

class MetroHTTP():
    def __init__(self, *, list_id: str, secret_key: str):
        """Contains the HTTP methods for the Metro Reviews API"""
        self.list_id = list_id
        self.secret_key = secret_key

    async def request(self, *, url: str, method: str, json: dict = None):
        """Make a request to the Metro Reviews API"""
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, 
                BASE_URL+url, 
                json=json, 
                headers={
                    "Authorization": self.secret_key
                }
            ) as resp:
                resp_data = await resp.json()
                return resp, resp_data

    async def update_list(self, update: ListUpdate):
        """Edits the list"""
        return await self.request(
            url=f"/lists/{self.list_id}",
            method="PATCH",
            json=update.dict()
        )
    
    async def add_bot(self, bot: BotPost):
        """Add a bot to Metro Reviews"""
        res, json = await self.request(url=f"/bots?list_id={self.list_id}", method="POST", json=bot.dict())

        if not res.ok:
            raise RuntimeError(f"Failed to add bot: {res.status}")

        return Bot(**json)

    async def approve_bot(self, *, bot_id: str, reviewer: str, reason: str):
        """Approve a bot"""
        return await self.request(
            url=f"/bots/{bot_id}/approve?reviewer={reviewer}&list_id={self.list_id}",
            method="POST",
            json={
                "reason": reason
            }
        )

    async def deny_bot(self, *, bot_id: str, reviewer: str, reason: str):
        """Dnies a bot"""
        return await self.request(
            url=f"/bots/{bot_id}/deny?reviewer={reviewer}&list_id={self.list_id}",
            method="POST",
            json={
                "reason": reason
            }
        )
    
    async def get_actions(self, *, offset: int, limit: int):
        """
**This is a paginated API**

Get actions from Metro Reviews. 

You need to use ``Metro.paginate`` with this as this endpoint is paginated.
        """
        res, json = await self.request(
            url=f"/actions?offset={offset}&limit={limit}",
            method="GET"
        )

        if not res.ok:
            raise RuntimeError(f"Failed to get actions: {res.status}")

        return json, Action

    async def get_all_lists(self) -> ListT[List]:
        """Get all lists from Metro Reviews"""
        res, json = await self.request(url="/lists", method="GET")
        
        if not res.ok:
            raise RuntimeError(f"Failed to get lists: {res.status}")
        
        return [List(**i) for i in json]

    async def get_list(self, list_id: str) -> List:
        """Get a list from Metro Reviews"""
        res, json = await self.request(url=f"/list/{list_id}", method="GET")

        if not res.ok:
            raise RuntimeError(f"Failed to get list: {res.status}")

        return List(**json)

    async def get_all_bots(self) -> ListT[Bot]:
        """Get all bots from Metro Reviews"""
        res, json = await self.request(url=f"/bots", method="GET")

        if not res.ok:
            raise RuntimeError(f"Failed to get bots: {res.status}")

        return [Bot(**i) for i in json]
    
    async def get_bot(self, bot_id: int) -> Bot:
        """Get a bot from Metro Reviews"""
        res, json = await self.request(url=f"/bots/{bot_id}", method="GET")

        if not res.ok:
            raise RuntimeError(f"Failed to get bot: {res.status}")

        return Bot(**json)
