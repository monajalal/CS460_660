import mysql.connector

db = mysql.connector.connect(user='root', host='127.0.0.1', password='123456', database='sakila')
cursor = db.cursor()

query = ('select film_id, title from film where film_id > 200;')

cursor.execute(query)

for info in cursor:
	print( info)

cursor.close()
db.close()
