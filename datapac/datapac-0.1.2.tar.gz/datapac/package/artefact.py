from pydantic import BaseModel


class Artefact(BaseModel):
    source: str  # TODO: make this pydantic class

    @property
    def output_path(self):
        raise NotImplementedError

    def write(self, path: str):
        raise NotImplementedError

    def map(self, variables: dict) -> "Artefact":
        raise NotImplementedError
