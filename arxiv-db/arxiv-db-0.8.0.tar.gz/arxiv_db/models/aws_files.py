
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_aws_files


class AwsFiles(Base):
    __tablename__ = 'arXiv_aws_files'
    __table_args__ = (
        Index('type', 'type'),
    )

    type = Column(String(10), nullable=False, server_default=text("''"))
    filename = Column(String(100), primary_key=True, server_default=text("''"))
    md5sum = Column(String(50))
    content_md5sum = Column(String(50))
    size = Column(Integer)
    timestamp = Column(DateTime)
    yymm = Column(String(4))
    seq_num = Column(Integer)
    first_item = Column(String(20))
    last_item = Column(String(20))
    num_items = Column(Integer)
