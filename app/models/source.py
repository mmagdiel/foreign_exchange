import datetime
from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    iso = Column(String, nullable=False)
    name = Column(String, nullable=True)
    number= Column(Integer, nullable=True)
    onCreated = Column(DateTime, default=datetime.datetime.utcnow)

    countries = relationship("Association", back_populates="source")

    source_destinys = relationship("Destiny", back_populates="source")
    __table_args__ = (UniqueConstraint("iso", name="_iso_unique"),)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, iso: {self.iso}, number: {self.number}, onCreated: {self.onCreated}'

    def to_dic(self):
        return { 'id_source': self.id, 'name_source': self.name, 'iso': self.iso, 'number': {self.number}, 'onCreated': {self.onCreated} }