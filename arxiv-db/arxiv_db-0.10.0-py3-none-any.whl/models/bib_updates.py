
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_bib_updates


class BibUpdates(Base):
    __tablename__ = 'arXiv_bib_updates'

    update_id = Column(MEDIUMINT, primary_key=True)
    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    bib_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    updated = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    journal_ref = Column(Text)
    doi = Column(Text)
