from . import engine
from sqlalchemy.orm import sessionmaker

def open_session():
    Session = sessionmaker(bind=engine)
    return Session()

def close_session(session):
    session.close()