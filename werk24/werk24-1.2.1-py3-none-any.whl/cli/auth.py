import argparse

from werk24.cli import utils
from werk24.techread_client import W24TechreadClient


async def main(
    args: argparse.Namespace
) -> None:
    """
    Interact with the Authentication Client through the API

    Args:
        args(argparse.Namespace): CLI args generated by
        argparse
    """

    # get the client instance and handle
    # potential errors
    client = utils.make_client()

    # then check whether we can do anything for the
    # caller
    if args.ask_jwt_token:
        await _handle_ask_jwt_token(client)

async def _handle_ask_jwt_token(
    client: W24TechreadClient,
) -> None:
    """ Steal a valid JWT token from the authentication
    client and print it to the console

    Args:
        client (W24TechreadClient): Current client
    """

    # start a session with the client to obtain a valid
    # token
    async with client as session:
        token =session._auth_client.token
        print(f"Received Token: {token}")