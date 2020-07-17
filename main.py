from app import create_app
from app.config import config
from app.models.populate import load_catalog

enviroment = config['development']
app = create_app(enviroment)

if __name__ == '__main__':
	load_catalog()
	app.run()