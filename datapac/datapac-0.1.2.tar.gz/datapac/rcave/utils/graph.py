from typing import Literal
from typing import Union

import yaml
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated

Graph = Annotated[Union["S3Node", "PostgresNode"], Field(discriminator="type")]


class S3Node(BaseModel):
    type: Literal["s3"]

    key: str
    bucket: str


class PostgresNode(BaseModel):
    type: Literal["postgres"]

    table: str
    where: dict

    relationships: list["Graph"] = []


class Config(BaseModel):
    graph: Graph

    class Config:
        orm_mode = True


def load_yaml(input) -> Config:
    return Config(**yaml.safe_load(input))


def load(path: str) -> Config:
    with open(path) as f:
        return load_yaml(f)
