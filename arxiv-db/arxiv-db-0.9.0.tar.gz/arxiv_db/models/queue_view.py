from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_queue_view

from .tapir_users import TapirUsers

class QueueView(TapirUsers):
    __tablename__ = 'arXiv_queue_view'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_queue_view_ibfk_1'),
    )

    user_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    total_views = Column(INTEGER, nullable=False, server_default=text("'0'"))
    last_view = Column(DateTime)
    second_last_view = Column(DateTime)
