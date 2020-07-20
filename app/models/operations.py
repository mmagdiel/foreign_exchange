from . import engine
from sqlalchemy.orm import sessionmaker

def open_session():
    Session = sessionmaker(bind=engine)
    return Session()

def close_session(session):
    session.commit()
    session.close()

def able_session(fn):
    def gn(*args, **kwargs):
        Session = sessionmaker(bind=engine)
        session = Session()
        fn(session, *args, **kwargs)
        session.commit()
        session.close()
    return gn