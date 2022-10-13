import json
from pathlib import Path


class JSONLoaderMixin:
    def load_dict(self, dictionary: dict):
        # put python dict through json encoder and decoder
        contents = json.dumps(dictionary)
        self._json = json.loads(contents)
        return

    def load(self):
        with open(self.fp, "r") as f:
            contents = f.read()

        self._json = json.loads(contents)
        return

    def save(self, fp: str | Path | None = None, return_fp: bool = False):
        if fp is None:
            fp = self.fp

        with open(fp, "w") as f:
            json.dump(self.serialize(), f, indent=4)

        print("Saved file to: {}".format(fp))
        if return_fp:
            return fp
        else:
            return

    # properties
    @property
    def fp(self):
        return getattr(self, "_fp", None)

    @fp.setter
    def fp(self, value: str | Path):
        assert isinstance(value, str | Path), "Must be filepath."
        self._fp = Path(value)
        return

    @property
    def json(self):
        return getattr(self, "_json", None)

    @json.setter
    def json(self, value: str | Path):
        self.fp = value
        self.load()
        return
