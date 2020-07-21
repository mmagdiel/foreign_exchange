from app import app

@app.route('/')
def index():
    return "hello world!"


@app.route('/load_data')
def load():
    return "Hola" 