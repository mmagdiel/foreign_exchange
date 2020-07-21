from flask import Flask
from .models import Base, engine
from .models.country import Country
from .models.source import Source
from .models.association import Association
from .models.destiny import Destiny
from sqlalchemy import create_engine
from .application.onLoading import OnLoading

app = Flask(__name__)
from .infrastructure import *

def create_app(enviroment):
	app.config.from_object(enviroment)
	Base.metadata.create_all(engine)
	seed = OnLoading()
	seed.onLoadCatalog()
	return app
