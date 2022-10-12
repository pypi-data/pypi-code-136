
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_mirror_list


class MirrorList(Base):
    __tablename__ = 'arXiv_mirror_list'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_mirror_list_fk_document_id'),
        Index('arXiv_mirror_list_idx_document_id', 'document_id')
    )

    mirror_list_id = Column(Integer, primary_key=True)
    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    version = Column(Integer, nullable=False, server_default=text("'1'"))
    write_source = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    write_abs = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_written = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    created = Column(DateTime)
    updated = Column(DateTime)

    document = relationship('Documents', back_populates='arXiv_mirror_list')
