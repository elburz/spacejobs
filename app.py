import datetime
import os

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.cache import Cache
from flask.ext.mail import Mail, Message
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.contrib.atom import AtomFeed


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


@app.route('/', methods=['GET'])
@app.cache.cached(timeout=10800)
def main():
    """
    Route for home page. Checks if old page ids like spacejobs.us/?page=6 exist
    and redirects back to the root of the domain with a 301.
    Caches DB query for 180 minutes.
    """
    old_url = request.args.get('page')
    if old_url:
        return redirect('/', 301)
    else:
        return render_template(
            "main.html",
            jobPostings=JobListing.query.order_by(
                JobListing.dateposted.desc()).limit(1000))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # this variable gets rid of form after submission
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

            # send job back to email for reference
            msg = Message(
                'Job posting attached',
                sender="spacejobs.us@gmail.com",
                recipients=["spacejobs.us@gmail.com"])
            msg.body = str(term) + '\n' + str(location) + '\n' + str(jobposition) + '\n' + \
                str(department) + '\n' + str(agency) + '\n' + str(dateposted) + '\n' + str(link)
            try:
                mail.send(msg)
            except:
                pass

            # set to true = swap out form for thank you message
            submit_bool = True

    return render_template("submit.html", submit_bool=submit_bool)

# coming soon to a theater near you
@app.route('/metrics', methods=['GET'])
def metrics():
    return render_template("metrics.html")


@app.route('/recent.atom')
def atom_feed():
    feed = AtomFeed('50 Newest Jobs This Week',
                    feed_url=request.url, url=request.url_root)
    jobs = JobListing.query.order_by(JobListing.dateposted.desc()).limit(50).all()
    for job in jobs:
        title = job.term + ' ' + job.jobposition + ' @ ' + job.agency
        content = 'Department: ' + job.department + '  ----   Location: ' + job.location
        date_obj = datetime.datetime.strptime(job.dateposted, '%m-%d-%Y')
        feed.add(title, content, content_type='html',author=job.agency,url=job.link,updated=date_obj)
    return feed.get_response()

