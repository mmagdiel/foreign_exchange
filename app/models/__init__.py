from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite")


"""
print(config)
from app.config import Config
import DATABASE_URI
.config.get('DATABASE_URI')
from sqlalchemy import create_engine
engine = create_engine(enviroment.DATABASE_URI)
"""