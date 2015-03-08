import os
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

'''
class JobListing(db.Model):
	# __tablename__ = 'scrapedresults'

	id = db.Column(db.Integer, primary_key=True)
	term = db.Column(db.Text)
	location = db.Column(db.Text)
	jobPosition = db.Column(db.Text)
	department = db.Column(db.Text)
	agency = db.Column(db.Text)
	datePosted = db.Column(db.Text)
	link = db.Column(db.Text)

	def __init__(self, term, location, jobPosition, department, agency, datePosted, link):
		self.term = term
		self.location = location
		self.jobPosition = jobPosition
		self.department = department
		self.agency = agency
		self.datePosted = datePosted
		self.link = link

	def __repr__(self):
		return self.jobPosition
'''


class JobListing():

	def __init__(self):
		self.id = 1
		self.term = 'test'
		self.location = '12345'
		self.jobPosition = '67890'
		self.department = 'asdfg'
		self.agency = 'qwert'
		self.datePosted = 'zxcvb'
		self.link = 'hjk;g'

jobTest = JobListing()


@app.route('/', methods=['GET', 'POST'])
def main():

	# switch header if someone subscribes
	subscribe_bool = False
	# if subscribe button clicked
	if request.method == 'POST':
		if request.form['submit'] == 'email_subscribe':
			# grab info
			email_address = request.form['email_address']
			date = datetime.date.today()

			# add to database here

			# swap message with bool
			subscribe_bool = True

			
	# return render_template("main.html", subscribe_bool=subscribe_bool, jobPostings=JobListing.query.all())
	return render_template("main.html", subscribe_bool=subscribe_bool, jobPostings=jobTest.term)
	
	# return render_template("main.html", subscribe_bool=subscribe_bool)


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/metrics')
def metrics():
	return render_template("metrics.html")


@app.route('/submit')
def submit():

	return render_template("submit.html")
