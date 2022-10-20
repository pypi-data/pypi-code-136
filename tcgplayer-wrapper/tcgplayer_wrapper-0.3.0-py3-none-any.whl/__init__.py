"""tcgplayer package entry file."""
__version__ = "0.3.0"
__all__ = ["__version__", "get_cache_root"]

from pathlib import Path


def get_cache_root() -> Path:
    """
    Create and return the path to the cache for TCGPlayer Wrapper.

    Returns:
        The path to the TCGPlayer Wrapper cache
    """
    folder = Path.home() / ".cache" / "tcgplayer-wrapper"
    folder.mkdir(parents=True, exist_ok=True)
    return folder
