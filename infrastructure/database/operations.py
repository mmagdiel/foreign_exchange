from infrastructure.database.setup import engine

def open_session():
    Session = sessionmaker(bind=engine)
    return Session()

