from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_versions_checksum

from .versions import Versions

class VersionsChecksum(Versions):
    __tablename__ = 'arXiv_versions_checksum'
    __table_args__ = (
        ForeignKeyConstraint(['document_id', 'version'], ['arXiv_versions.document_id', 'arXiv_versions.version'], name='arXiv_versions_checksum_ibfk_1'),
        Index('abs_md5sum', 'abs_md5sum'),
        Index('abs_size', 'abs_size'),
        Index('src_md5sum', 'src_md5sum'),
        Index('src_size', 'src_size')
    )

    document_id = Column(MEDIUMINT, primary_key=True, nullable=False, server_default=text("'0'"))
    version = Column(TINYINT, primary_key=True, nullable=False, server_default=text("'0'"))
    flag_abs_present = Column(INTEGER, nullable=False, server_default=text("'0'"))
    abs_size = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_src_present = Column(TINYINT, nullable=False, server_default=text("'0'"))
    src_size = Column(INTEGER, nullable=False, server_default=text("'0'"))
    abs_md5sum = Column(BINARY(16))
    src_md5sum = Column(BINARY(16))
