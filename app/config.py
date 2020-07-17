class Config:
	DATABASE_URI = "sqlite:///db.sqlite"

class DevelopmentConfig(Config):
	DEBUG  = True

config = {
	'development': DevelopmentConfig
}