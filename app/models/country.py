from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    country_sources = relationship("Source", back_populates="countries")

