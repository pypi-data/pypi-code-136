import os
from postman_api import AsyncPostmanClient
from postman_api import PostmanClient


def main():
    client = PostmanClient.from_env()
    response = client.create_collection_from_schema(
        api_id="your api id",
        api_version_id="your api version id",
        schema_id="your schema id",
        name="your name",
        relations=[{}],
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPostmanClient.from_env()
    response = await client.create_collection_from_schema(
        api_id="your api id",
        api_version_id="your api version id",
        schema_id="your schema id",
        name="your name",
        relations=[{}],
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
