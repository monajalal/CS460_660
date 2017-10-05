'''
Author: Craig Einstein
File: search_app.py
Description: A simple web application that connects to the sakila database and implements a query execution feature
'''

from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

db = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hello' #CHANGE TO YOUR PASSWORD
app.config['MYSQL_DATABASE_DB'] = 'sakila'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
db.init_app(app)

#defines a function for extracting the data from a query
def extractData(query):
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall() #fetches all rows of the query
    cursor.close()
    conn.close()
    return data


#main page of website
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': #if method is get
        data = extractData("SELECT title FROM film WHERE film_id < 5;")
        return render_template('index_search.html')
    else: #if method is post
        query = request.form['QUERY'] #get information from the 'QUERY' row of the form
        try: #tries the query
            data = extractData(query)
            return render_template("index.html", data=data, query=query)
        except Exception as e:
            print(e)
            return render_template("index.html", query=query, error=e)
        

#search page
@app.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')




