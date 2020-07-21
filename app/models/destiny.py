import datetime
from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime

class Destiny(Base):
    __tablename__ = "destinys"

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=True)
    iso = Column(String, nullable=True)
    value = Column(Float, nullable=True)
    onCreated = Column(DateTime, default=datetime.datetime.utcnow)

    source_id = Column(None, ForeignKey("sources.id"), nullable=False)
    source = relationship("Source", back_populates="source_destinys")

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, iso: {self.iso}, value: {self.value}, onCreated: {self.onCreated}'

    def to_dic(self):
        return { 'id_country': self.id, 'name_country': self.name, 'iso': self.iso, 'value': self.value, 'onCreated': self.onCreated }