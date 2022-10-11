from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

import podarr


class User(podarr.BASE_MODEL):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    enabled = Column(Boolean, default=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)

    def dict(self):
        return {
            'id': self.id,
            'enabled': self.enabled,
            'email': self.email,
            'name': self.name,
        }


class Service(podarr.BASE_MODEL):

    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    repr = Column(String, unique=True)
    priority = Column(Integer)
    enabled = Column(Boolean, default=False)
    image = Column(String, nullable=True)
    tag = Column(String, nullable=True)
    locks = relationship('Lock', backref='service', uselist=True)
    ports = relationship('Port', backref='service', uselist=True)
    remote = Column(String, nullable=True, default=None)

    def dict(self):
        return {
            'id': self.id,
            'enabled': self.enabled,
            'name': self.name,
            'repr': self.repr,
            'priority': self.priority,
            'image': self.image,
            'tag': self.tag,
            'ports': self.ports,
            'lock': self.locks,
            'remote': self.remote,
        }


class Lock(podarr.BASE_MODEL):

    __tablename__ = 'locks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    datetime = Column(DateTime, nullable=True, default=None)
    service_id = Column(Integer, ForeignKey('services.id'))


class Port(podarr.BASE_MODEL):

    __tablename__ = 'ports'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True)
    service_id = Column(Integer, ForeignKey('services.id'))
