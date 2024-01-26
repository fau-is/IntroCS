from flask import Flask, url_for, redirect, session

app = Flask(__name__)

@app.route("/")
def index():
	return '<a href="' + url_for('login') + '">Login</a>'

@app.route("/login")
def login():
	return redirect(url_for('foo'))

@app.route("/foo")
def foo():
	print(session)
	return 'Foo'
