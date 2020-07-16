from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint

Base = declarative_base()


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    iso = Column(String, nullable=True)
    name = Column(String, nullable=False)

    source_destinys = relationship("Destiny", back_populates="source")
    __table_args__ = (UniqueConstraint("iso", name="_iso_unique"),)


class Destiny(Base):
    __tablename__ = "destinys"

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=True)
    iso = Column(String, nullable=True)
    value = Column(Float, nullable=True)

    source_id = Column(None, ForeignKey("sources.id"), nullable=False)
    source = relationship("Source", back_populates="source_destinys")

