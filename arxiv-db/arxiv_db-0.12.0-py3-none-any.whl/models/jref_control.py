
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_jref_control


class JrefControl(Base):
    __tablename__ = 'arXiv_jref_control'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_jref_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_jref_control_ibfk_2'),
        Index('document_id', 'document_id', 'version', unique=True),
        Index('freeze_date', 'freeze_date'),
        Index('status', 'status'),
        Index('user_id', 'user_id')
    )

    control_id = Column(INTEGER, primary_key=True)
    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    version = Column(TINYINT, nullable=False, server_default=text("'0'"))
    user_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    status = Column(Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'"))
    jref = Column(String(255), nullable=False, server_default=text("''"))
    request_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    freeze_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    publish_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_must_notify = Column(Enum('0', '1'), server_default=text("'1'"))

    document = relationship('Documents', back_populates='arXiv_jref_control')
    user = relationship('TapirUsers', back_populates='arXiv_jref_control')
