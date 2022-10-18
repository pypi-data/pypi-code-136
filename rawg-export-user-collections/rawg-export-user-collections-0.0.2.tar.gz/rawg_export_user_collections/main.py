import argparse
import asyncio
import json
import logging
import os
from datetime import datetime
from typing import Any, Optional

import aiohttp

from rawg_export_user_collections.models import CollectionModel, GameModel, ResultModel

logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Export public user's collections "
        "from the RAWG.IO video game database.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--user_slug",
        type=str,
        required=True,
        help="User slug from which we get collections.",
    )
    parser.add_argument(
        "--export_folder_path",
        type=str,
        required=True,
        help="Path where to export the file.",
    )

    return parser.parse_args()


async def fetch_user_collections(user_slug: str) -> list[CollectionModel]:
    collections: list[CollectionModel] = []

    async with aiohttp.ClientSession() as session:
        user_collections_url: Optional[
            str
        ] = f"https://rawg.io/api/users/{user_slug}/collections"

        while user_collections_url is not None:
            async with session.get(user_collections_url) as response:
                response_json: dict[str, Any] = await response.json()

                for item in response_json["results"]:
                    collection_slug: str = item["slug"]

                    collections.append(
                        CollectionModel(
                            id=item["id"],
                            name=item["name"],
                            slug=collection_slug,
                            url=f"https://rawg.io/collections/{collection_slug}",
                            description=item["description"],
                            games_count=item["games_count"],
                            created=item["created"],
                            updated=item["updated"],
                        )
                    )

                user_collections_url = response_json["next"]

        logging.info(f"Collected {len(collections)} collections")

        for collection in collections:
            collection.games = await fetch_collection_games(
                session=session, collection_slug=collection.slug
            )

    return collections


async def fetch_collection_games(
    session: aiohttp.ClientSession, collection_slug: str
) -> list[GameModel]:
    games: list[GameModel] = []

    request_url: Optional[str] = (
        f"https://api.rawg.io/api/collections/"
        f"{collection_slug}/feed?ordering=-created&page=1"
    )

    while request_url is not None:
        async with session.get(request_url) as response:
            response_json: dict[str, Any] = await response.json()

            for item in response_json["results"]:
                game_value: dict[str, Any] = item["game"]
                game_slug: str = game_value["slug"]

                genres: list[str] = [genre["name"] for genre in game_value["genres"]]
                platforms: list[str] = [
                    platform["platform"]["name"] for platform in game_value["platforms"]
                ]

                game: GameModel = GameModel(
                    id=game_value["id"],
                    name=game_value["name"],
                    slug=game_slug,
                    url=f"https://rawg.io/games/{game_slug}",
                    released=game_value["released"],
                    tba=game_value["tba"],
                    rating=game_value["rating"],
                    updated=game_value["updated"],
                    genres=genres,
                    platforms=platforms,
                )

                games.append(game)

            request_url = response_json["next"]

    return games


async def export_collections_to_json_file(
    collections: list[CollectionModel], export_folder_path: str
) -> None:
    filename: str = f"{datetime.now().strftime('%Y.%m.%d')} - exported_collections.json"

    with open(os.path.join(export_folder_path, filename), "w", encoding="utf8") as file:
        result_model: ResultModel = ResultModel(
            count=len(collections), collections=collections
        )

        json.dump(obj=result_model.dict(), fp=file, indent=4, ensure_ascii=False)


async def main():
    args: argparse.Namespace = parse_args()

    logging.info("Fetching collections...")

    collections: list[CollectionModel] = await fetch_user_collections(
        user_slug=args.user_slug
    )

    logging.info("Exporting collections to json file...")

    await export_collections_to_json_file(
        collections=collections, export_folder_path=args.export_folder_path
    )

    logging.info("Completed!")

    await asyncio.sleep(0.5)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
