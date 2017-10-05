'''
Author: Craig Einstein
File: app.py
Description: A simple web application that connects to the sakila database
'''
#import the modules
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

#define an app object
app = Flask(__name__)

#define a MySQL database
db = MySQL()

#configure the database settings
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'heresthedata!' #CHANGE TO YOUR PASSWORD
app.config['MYSQL_DATABASE_DB'] = 'sakila'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
db.init_app(app)

#create a connection to the database
conn = db.connect()

#create a cursor to retrieve the data
cursor = conn.cursor()

#define a query
query = 'Select title from film where film_id < 5;'

#execute the query
cursor.execute(query)

#retrieve the data (this is one of several ways to accomplisht this)
data = []
for item in cursor:
    data.append(item)

#close the cursor and the connection
cursor.close()
conn.close()

#print the data to the terminal
print data

#main page of website
@app.route('/')
def index():
    #display the index.html file contained within the templates directory on the webpage
    return render_template('index.html', data=data, query=query)

#define a second page
@app.route('/hello/')
def hello():
    #print hello to the page
    return "Hello!"

