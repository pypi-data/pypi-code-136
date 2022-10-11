
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_bib_feeds


class BibFeeds(Base):
    __tablename__ = 'arXiv_bib_feeds'

    bib_id = Column(MEDIUMINT, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("''"))
    priority = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    strip_journal_ref = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    uri = Column(String(255))
    identifier = Column(String(255))
    version = Column(String(255))
    concatenate_dupes = Column(Integer)
    max_updates = Column(Integer)
    email_errors = Column(String(255))
    prune_ids = Column(Text)
    prune_regex = Column(Text)
    enabled = Column(TINYINT(1), server_default=text("'0'"))
