from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    sources = relationship("Association", back_populates="country")
    
    __table_args__ = (UniqueConstraint("name", name="_name_unique"),)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

    def to_dic(self):
        return { 'id_country': self.id, 'name_country': self.name }