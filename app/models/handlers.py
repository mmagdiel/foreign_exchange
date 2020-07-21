from app.models import able_session
from app.models.source import Source
from app.models.country import Country
from app.models.destiny import Destiny
from app.models.association import Association

class Handlers:
	@able_session
	def countries(self, session):
		countries = session.query(Country).all()
		collection = [country.to_dic() for country in countries]
		return collection

	@able_session
	def associations(self, session):
		associations = session.query(Association).all()
		collection = [association.to_dic() for association in associations]
		return collection

	@able_session
	def sources(self, session):
		sources = session.query(Source).all()
		collection = [source.to_dic() for source in sources]
		return collection

	@able_session
	def destinies(self, session):
		destinies = session.query(Destiny).all()
		collection = [destiny.to_dic() for destiny in destinies]
		print(collection)
		return collection
