from flask import Flask
from .models import Base
from sqlalchemy import create_engine

app = Flask(__name__)
from .routes import *

def create_app(enviroment):
	app.config.from_object(enviroment)
	DATABASE_URI = enviroment.DATABASE_URI
	Base.metadata.create_all(create_engine(DATABASE_URI))
	return app
