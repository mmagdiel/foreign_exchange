from app import app
from flask import jsonify
from app.models.handlers import Handlers

@app.route('/')
def index():
    return "hello world!"


@app.route('/load_data')
def load():
    return "Hola" 


@app.route('/countries')
def countries():
    res = Handlers().countries()
    return jsonify(res), 200


@app.route('/sources')
def sources():
    res = Handlers().sources()
    return jsonify(res), 200  


@app.route('/destinies')
def destinies():
    res = Handlers().destinies()
    return jsonify(res), 200  


@app.route('/associations')
def associations():
    res = Handlers().associations()
    return jsonify(res), 200