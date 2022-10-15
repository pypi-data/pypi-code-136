from dataclasses import dataclass


@dataclass
class MongoConfig:
    mongo_uri: str
    db_name: str
