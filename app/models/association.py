import datetime
from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer,String, DateTime
from sqlalchemy.sql.schema import UniqueConstraint


class Association(Base):
	__tablename__ = 'association'

	country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)
	source_id = Column(Integer, ForeignKey('sources.id'), primary_key=True)
	onCreated = Column(DateTime, default=datetime.datetime.utcnow)

	source = relationship("Source", back_populates="countries")
	country = relationship("Country", back_populates="sources")