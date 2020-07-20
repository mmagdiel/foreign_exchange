import os
import json
import pandas as pd
from .source import Source
from .country import Country
from .association import Association
from .operations import open_session, close_session, able_session

@able_session
def load_catalog(session):
	countries = session.query(Country).all()
	if len(countries) == 0:
		ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
		FILE_PATH = os.path.join(ROOT_DIR, "currency.csv")
		df = pd.read_csv(filepath_or_buffer=FILE_PATH, sep=",")
		save_country_all(df)


def save_country_all(df):
	session = open_session()
	list_countries = []
	for country in pd.unique(df.Country):
		country_instance = Country(name=country)
		list_countries.append(country_instance)

	session.add_all(list_countries)
	close_session(session)
	save_currency_all(df)


def save_currency_all(df):
	session = open_session()
	list_currencies = []

	for code in pd.unique(df.Code):
		dd = df[df.Code == code]
		number = int(dd.Number.values[0])
		currency = dd.Currency.values[0]	

		currency_instance = Source(name=currency, iso=code, number=number)
		list_currencies.append(currency_instance)

	session.add_all(list_currencies)
	close_session(session)
	merge_country_currency(df)


def merge_country_currency(df):
	session = open_session()

	countries = session.query(Country).all()
	collection = [country.to_dic() for country in countries]
	df_country = pd.DataFrame(collection)

	df_inter = pd.merge(left=df, right=df_country, on=None, left_on='Country', right_on='name_country')

	currencies = session.query(Source).all()
	collection = [currency.to_dic() for currency in currencies]
	df_currency = pd.DataFrame(collection)

	df_final = pd.merge(left=df_inter, right=df_currency, on=None, left_on='Code', right_on='iso')
	
	list_association = []
	for i in range(df.shape[0]):
		id_source = int(df_final.id_source.values[i])
		id_country = int(df_final.id_country.values[i])
		association = Association(country_id=id_country, source_id=id_source)
		list_association.append(association)

	session.add_all(list_association)
	close_session(session)