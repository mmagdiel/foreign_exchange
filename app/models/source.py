from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy import Column, ForeignKey, Integer, String


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    iso = Column(String, nullable=True)
    name = Column(String, nullable=False)

    country_id = Column(None, ForeignKey("countries.id"), nullable=False)
    country = relationship("Country", back_populates="country_sources")

    source_destinys = relationship("Destiny", back_populates="source")
    __table_args__ = (UniqueConstraint("iso", name="_iso_unique"),)