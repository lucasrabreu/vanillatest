from flask import Flask
from sqlalchemy import create_engine
import pandas as pd
import os
pw = os.environ.get('DB_PW', '1234')
user = os.environ.get('DB_USER', 'admin')

eng = create_engine('mysql+pymysql://{}:{}@database-test-1.c5yisr2rt5nu.us-east-1.rds.amazonaws.com/db'.format(user,pw))

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return "Hello world"

@app.route('/msg/<msg>')
def msg(msg):
    return "Hello world " + str(msg)

@app.route('/insert/<user>/<age>')
def insert_data(user, age):
    df = pd.DataFrame({'user':[user], 'age':[age]})
    r = df.to_sql('user', if_exists='append', index=False, con=eng)
    return 'ok'

@app.route('/users')
def users():
    return pd.read_sql_query('select * from user', eng).to_html()