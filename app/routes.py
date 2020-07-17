from flask import Flask, jsonify
from app.infrastructure.loader import main

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world!"


@app.route('/load_data')
def load():
    return jsonify(main()), 200

