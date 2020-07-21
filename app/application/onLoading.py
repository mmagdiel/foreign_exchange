from app.models.seeding import Seeding
from app.domain.migrate import IMigrate


class OnLoading(IMigrate):
	def __init__(self):
		self.seed = Seeding()
	
	def	onLoadCatalog(self):
		if self.seed.flat:
			self.seed.save_country_all()
			self.seed.save_currency_all()
			self.seed.merge_country_currency()
