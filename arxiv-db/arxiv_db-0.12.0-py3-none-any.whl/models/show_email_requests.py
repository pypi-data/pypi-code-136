
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_show_email_requests


class ShowEmailRequests(Base):
    __tablename__ = 'arXiv_show_email_requests'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_show_email_requests_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_show_email_requests_ibfk_2'),
        Index('dated', 'dated'),
        Index('document_id', 'document_id'),
        Index('remote_addr', 'remote_addr'),
        Index('user_id', 'user_id', 'dated')
    )

    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    user_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    session_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    dated = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_allowed = Column(TINYINT, nullable=False, server_default=text("'0'"))
    remote_addr = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
    request_id = Column(INTEGER, primary_key=True)

    document = relationship('Documents', back_populates='arXiv_show_email_requests')
    user = relationship('TapirUsers', back_populates='arXiv_show_email_requests')
