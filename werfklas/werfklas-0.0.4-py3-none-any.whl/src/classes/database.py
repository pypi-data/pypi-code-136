from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, Session
from src.modules.config import load_config
from os.path import exists


config = load_config()
def sessionSetup():
    engine = create_engine(
        f'sqlite:///{config["database"]["path"] + config["database"]["name"]}' + '?check_same_thread=False',
        echo=False,
    )
    return Session(bind=engine, autoflush=True)


def __init__():
    session = sessionSetup()


Base = declarative_base()


class Audit(Base):
    __tablename__ = 'tbl_audit'
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    action = Column(String)
    uuid = Column(String)

    def __init__(self, aid, date, action, uuid):
        super().__init__()
        self.aid = aid
        self.date = date
        self.action = action
        self.uuid = uuid


class Teacher(Base):
    __tablename__ = 'tbl_teachers'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    uuid = Column(String)

    def __init__(self, tid, firstname, lastname, uuid):
        super().__init__()
        self.tid = tid
        self.firstname = firstname
        self.lastname = lastname
        self.uuid = uuid


class Class(Base):
    __tablename__ = 'tbl_classrooms'
    id = Column(Integer, primary_key=True)
    class_name = Column(String)
    teacher_uuid = Column(String, ForeignKey('tbl_teachers.uuid'))
    teacher = relationship("Teacher", foreign_keys=[teacher_uuid])
    start_date = Column(Integer)
    end_date = Column(Integer)
    uuid = Column(String)

    def __init__(self, class_id, class_name, teacher_uuid, start_date, end_date, uuid):
        super().__init__()
        self.class_id = class_id
        self.class_name = class_name
        self.teacher_uuid = teacher_uuid
        self.start_date = start_date
        self.end_date = end_date
        self.uuid = uuid


class Parent(Base):
    __tablename__ = 'tbl_parents'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    zipcode = Column(String)
    city = Column(String)
    email = Column(String)
    phone = Column(String)
    uuid = Column(String)

    def __init__(self, oid, firstname, lastname, address, zipcode, city, email, phone, uuid):
        super().__init__()
        self.oid = oid
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.zipcode = zipcode
        self.city = city
        self.email = email
        self.phone = phone
        self.uuid = uuid


class Family(Base):
    __tablename__ = 'tbl_families'
    id = Column(Integer, primary_key=True)
    parent1_uuid = Column(String, ForeignKey('tbl_parents.uuid'))
    parent1 = relationship("Parent", foreign_keys=[parent1_uuid])
    parent2_uuid = Column(String, ForeignKey('tbl_parents.uuid'))
    parent2 = relationship("Parent", foreign_keys=[parent2_uuid])
    divorced = Column(Integer)
    uuid = Column(String)

    def __init__(self, oid, parent1_uuid, parent2_uuid, divorced, uuid):
        super().__init__()
        self.oid = oid
        self.parent1_uuid = parent1_uuid
        self.parent2_uuid = parent2_uuid
        self.divorced = divorced
        self.uuid = uuid


class Child(Base):
    __tablename__ = 'tbl_children'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    date_of_registration = Column(Integer)
    family_uuid = Column(String, ForeignKey('tbl_families.uuid'))
    family = relationship("Family", foreign_keys=[family_uuid])
    date_of_birth = Column(Integer)
    class1_uuid = Column(String, ForeignKey('tbl_classrooms.uuid'))
    classroom1 = relationship("Class", foreign_keys=[class1_uuid])
    class2_uuid = Column(String, ForeignKey('tbl_classrooms.uuid'))
    classroom2 = relationship("Class", foreign_keys=[class2_uuid])
    class3_uuid = Column(String, ForeignKey('tbl_classrooms.uuid'))
    classroom3 = relationship("Class", foreign_keys=[class3_uuid])
    uuid = Column(String)

    def __init__(self, kid, firstname, lastname, date_of_registration, family_uuid, date_of_birth, class1_uuid,
                 class2_uuid, class3_uuid, uuid):
        super().__init__()
        self.kid = kid
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_registration = date_of_registration
        self.family_uuid = family_uuid
        self.date_of_birth = date_of_birth
        self.class1_uuid = class1_uuid
        self.class2_uuid = class2_uuid
        self.class3_uuid = class3_uuid
        self.uuid = uuid


def create_database(databasefile):
    engine = create_engine('sqlite:////' + databasefile, echo=True)
    Base.metadata.create_all(engine)


def test_database(databasefile):
    # Check if database exists. If not, create it.
    file_exists = exists(databasefile)
    if not file_exists:
        print(f'Database aanmaken..')
        create_database(databasefile=databasefile)

if __name__ == '__main__':
#     .run(debug=True)
    create_database(databasefile='/home/yvesvanelk/Git/werfklas/werfklas.db')
# def __init__(self):

# ------ lisnters
