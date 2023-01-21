import mysql.connector

cnx = mysql.connector.connect(user='root', password='Tigrex171328!',
                              host='127.0.0.1',
                              database='grocery_store')
cnx.close()