from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_policy_classes


class TapirPolicyClasses(Base):
    __tablename__ = 'tapir_policy_classes'

    ADMIN = 1
    PUBLIC_USER = 2
    LEGACY_USER = 3
    POLICY_CLASSES = [
        {"name": "Administrator", "class_id": ADMIN, "description": ""},
        {"name": "Public user", "class_id": PUBLIC_USER, "description": ""},
        {"name": "Legacy user", "class_id": LEGACY_USER, "description": ""}
    ]

    class_id = Column(SMALLINT, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("''"))
    description = Column(Text, nullable=False)
    password_storage = Column(INTEGER, nullable=False, server_default=text("'0'"))
    recovery_policy = Column(INTEGER, nullable=False, server_default=text("'0'"))
    permanent_login = Column(Integer, nullable=False, server_default=text("'0'"))

    tapir_users = relationship('TapirUsers', back_populates='tapir_policy_classes')

    @staticmethod
    def insert_policy_classes(session) -> None:
        """Insert all the policy classes for legacy."""
        data = session.query(TapirPolicyClasses).all()
        if data:
            return

        for datum in TapirPolicyClasses.POLICY_CLASSES:
            session.add(TapirPolicyClasses(**datum))
