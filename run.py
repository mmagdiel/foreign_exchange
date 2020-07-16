from infrastructure.routes import app
from infrastructure.database_setup import engine
from infrastructure.application.domain.models import Base

if __name__== '__main__':
  Base.metadata.create_all(engine)
  app.run(port=7000, debug=True)
