from flask import Flask
from .models import Base, engine
from .models.country import Country
from .models.source import Source
from .models.association import Association
from .models.destiny import Destiny
from sqlalchemy import create_engine
from .models.populate import load_catalog

app = Flask(__name__)
from .routes import *

def create_app(enviroment):
	app.config.from_object(enviroment)
	DATABASE_URI = enviroment.DATABASE_URI
	Base.metadata.create_all(engine)
	load_catalog()
	return app
