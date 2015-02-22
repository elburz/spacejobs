import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


# database models
class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	position = db.Column(db.String(120))
	agency = db.Column(db.String(120))
	description = db.Column(db.Text)
	location = db.Column(db.String(120))
	term = db.Column(db.String(120))
	date_added = db.Column(db.Date)
	apply_link = db.Column(db.Text)

	def __init__(self, position, agency, description, location, term, date_added, apply_link):
		self.position = position
		self.agency = agency
		self.description = description
		self.location = location
		self.term = term
		self.date_added = date_added
		self.apply_link = apply_link

	def __repr__(self):
		return '<Job %r>' % self.position


@app.route('/')
def main():
    return "main page"


@app.route('/metrics')
def metrics():
	return "metrics"


@app.route('/submit')
def submit():
	return "submit here"
