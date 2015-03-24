import datetime
import os

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.cache import Cache
from flask.ext.mail import Mail, Message
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.cache = Cache(app)
db = SQLAlchemy(app)
mail = Mail(app)
toolbar = DebugToolbarExtension(app)


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

    def __init__(
            self,
            term,
            location,
            jobposition,
            department,
            agency,
            dateposted,
            link):
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
@app.cache.cached(timeout=10800)  # DUMB DAT BI$H INTO CA$H FOR 180 MIN!
def main():
    # switch header if someone subscribes
    # subscribe_bool = False
    # if subscribe button clicked
    '''
    if request.method == 'POST':
        if request.form['submit'] == 'Subscribe':
            # grab info
            # email_address = request.form['email_address']

            # add to database here
            #emailAddition = EmailListing(email_address)
            #db.session.add(emailAddition)
            #db.session.commit()
            # swap message with bool
            #subscribe_bool = True
            continue
        elif request.form['submit'] == 'search_submit':
            search_by = request.form['searchby']
            #search_term = request.form['term']
            #search_term = '%' + search_term + '%'
            # add % to search term

            if search_by == 'Term':
                testList = JobListing.query.fitler(JobListing.department.like('blue')).order_by(JobListing.dateposted.desc()).limit(100)
            elif search_by == 'Department':
                testList = JobListing.query.fitler_by(JobListing.department.like(search_term)).order_by(JobListing.dateposted.desc()).limit(250)
            elif search_by == 'Location':
                testList = JobListing.query.fitler_by(JobListing.department.like(search_term)).order_by(JobListing.dateposted.desc()).limit(250)
            elif search_by == 'Agency':
                testList = JobListing.query.fitler_by(JobListing.department.like(search_term)).order_by(JobListing.dateposted.desc()).limit(250)
            elif search_by == 'Job Position':
                testList = JobListing.query.fitler_by(JobListing.department.like(search_term)).order_by(JobListing.dateposted.desc()).limit(250)

            return('worked')

            # return(search_query)
            '''
    return render_template(
        "main.html",
        jobPostings=JobListing.query.order_by(
            JobListing.dateposted.desc()).limit(1000))


@app.route('/about', methods=['GET', 'POST'])
def about():
    # switch header if someone subscribes
    # subscribe_bool = False
    # if subscribe button clicked
    '''
    if request.method == 'POST':
        if request.form['submit'] == 'Subscribe':
            # grab info
            # email_address = request.form['email_address']

            # add to database here
            #emailAddition = EmailListing(email_address)
            #db.session.add(emailAddition)
            #db.session.commit()
            # swap message with bool
            # subscribe_bool = True
            continue
    '''

    return render_template("about.html")


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # switch header if someone subscribes
    # subscribe_bool = False
    submit_bool = False

    # if subscribe button clicked
    if request.method == 'POST':
        if request.form['submit'] == 'job_submit':
            term = request.form['term']
            location = request.form['location']
            jobposition = request.form['jobposition']
            department = request.form['department']
            agency = request.form['agency']
            dateposted = datetime.date.today()
            dateposted = dateposted.strftime('%m-%d-%Y')
            link = request.form['link']

            submit_bool = True

            # might be better to email back to me for checking
            # add to database here
            # jobAddition = JobListing(term, location, jobposition, department, agency, dateposted, link)
            # db.session.add(jobAddition)
            # db.session.commit()

            # send job back to email for reference
            msg = Message(
                'Job posting attached',
                sender="spacejobs.us@gmail.com",
                recipients=["spacejobs.us@gmail.com"])
            msg.body = str(term) + '\n' + str(location) + '\n' + str(jobposition) + '\n' + \
                str(department) + '\n' + str(agency) + '\n' + str(dateposted) + '\n' + str(link)
            mail.send(msg)

            # flash message as well
            # return redirect(url_for('main'))

    return render_template("submit.html", submit_bool=submit_bool)


@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
    # switch header if someone subscribes
    # subscribe_bool = False
    # if subscribe button clicked
    '''
    if request.method == 'POST':
        if request.form['submit'] == 'Subscribe':
            # grab info
            # email_address = request.form['email_address']

            # add to database here
            # emailAddition = EmailListing(email_address)
            #db.session.add(emailAddition)
            #db.session.commit()
            # swap message with bool
            #subscribe_bool = True
            continue
    '''
    return render_template("metrics.html")
