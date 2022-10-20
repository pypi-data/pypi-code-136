import os
from postman_api import AsyncPostmanClient
from postman_api import PostmanClient


def main():
    client = PostmanClient.from_env()
    response = client.delete_environment(environment_uid)
    print(f"{response!r}")


async def async_main():
    client = AsyncPostmanClient.from_env()
    response = await client.delete_environment(environment_uid)
    print(f"{response!r}")


environment_uid = "your environment uid"
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
