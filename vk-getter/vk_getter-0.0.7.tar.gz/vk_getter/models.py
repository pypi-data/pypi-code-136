from dataclasses import dataclass


@dataclass(frozen=True)
class Attachments:
    photo: list[str]
    video: list[str]
    audio: list[str]
    other: list[str]


@dataclass(frozen=True)
class Post:
    id: int
    date: str
    time: str
    text: str
    attachments: Attachments
    comments: int = 0
    likes: int = 0
    reposts: int = 0
    views: int = 0
            