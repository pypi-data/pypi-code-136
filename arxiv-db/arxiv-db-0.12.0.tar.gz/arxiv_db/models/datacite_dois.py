
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_datacite_dois


class DataciteDois(Base):
    __tablename__ = 'arXiv_datacite_dois'
    __table_args__ = (
        ForeignKeyConstraint(['metadata_id'], ['arXiv_metadata.metadata_id'], name='arXiv_datacite_dois_ibfk_1'),
        Index('account_paper_id', 'account', 'paper_id', unique=True),
        Index('metadata_id', 'metadata_id')
    )

    doi = Column(String(255), primary_key=True)
    metadata_id = Column(Integer, nullable=False)
    paper_id = Column(String(64), nullable=False)
    account = Column(Enum('test', 'prod'))
    created = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    metadata_ = relationship('Metadata', back_populates='arXiv_datacite_dois')
