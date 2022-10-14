from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_questionable_categories

from .categories import Categories

class QuestionableCategories(Categories):
    __tablename__ = 'arXiv_questionable_categories'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'],
                             ['arXiv_categories.archive', 'arXiv_categories.subject_class'],
                             name='0_756'),
    )

    archive = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
    subject_class = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
