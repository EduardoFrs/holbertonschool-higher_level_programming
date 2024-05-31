#!/usr/bin/python3
from flask import Flask
from flask import jsonify


app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


if __name__ == "__main__":
    app.run(port=5000)
