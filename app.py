import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MAIN_SCRAPER_DB_URL']
db = SQLAlchemy(app)


class JobListing(db.Model):
	__tablename__ = 'scrapedresults'

	id = db.Column(db.Integer, primary_key=True)
	term = db.Column(db.Text)
	location = db.Column(db.Text)
	jobposition = db.Column(db.Text)
	department = db.Column(db.Text)
	agency = db.Column(db.Text)
	dateposted = db.Column(db.Text)
	link = db.Column(db.Text)

	def __init__(self, term, location, jobposition, department, agency, dateposted, link):
		self.term = term
		self.location = location
		self.jobposition = jobposition
		self.department = department
		self.agency = agency
		self.dateposted = dateposted
		self.link = link

	def __repr__(self):
		return self.jobposition


class EmailListing(db.Model):
	__tablename__ = 'emaillist'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Text)

	def __init__(self, email):
		self.email = email

	def __repr__(self):
		return self.email


@app.route('/', methods=['GET', 'POST'])
def main():

	# switch header if someone subscribes
	subscribe_bool = False
	# if subscribe button clicked
	if request.method == 'POST':
		if request.form['submit'] == 'email_subscribe':
			# grab info
			email_address = request.form['email_address']

			# add to database here
			emailAddition = EmailListing(email_address)
			db.session.add(emailAddition)
			db.session.commit()
			# swap message with bool
			subscribe_bool = True
			# today =
			# yesterday =
	return render_template("main.html", subscribe_bool=subscribe_bool, jobPostings=JobListing.query.order_by(JobListing.dateposted.desc()).limit(100))


@app.route('/about', methods=['GET', 'POST'])
def about():
	# switch header if someone subscribes
	subscribe_bool = False
	# if subscribe button clicked
	if request.method == 'POST':
		if request.form['submit'] == 'email_subscribe':
			# grab info
			email_address = request.form['email_address']

			# add to database here
			emailAddition = EmailListing(email_address)
			db.session.add(emailAddition)
			db.session.commit()
			# swap message with bool
			subscribe_bool = True

	return render_template("about.html", subscribe_bool=subscribe_bool)


@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
	# switch header if someone subscribes
	subscribe_bool = False
	# if subscribe button clicked
	if request.method == 'POST':
		if request.form['submit'] == 'email_subscribe':
			# grab info
			email_address = request.form['email_address']

			# add to database here
			emailAddition = EmailListing(email_address)
			db.session.add(emailAddition)
			db.session.commit()
			# swap message with bool
			subscribe_bool = True
	return render_template("metrics.html", subscribe_bool=subscribe_bool)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
	# switch header if someone subscribes
	subscribe_bool = False
	# if subscribe button clicked
	if request.method == 'POST':
		if request.form['submit'] == 'email_subscribe':
			# grab info
			email_address = request.form['email_address']

			# add to database here
			emailAddition = EmailListing(email_address)
			db.session.add(emailAddition)
			db.session.commit()
			# swap message with bool
			subscribe_bool = True
		elif request.form['submit'] == 'job_submit':
			term = request.form['term']
			location = request.form['location']
			jobposition = request.form['jobposition']
			department = request.form['department']
			agency = request.form['agency']
			dateposted = datetime.date.today()
			dateposted = dateposted.strftime('%m-%d-%Y')
			link = request.form['link']

			#might be better to email back to me for checking
			# add to database here
			jobAddition = JobListing(term, location, jobposition, department, agency, dateposted, link)
			db.session.add(jobAddition)
			db.session.commit()
			#flash message as well
			return redirect(url_for('main'))
	return render_template("submit.html", subscribe_bool=subscribe_bool)
