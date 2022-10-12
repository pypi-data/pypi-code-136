
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_licenses


class Licenses(Base):
    __tablename__ = 'arXiv_licenses'

    name = Column(String(255), primary_key=True)
    label = Column(String(255))
    active = Column(TINYINT(1), server_default=text("'1'"))
    note = Column(String(400))
    sequence = Column(TINYINT)

    arXiv_metadata = relationship('Metadata', back_populates='arXiv_licenses')
    arXiv_submissions = relationship('Submissions', back_populates='arXiv_licenses')
