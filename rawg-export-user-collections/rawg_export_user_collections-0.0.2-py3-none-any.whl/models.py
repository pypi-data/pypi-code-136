from typing import Optional

from pydantic import BaseModel


class GameModel(BaseModel):
    id: int
    name: str
    slug: str
    url: str
    released: Optional[str] = None
    tba: bool
    rating: float
    updated: str
    genres: Optional[list[str]] = None
    platforms: Optional[list[str]] = None


class CollectionModel(BaseModel):
    id: int
    name: str
    slug: str
    url: str
    description: str
    games_count: int
    created: str
    updated: str
    games: list[GameModel] = []


class ResultModel(BaseModel):
    count: int
    collections: list[CollectionModel]
