import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


@app.route('/')
def main():
    return "main page"


@app.route('/metrics')
def metrics():
	return "metrics"


@app.route('/submit')
def submit():
	return "submit here"
