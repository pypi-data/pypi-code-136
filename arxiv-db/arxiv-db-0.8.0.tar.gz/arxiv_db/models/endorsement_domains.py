
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_endorsement_domains


class EndorsementDomains(Base):
    __tablename__ = 'arXiv_endorsement_domains'

    endorsement_domain = Column(String(32), primary_key=True, server_default=text("''"))
    endorse_all = Column(Enum('y', 'n'), nullable=False, server_default=text("'n'"))
    mods_endorse_all = Column(Enum('y', 'n'), nullable=False, server_default=text("'n'"))
    endorse_email = Column(Enum('y', 'n'), nullable=False, server_default=text("'y'"))
    papers_to_endorse = Column(SMALLINT, nullable=False, server_default=text("'4'"))

    arXiv_categories = relationship('Categories', back_populates='arXiv_endorsement_domains')
