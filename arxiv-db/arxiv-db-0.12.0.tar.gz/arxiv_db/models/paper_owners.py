from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKey, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import RelationshipProperty, relationship

from arxiv_db.models.sqa_types import EpochIntArxivTz

from .. import Base

metadata = Base.metadata

from .documents import Documents
from .tapir_users import TapirUsers

# arXiv_paper_owners

class PaperOwners(Base):
    __tablename__ = 'arXiv_paper_owners'
    __table_args__ = (
        ForeignKeyConstraint(['added_by'], ['tapir_users.user_id'], name='0_595'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_593'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_594'),
        Index('added_by', 'added_by'),
        Index('document_id', 'document_id', 'user_id', unique=True),
        Index('user_id', 'user_id'),
        )

    document_id = Column(ForeignKey(Documents.document_id), primary_key=True)
    """Note that this is not a primary_key in the DB schema, just in the ORM"""

    user_id = Column(ForeignKey(TapirUsers.user_id), primary_key=True)
    """Note that this is not a primary_key in the DB schema, just in the ORM"""

    date = Column('date', EpochIntArxivTz, nullable=False, server_default=text("'0'"))
    added_by = Column('added_by', INTEGER, nullable=False, server_default=text("'0'"))
    remote_addr = Column('remote_addr', String(16), nullable=False, server_default=text("''"))
    remote_host = Column('remote_host', String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column('tracking_cookie', String(32), nullable=False, server_default=text("''"))
    valid = Column('valid', INTEGER, nullable=False, server_default=text("'0'"))
    flag_author = Column('flag_author', INTEGER, nullable=False, server_default=text("'0'"))
    flag_auto = Column('flag_auto', INTEGER, nullable=False, server_default=text("'1'"))

    document = relationship('Documents', back_populates='owners')
    owner = relationship('TapirUsers', foreign_keys="[PaperOwners.user_id]", back_populates='owned_papers')
