import json
import time
from base64 import b64decode
import asyncio
from math import ceil
from typing import List

from tonsdk.boc import Cell
from tonsdk.utils import Address, bytes_to_b64str, b64str_to_bytes

from ton import TonlibClient

from .utils import *


async def _get_client(ls: int):
    TonlibClient.enable_unaudited_binaries()
    client = TonlibClient(ls_index=ls)
    await client.init_tonlib()
    # await client.tonlib_wrapper.cancel_futures()
    # client.loop
    # await client.set_verbosity_level(5)
    return client


def get_client(ls: int = 0):
    client = asyncio.get_event_loop().run_until_complete(_get_client(ls))
    return client


async def get_owner(client: TonlibClient, addr: str):
    account = await client.find_account(addr)
    x = await account.get_nft_data()
    a = x['owner_address'].to_string()
    return a.to_string()


def get_items(client: List[TonlibClient] or TonlibClient, addresses: list, filename_with_nft_metadata=None, max_requests: int = 1000):
    if filename_with_nft_metadata and 'json' not in filename_with_nft_metadata:
        raise Exception('Only .json files are expected')
    elif filename_with_nft_metadata:
        with open(filename_with_nft_metadata, 'r') as j:
            items = json.loads(j.read())
    nft_items = []

    if isinstance(client, list):
        pass
    else:
        client = [client]

    d = 0

    for i in range(ceil(len(addresses) / max_requests)):
        tasks = []
        for addr in addresses[i * max_requests:min(len(addresses), max_requests * (i + 1))]:
            tasks.append(get_item(client[d % len(client)], addr, nft_items, items))
            # print(d % len(client))
            d += 1
        # asyncio.set_event_loop(asyncio.SelectorEventLoop())
        asyncio.get_event_loop().run_until_complete(asyncio.gather(*tasks))
        print('DONE')
    if len(nft_items) < len(addresses):
        raise Exception('SCANNED NOT ALL ITEMS')
    return {"nft_items": nft_items}


async def get_item(client: TonlibClient, addr: str, nft_items: list, items: dict = None):
    account = await client.find_account(addr, preload_state=False)

    x = await account.get_nft_data()
    collection_address = x['collection_address'].to_string()
    owner_address = x['owner_address'].to_string()

    content_url = await get_nft_content_url(client, x['content'], collection_address)

    s = time.time()
    if items:
        if str(x['index']) in items:
            content = items[str(x['index'])]
            # print(time.time() - s)
        else:
            content = await get(content_url)
    else:
        content = await get(content_url)

    collection_content = await get_collection_content(client, x['collection_address'].to_string())
    result = {
        'address': Address(addr).to_string(is_user_friendly=False),
        'collection': {
            'address': collection_address,
            'name': collection_content.get('name'),
            'description': collection_content.get('description'),
            'image': collection_content.get('image')
        },
        'collection_address': collection_address,
        'index': x['index'],
        'content_url': content_url,
        'metadata': {
            'attributes': content.get('attributes'),
            'description': content.get('description'),
            'image': content.get('image'),
            'name': content.get('name'),
        },
        'owner': {
            'address': x['owner_address'].to_string()
        }
    }

    sale_data = await get_nft_sale(client, owner_address)

    if sale_data:
        result['sale'] = sale_data

    nft_items.append(result)
