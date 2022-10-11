
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_next_mail


class NextMail(Base):
    __tablename__ = 'arXiv_next_mail'
    __table_args__ = (
        Index('arXiv_next_mail_idx_document_id', 'document_id'),
        Index('arXiv_next_mail_idx_document_id_version', 'document_id', 'version')
    )

    next_mail_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer, nullable=False)
    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    version = Column(Integer, nullable=False, server_default=text("'1'"))
    type = Column(String(255), nullable=False, server_default=text("'new'"))
    is_written = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    paper_id = Column(String(20))
    extra = Column(String(255))
    mail_id = Column(CHAR(6))
