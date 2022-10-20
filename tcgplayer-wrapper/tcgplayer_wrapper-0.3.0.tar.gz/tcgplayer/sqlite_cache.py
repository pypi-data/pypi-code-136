"""
The SQLiteCache module.

This module provides the following classes:
- SQLiteCache
"""
__all__ = ["SQLiteCache"]

import json
import sqlite3
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

from tcgplayer import get_cache_root


class SQLiteCache:
    """
    The SQLiteCache object caches results from TCGPlayer.

    Args:
        path: Path to the database.
        expiry: How long to keep the cache results, in days.
    Attributes:
        expiry (Optional[timedelta]): How long to keep the cache results, in days.
        con (sqlite3.Connection): Database connection.
        cur (sqlite3.Cursor): Database cursor.
    """

    def __init__(
        self,
        path: Path = get_cache_root() / "cache.sqlite",
        expiry: Optional[int] = 14,
    ):
        self.expiry = timedelta(days=expiry) if expiry else None
        self.con = sqlite3.connect(str(path))
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS queries (query, response, date_added);")
        self.delete()

    def select(self, query: str) -> Dict[str, Any]:
        """
        Retrieve data from the cache.

        Args:
            query: Search string.
        Returns:
            Empty dict or results.
        """
        if self.expiry:
            self.cur.execute(
                "SELECT response FROM queries WHERE query = ? and date_added > ?;",
                (query, (date.today() - self.expiry).isoformat()),
            )
        else:
            self.cur.execute("SELECT response FROM queries WHERE query = ?;", (query,))
        if results := self.cur.fetchone():
            return json.loads(results[0])
        return {}

    def insert(self, query: str, response: Dict[str, Any]):
        """
        Insert data into the cache.

        Args:
            query: Search string.
            response: Data to save.
        """
        self.cur.execute(
            "INSERT INTO queries (query, response, date_added) VALUES (?, ?, ?);",
            (query, json.dumps(response), date.today().isoformat()),
        )
        self.con.commit()

    def delete(self):
        """Remove all expired data from the cache."""
        if not self.expiry:
            return
        self.cur.execute(
            "DELETE FROM queries WHERE date_added <= ?;",
            ((date.today() - self.expiry).isoformat(),),
        )
        self.con.commit()
