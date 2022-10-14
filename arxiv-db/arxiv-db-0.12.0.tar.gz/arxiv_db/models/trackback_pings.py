
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_trackback_pings


class TrackbackPings(Base):
    __tablename__ = 'arXiv_trackback_pings'
    __table_args__ = (
        Index('arXiv_trackback_pings__document_id', 'document_id'),
        Index('arXiv_trackback_pings__posted_date', 'posted_date'),
        Index('arXiv_trackback_pings__status', 'status'),
        Index('arXiv_trackback_pings__url', 'url')
    )

    trackback_id = Column(MEDIUMINT, primary_key=True)
    title = Column(String(255), nullable=False, server_default=text("''"))
    excerpt = Column(String(255), nullable=False, server_default=text("''"))
    url = Column(String(255), nullable=False, server_default=text("''"))
    blog_name = Column(String(255), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    remote_addr = Column(String(16), nullable=False, server_default=text("''"))
    posted_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    is_stale = Column(TINYINT, nullable=False, server_default=text("'0'"))
    approved_by_user = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    approved_time = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(Enum('pending', 'pending2', 'accepted', 'rejected', 'spam'), nullable=False, server_default=text("'pending'"))
    document_id = Column(MEDIUMINT)
    site_id = Column(INTEGER)
