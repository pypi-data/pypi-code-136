import os
from postman_api import AsyncPostmanClient
from postman_api import PostmanClient


def main():
    client = PostmanClient.from_env()
    response = client.sync_relations_with_schema(
        api_id="your api id",
        api_version_id="your api version id",
        relation_type="your relation type",
        entity_id="your entity id",
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPostmanClient.from_env()
    response = await client.sync_relations_with_schema(
        api_id="your api id",
        api_version_id="your api version id",
        relation_type="your relation type",
        entity_id="your entity id",
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
