import os
from postman_api import AsyncPostmanClient
from postman_api import PostmanClient


def main():
    client = PostmanClient.from_env()
    response = client.single_collection(collection_uid)
    print(f"{response!r}")


async def async_main():
    client = AsyncPostmanClient.from_env()
    response = await client.single_collection(collection_uid)
    print(f"{response!r}")


collection_uid = "your collection uid"
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
