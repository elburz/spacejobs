import os
from flask import Flask, url_for, render_template
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
    return render_template("main.html")


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/metrics')
def metrics():
	return render_template("metrics.html")


@app.route('/submit')
def submit():
	return render_template("submit.html")
