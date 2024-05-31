#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
import json


app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def show_username(username):
    return jsonify(users[username])


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
