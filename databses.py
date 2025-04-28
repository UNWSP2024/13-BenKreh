import sqlite3 as sl

connection = sl.connect("cities.db")
cursor = connection.cursor()

for row in cursor.execute("select * from cities"):
    print(row)