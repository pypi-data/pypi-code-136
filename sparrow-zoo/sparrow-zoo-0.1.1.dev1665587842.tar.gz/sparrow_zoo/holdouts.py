"""Holdout utilities."""
import enum

import farmhash


class Holdout(enum.Enum):
    """Holdout enum."""

    train = "train"
    dev = "dev"
    test = "test"


def get_holdout(slug: str) -> Holdout:
    """Compute which holdout a slug belongs to."""
    slug_mod = farmhash.fingerprint64(slug) % 10
    if slug_mod < 8:
        return Holdout.train
    elif slug_mod == 8:
        return Holdout.dev
    else:
        return Holdout.test
