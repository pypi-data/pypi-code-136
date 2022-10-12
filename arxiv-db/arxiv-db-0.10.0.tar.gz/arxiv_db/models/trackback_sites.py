
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_trackback_sites


class TrackbackSites(Base):
    __tablename__ = 'arXiv_trackback_sites'
    __table_args__ = (
        Index('arXiv_trackback_sites__pattern', 'pattern'),
    )

    pattern = Column(String(255), nullable=False, server_default=text("''"))
    site_id = Column(INTEGER, primary_key=True)
    action = Column(Enum('neutral', 'accept', 'reject', 'spam'), nullable=False, server_default=text("'neutral'"))
