from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']='root'
app.config['MySQL_DB']='bdflask'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('login.html')
