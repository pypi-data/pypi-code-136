from typing import List

from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_demographics

class Demographics(Base):
    __tablename__ = 'arXiv_demographics'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_588'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_587'),
        Index('archive', 'archive', 'subject_class'),
        Index('country', 'country'),
        Index('flag_group_cs', 'flag_group_cs'),
        Index('flag_group_econ', 'flag_group_econ'),
        Index('flag_group_eess', 'flag_group_eess'),
        Index('flag_group_math', 'flag_group_math'),
        Index('flag_group_nlin', 'flag_group_nlin'),
        Index('flag_group_physics', 'flag_group_physics'),
        Index('flag_group_q_bio', 'flag_group_q_bio'),
        Index('flag_group_q_fin', 'flag_group_q_fin'),
        Index('flag_group_stat', 'flag_group_stat'),
        Index('flag_journal', 'flag_journal'),
        Index('flag_proxy', 'flag_proxy'),
        Index('flag_suspect', 'flag_suspect'),
        Index('flag_xml', 'flag_xml'),
        Index('type', 'type')
    )

    user_id = Column(INTEGER, primary_key=True, server_default=text("'0'"), )
    country = Column(CHAR(2), nullable=False, server_default=text("''"))
    affiliation = Column(String(255), nullable=False, server_default=text("''"))
    url = Column(String(255), nullable=False, server_default=text("''"))
    original_subject_classes = Column(String(255), nullable=False, server_default=text("''"))
    flag_group_math = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_cs = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_nlin = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_proxy = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_journal = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_xml = Column(INTEGER, nullable=False, server_default=text("'0'"))
    dirty = Column(INTEGER, nullable=False, server_default=text("'2'"))
    flag_group_test = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_suspect = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_q_bio = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_q_fin = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_stat = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_eess = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_group_econ = Column(INTEGER, nullable=False, server_default=text("'0'"))
    veto_status = Column(Enum('ok', 'no-endorse', 'no-upload', 'no-replace'), nullable=False, server_default=text("'ok'"))
    type = Column(SMALLINT)
    archive = Column(String(16))
    subject_class = Column(String(16))
    flag_group_physics = Column(INTEGER)

    arXiv_categories = relationship('Categories', back_populates='arXiv_demographics')

    TYPE_CHOICES = [
        (1, 'Staff'),
        (2, "Professor"),
        (3, "Post Doc"),
        (4, "Grad Student"),
        (5, "Other")
    ]
    """Legacy ranks in arXiv user profiles."""


    GROUP_FLAGS = [
        ('grp_physics', 'flag_group_physics'),
        ('grp_math', 'flag_group_math'),
        ('grp_cs', 'flag_group_cs'),
        ('grp_q-bio', 'flag_group_q_bio'),
        ('grp_q-fin', 'flag_group_q_fin'),
        ('grp_q-stat', 'flag_group_stat'),
        ('grp_q-econ', 'flag_group_econ'),
        ('grp_eess', 'flag_group_eess'),
    ]

    @property
    def groups(self) -> List[str]:
        """Active groups for this user profile."""
        return [group for group, column in self.GROUP_FLAGS
                if getattr(self, column) == 1]
