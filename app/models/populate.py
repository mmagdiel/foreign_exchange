import pandas as pd
import os
from .operations import open_session, close_session
from .country import Country
from .source import Source

def load_catalog():
	ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
	FILE_PATH = os.path.join(ROOT_DIR, "currency.csv")

	session = open_session()
	fd = pd.read_csv(filepath_or_buffer=FILE_PATH, sep=",")
	df = fd.notnull()

	for i in range(df.shape[0]):
		country = Country(name=df.Country.values[i])
		session.add(country)
		session.flush()

		session.commit()
		
	close_session(session)

def save_country_all():
	pass
def save_currency_all():
	pass