from flask import Flask
from .models import Base
from .models.country import Country
from .models.source import Source
from .models.destiny import Destiny
from sqlalchemy import create_engine

app = Flask(__name__)
from .routes import *

def create_app(enviroment):
	app.config.from_object(enviroment)
	DATABASE_URI = enviroment.DATABASE_URI
	Base.metadata.create_all(create_engine(DATABASE_URI))
	return app
