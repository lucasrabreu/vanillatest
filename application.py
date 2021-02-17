from flask import Flask

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return "Hello world"

@app.route('/msg/<msg>')
def msg(msg):
    return "Hello world " + str(msg)
