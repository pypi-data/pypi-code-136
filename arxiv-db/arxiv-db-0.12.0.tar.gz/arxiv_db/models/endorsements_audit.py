from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_endorsements_audit

from .endorsements import Endorsements

class EndorsementsAudit(Base):
    __tablename__ = 'arXiv_endorsements_audit'
    __table_args__ = (
        ForeignKeyConstraint(['endorsement_id'], ['arXiv_endorsements.endorsement_id'], name='0_732'),
    )

    endorsement_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    session_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    remote_addr = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
    flag_knows_personally = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_seen_paper = Column(INTEGER, nullable=False, server_default=text("'0'"))
    comment = Column(Text)
