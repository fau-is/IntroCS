from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "You are at the index page!"

@app.route("/abcd")
def sample():
    return "You are on the sample page!"























@app.route("/show/<number>")
def show(number):
	return f"You passed in {number}."
