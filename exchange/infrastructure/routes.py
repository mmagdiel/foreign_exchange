from flask import Flask
from loader import main

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world!"


@app.route('/load_data')
def load():
    return main()
