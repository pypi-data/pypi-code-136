
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_versions


class Versions(Base):
    __tablename__ = 'arXiv_versions'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_versions_ibfk_1'),
        Index('freeze_date', 'freeze_date'),
        Index('publish_date', 'publish_date'),
        Index('request_date', 'request_date')
    )

    document_id = Column(MEDIUMINT, primary_key=True, nullable=False, server_default=text("'0'"))
    version = Column(TINYINT, primary_key=True, nullable=False, server_default=text("'0'"))
    request_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    freeze_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    publish_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_current = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))

    document = relationship('Documents', back_populates='arXiv_versions')
