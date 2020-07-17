import pandas as pd
import os
from . import open_session, close_session


def load_catalog():
	ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
	FILE_PATH = os.path.join(ROOT_DIR, "currency.csv")

	currency = pd.read_csv(filepath_or_buffer=FILE_PATH, sep=",",)
	df = currency[currency.Code == iso_new]
	name_new = df.Currency.values[0]


def save_country_all():
	open_session()
	close_session()

def save_currency_all():
	pass