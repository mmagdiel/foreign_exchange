import os
import json
import pandas as pd
from app.models.source import Source
from app.models.country import Country
from app.models.association import Association
from app.models import able_session

class Seeding:
	@able_session
	def __init__(self, session):
		countries = session.query(Country).all()

		if len(countries) == 0:
			ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
			FILE_PATH = os.path.join(ROOT_DIR, "currency.csv")
			self.df = pd.read_csv(filepath_or_buffer=FILE_PATH, sep=",")
			self.flat = True
		else: 
			self.flat = False

	@able_session
	def save_country_all(self, session):
		list_countries = []
		for country in pd.unique(self.df.Country):
			country_instance = Country(name=country)
			list_countries.append(country_instance)

		session.add_all(list_countries)


	@able_session
	def save_currency_all(self, session):
		list_currencies = []

		for code in pd.unique(self.df.Code):
			dd = self.df[self.df.Code == code]
			number = int(dd.Number.values[0])
			currency = dd.Currency.values[0]	

			currency_instance = Source(name=currency, iso=code, number=number)
			list_currencies.append(currency_instance)

		session.add_all(list_currencies)


	@able_session
	def merge_country_currency(self, session):
		countries = session.query(Country).all()
		collection = [country.to_dic() for country in countries]
		df_country = pd.DataFrame(collection)

		df_inter = pd.merge(left=self.df, right=df_country, on=None, left_on='Country', right_on='name_country')

		currencies = session.query(Source).all()
		collection = [currency.to_dic() for currency in currencies]
		df_currency = pd.DataFrame(collection)

		df_final = pd.merge(left=df_inter, right=df_currency, on=None, left_on='Code', right_on='iso')

		list_association = []
		for i in range(self.df.shape[0]):
			id_source = int(df_final.id_source.values[i])
			id_country = int(df_final.id_country.values[i])
			association = Association(country_id=id_country, source_id=id_source)
			list_association.append(association)

		session.add_all(list_association)