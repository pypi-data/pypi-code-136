from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from cerberus.model.ParentModel import ParentModel

class AbstractModelResource(ParentModel):

	def __init__(self, url):
		ParentModel.__init__(AbstractModelResource,url)
		self.session = Session(self.engine, expire_on_commit=False)

	def update(self, obj):
		self.session.commit()
		self.session.close()

	def insert(self, obj):
		self.session.add(obj)
		self.session.commit()
		self.session.close()
