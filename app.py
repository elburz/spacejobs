from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "main page"


@app.route('/metrics')
def metrics():
	return "metrics"


@app.route('/submit')
def submit():
	return "submit here"
