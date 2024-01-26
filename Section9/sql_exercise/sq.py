"""
6. sqlite insert multiple data rows
"""
import sqlite3

connection = sqlite3.connect("MyUsers.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS newUsers (idnum INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, fullname TEXT)")


# insert multiple rows of data 
data = [
    ('gcostanza', 'b0sc0', 'George Costanza'),
    ('newman', 'USMAIL', 'Newman')
]
cursor.executemany("INSERT INTO newUsers (username, password, fullname) VALUES (?,?,?)", data)
connection.commit()

print(cursor.execute("SELECT * FROM newUsers").fetchall())
#connection.close()
