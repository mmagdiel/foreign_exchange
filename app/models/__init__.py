from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite")

def able_session(fn):
    def gn(*args, **kwargs):
        Session = sessionmaker(bind=engine)
        session = Session()
        res = fn(*args, session, **kwargs)
        session.commit()
        session.close()
        return res
    return gn