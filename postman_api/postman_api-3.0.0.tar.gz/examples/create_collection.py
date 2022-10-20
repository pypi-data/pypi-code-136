import os
from postman_api import AsyncPostmanClient
from postman_api import PostmanClient


def main():
    client = PostmanClient.from_env()
    response = client.create_collection()
    print(f"{response!r}")


async def async_main():
    client = AsyncPostmanClient.from_env()
    response = await client.create_collection()
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
