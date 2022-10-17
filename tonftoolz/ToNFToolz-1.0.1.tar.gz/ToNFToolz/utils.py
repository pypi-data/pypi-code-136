import logging
from base64 import b64decode
import aiohttp

import asyncio
from tonsdk.boc import Cell
from tonsdk.utils import Address, bytes_to_b64str, b64str_to_bytes

from ton.account import Account
from ton import TonlibClient
from ton.utils.cell import read_address


async def get_nft_content_url(client: TonlibClient, individual_content: Cell, collection_address: str):
    url = ''
    if collection_address in collections_content_base_urls:
        url += collections_content_base_urls[collection_address]
    else:
        account = await client.find_account(collection_address)
        l = await account.get_state()
        data = Cell.one_from_boc(b64decode(l.data))
        # print(data.refs[0].refs[0])
        if len(data.refs[0].refs) == 1:
            url += data.refs[0].refs[0].bits.get_top_upped_array().decode()
        else:
            url += data.refs[0].refs[1].bits.get_top_upped_array().decode()
    if len(individual_content.refs) != 0:
        url += individual_content.refs[0].bits.get_top_upped_array().decode()
    else:
        url += individual_content.bits.get_top_upped_array().decode()
    return url


async def get(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_collection_content(client: TonlibClient, address: str):
    if address in collections_content:
        return collections_content[address]
    account = await client.find_account(address)
    collection_data = await account.get_collection_data()
    collection_data = collection_data['content'].bits.get_top_upped_array().decode()
    collection_url = collection_data[collection_data.find('http'):]
    # print(collection_url)
    resp = await get(collection_url)
    return resp


async def get_nft_sale(client: TonlibClient, owner_address: str):
    account = await client.find_account(owner_address)
    response = await account.run_get_method(method='get_sale_data', stack=[])
    if response.exit_code != 0:
        return False
    if len(response.stack) == 10:
        return {
            'address': owner_address,
            'market': {
                'address': read_address(Cell.one_from_boc(b64decode(response.stack[3].cell.bytes))).to_string(),
                'name': markets_adresses.get(
                    read_address(Cell.one_from_boc(b64decode(response.stack[3].cell.bytes))).to_string(), '')
            },
            'owner': {
                'address': read_address(Cell.one_from_boc(b64decode(response.stack[5].cell.bytes))).to_string()
            },
            'price': {
                'value': response.stack[6].number.number,
            }
        }
    elif len(response.stack) == 7:
        return {
            'address': owner_address,
            'market': {
                'address': read_address(Cell.one_from_boc(b64decode(response.stack[0].cell.bytes))).to_string(),
                'name': markets_adresses.get(
                    read_address(Cell.one_from_boc(b64decode(response.stack[0].cell.bytes))).to_string(), '')
            },
            'owner': {
                'address': read_address(Cell.one_from_boc(b64decode(response.stack[2].cell.bytes))).to_string()
            },
            'price': {
                'token_name': 'TON',
                'value': response.stack[3].number.number,
            }
        }
    elif len(response.stack) >= 11:
        return {
            'address': owner_address,
            'market': {
                'address': read_address(Cell.one_from_boc(b64decode(response.stack[3].cell.bytes))).to_string(),
                'name': markets_adresses.get(
                    read_address(Cell.one_from_boc(b64decode(response.stack[3].cell.bytes))).to_string(), '')
            },
            'owner': {
                'address': read_address(Cell.one_from_boc(b64decode(response.stack[5].cell.bytes))).to_string()
            },
            'price': {
                'value': response.stack[6].number.number,
            }
        }
    else:
        logging.warning(f'FAILED TO PARSE NFT SALE DATA; NFT SALE SMART CONTRACT: {owner_address}')
        return False

    # print(response)


collections_content = {
    '0:00d72bc3683c042b9bc718e5d176d4b631b395775f93372d352f54bfb761c5e2': {
        "name": "Animals Red List",
        "description": "Animals Red List is the first NFT project on the TON platform to integrate with Telegram. The project consists of 13,333 NFTs. Each NFT is a unique, hand-drawn illustration matching an endangered animal from the Red List.",
        "image": "https://nft.animalsredlist.com/nfts/Gorilla.gif"
    },
    '0:28f760d832893182129cabe0a40864a4fcc817639168d523d6db4824bd997be6': {
        "name": "TON Punks 💎",
        "description": "TON PUNKS 💎 — a collection of 9999 NFTs created for the TON blockchain. Our values are freedom of information, enlightenment and decentralization.",
        "image": "https://cloudflare-ipfs.com/ipfs/QmRGAJd1sQVWntuXMLrPmZ9oiafSvCwsmdGsTVfQ9UiS5D?filename=logo.png",
        "cover_image": "https://cloudflare-ipfs.com/ipfs/bafybeifvjuiq3wvn5pgxi2pikfwzlrion57kprogo4nsbhe3ym6ieb2b2u?filename=cover.png"
    },
    '0:3391a5590a9eb61c1cfc2af78a3349ff8eef19d934db0ca1eb122a52115bd727': {
        "name": "Mintosaurs",
        "description": "Mintosaurs \ud83e\udd96 \u2014 a collection of 5000 NFT, created in different styles, including 3D. The collection has staking, a deflation mechanism, and ecosystem of services: Tonometer and Monster Bot.",
        "image": "https://cloudflare-ipfs.com/ipfs/QmcMD8145qSygwFWmRdahwPxjc8fjJWx3WEUNvoFMWC4EG?filename=logo.gif",
        "social_links": ["https://mintosaurs.com"]
    },
    '0:11c2e552309b2bbb88e54355bd95f6bbc2d4af3c311ec7a2258406f1f0feee67': {
        "cover_image": "https://cloudflare-ipfs.com/ipfs/QmW7G4M7CzW78iDJLgDvc5C63jpTZovdyFBqkpV3uiQtsV?filename=banner.gif",
        "description": "No community. No price. No rules.",
        "image": "https://collection.disruptors.space/items/avatar.gif",
        "name": "Disruptors"
    },
    '0:5d5fa5b27067f247a6710ee08ec527667cf00c6a8993db35bb2f56b5cf7b4a3e': {
        'name': '💎 TON Earth 🌍 Houseboats 🏠🚢',
        'description': '🏠🚢 Houseboats, for the TON Earthlings who think that land is for suckers.',
        'image': 'https://nft.tonearth.com/houseboats/images/collection-houseboats.png'
    },
    '0:af1b993989ddfdc521bc14f38d68f6ad8c40570762e7e7ae7bf540381458fc7b': {
        'name': '💎 TON Earth 🌍 Lands ⛰',
        'description': '⛰ Lands, the foundation of the first virtual world on TON!',
        'image': 'https://cloudflare-ipfs.com/ipfs/bafybeibqh7hp3ijv36a4e7ijrk3uhpoa73pkp2v5m3nblj46vynfms73nq'
    },
    '0:76be90926bfd3ccfd71aa701e27eb158f7d76943caef004302e76f0248cbad36:': {
        'name': '💎 TON Earth 🌍 Collectibles 🧭',
        'description': "🧭 Collectibles from 💎 TON Earth's 🌎 history. Catch em' all!",
        'image': 'https://cloudflare-ipfs.com/ipfs/bafybeihhm2i6enytv4dveqpukdxumol5jnczbrjskmeajfocwiewzcdsbi'
    },
    '0:15a372f8e631b3b0b8aeca9c1506277ab2bb6702ac6381a0598ec9750c30b306': {
        'name': '💎 TON Earth 🌍 Houses v1',
        'description': 'The first attempted house designs for TON Earth. They were thrown out, but now they are a fun little gift for our users.',
        'image': 'https://cloudflare-ipfs.com/ipfs/bafybeiejh4ws3tck55du7opkz6ncvm2azdhbyf23ceyjvxomcpqhgjzd2y/preview.png'
    },
    '0:ef8f2677f36bf0c0ec0755f3a7c4445acba2d8038adac92eadebef593b549fc5': {
        'name': '💎 TON Earth 🌍 Houses 🏘️',
        'description': '🏘️ Houses in the first virtual world on TON. Build your homestead today!',
        'image': 'https://cloudflare-ipfs.com/ipfs/bafybeidcvr3asseofyzn5jdi2si74i3nywvrwvqajc6q33tbpu7j5bkx7i'
    }
}

collections_content_base_urls = {
    '0:00d72bc3683c042b9bc718e5d176d4b631b395775f93372d352f54bfb761c5e2': 'http://nft.animalsredlist.com/nfts/',
}

markets_adresses = {
    '0:584ee61b2dff0837116d0fcb5078d93964bcbe9c05fd6a141b1bfca5d6a43e18': 'Getgems Sales',
    '0:eb2eaf97ea32993470127208218748758a88374ad2bbd739fc75c9ab3a3f233d': 'Disintar Marketplace'
}
