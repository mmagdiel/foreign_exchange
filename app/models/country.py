from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    country_sources = relationship("Source", back_populates="country")

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

