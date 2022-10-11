"""
Database pre-defined queries.
"""

from sqlalchemy import text

import podarr


class Query:
    """
    This object contains methods with pre-defined queries.
    """

    def __init__(self) -> None:
        self.session = podarr.SESSION_MAKER

    def get_all_services(self, order_by: str, desc=False) -> list:
        """
        1. This will query all the service entries in the database
        and return it as a list.
        2. It can be ordered by any column in the database, in descending
        or ascending order.
        """
        return self.session.query(podarr.Service).order_by(
            text(f'{order_by} {"desc" if desc else "asc"}')).all()

    def get_all_users(self, order_by: str, desc=False) -> list:
        """
        1. This will query all the user entries in the database
        and return it as a list.
        2. It can be ordered by any column in the database, in descending
        or ascending order.
        """
        return self.session.query(podarr.User).order_by(
            text(f'{order_by} {"desc" if desc else "asc"}')).all()
