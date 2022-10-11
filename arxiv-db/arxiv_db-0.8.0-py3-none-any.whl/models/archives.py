
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_archives


class Archives(Base):
    __tablename__ = 'arXiv_archives'
    __table_args__ = (
        ForeignKeyConstraint(['in_group'], ['arXiv_groups.group_id'], name='0_576'),
        Index('in_group', 'in_group')
    )

    archive_id = Column(String(16), primary_key=True, server_default=text("''"))
    in_group = Column(String(16), nullable=False, server_default=text("''"))
    archive_name = Column(String(255), nullable=False, server_default=text("''"))
    start_date = Column(String(4), nullable=False, server_default=text("''"))
    end_date = Column(String(4), nullable=False, server_default=text("''"))
    subdivided = Column(INTEGER, nullable=False, server_default=text("'0'"))

    arXiv_groups = relationship('Groups', back_populates='arXiv_archives')
    arXiv_categories = relationship('Categories', back_populates='arXiv_archives')
