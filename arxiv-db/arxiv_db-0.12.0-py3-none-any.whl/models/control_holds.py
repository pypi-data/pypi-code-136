
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_control_holds


class ControlHolds(Base):
    __tablename__ = 'arXiv_control_holds'
    __table_args__ = (
        ForeignKeyConstraint(['last_changed_by'], ['tapir_users.user_id'], name='arXiv_control_holds_ibfk_2'),
        ForeignKeyConstraint(['placed_by'], ['tapir_users.user_id'], name='arXiv_control_holds_ibfk_1'),
        Index('control_id', 'control_id', 'hold_type', unique=True),
        Index('hold_reason', 'hold_reason'),
        Index('hold_status', 'hold_status'),
        Index('hold_type', 'hold_type'),
        Index('last_changed_by', 'last_changed_by'),
        Index('origin', 'origin'),
        Index('placed_by', 'placed_by')
    )

    hold_id = Column(INTEGER, primary_key=True)
    control_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    hold_type = Column(Enum('submission', 'cross', 'jref'), nullable=False, server_default=text("'submission'"))
    hold_status = Column(Enum('held', 'extended', 'accepted', 'rejected'), nullable=False, server_default=text("'held'"))
    hold_reason = Column(String(255), nullable=False, server_default=text("''"))
    hold_data = Column(String(255), nullable=False, server_default=text("''"))
    origin = Column(Enum('auto', 'user', 'admin', 'moderator'), nullable=False, server_default=text("'auto'"))
    placed_by = Column(INTEGER)
    last_changed_by = Column(INTEGER)

    tapir_users = relationship('TapirUsers', foreign_keys=[last_changed_by], back_populates='arXiv_control_holds')
    tapir_users_ = relationship('TapirUsers', foreign_keys=[placed_by], back_populates='arXiv_control_holds_')
