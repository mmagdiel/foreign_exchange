from . import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, ForeignKey, Integer, String

class Destiny(Base):
    __tablename__ = "destinys"

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=True)
    iso = Column(String, nullable=True)
    value = Column(Float, nullable=True)

    source_id = Column(None, ForeignKey("sources.id"), nullable=False)
    source = relationship("Source", back_populates="source_destinys")