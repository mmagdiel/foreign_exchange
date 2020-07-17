from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy import Column, Float, ForeignKey, Integer, String


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    iso = Column(String, nullable=True)
    name = Column(String, nullable=False)

    source_destinys = relationship("Destiny", back_populates="source")
    __table_args__ = (UniqueConstraint("iso", name="_iso_unique"),)