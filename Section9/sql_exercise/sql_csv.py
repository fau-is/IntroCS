import csv


# """
# 1. csv reader iterator, indice only via int 
# """ 
# print("************1************")

# with open('users.csv', 'r') as f:
#     reader = csv.reader(f)
#     # next(reader)

#     for row in reader:
#         print(row[0])

# print("************1************")


# """
# 2. csv DictReader, indice via column name
# """
# print("************2************")

# with open('users.csv', 'r') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(row['username'])

# print(row['username'] for row in reader)
# print("************2************")




# """
# 3. remove duplicates with set
# """
# print("************3************")

# usernames = set()
# with open('users.csv', 'r') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         usernames.add(row['username'])

# print(usernames)
# print(sorted(usernames))
# print("************3************")

# """
# 4. count frequency of entries with dict
# """
# print("************4************")

# usernames = {}
# with open('users.csv', 'r') as f:
#     reader = csv.DictReader(f)
    
#     for row in reader:
#         uname = row["username"].strip().lower()
#         if uname in usernames.keys():
#             usernames[uname] += 1
#         else: 
#             usernames[uname] = 1
#     print(usernames)
# print("************4************")



"""
5. sqlite in python
"""

""" import sqlite3

connection = sqlite3.connect("MyUsers.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (idnum INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, fullname TEXT)")
cursor.execute("INSERT OR REPLACE INTO users (idnum, username, password, fullname) VALUES (11, 'jerry', 'fus388', 'Jerry Seinfeld')")

print("First data insert from jerry", cursor.execute("SELECT * FROM users").fetchall())
connection.commit() # for insert
 """


"""
6. sqlite insert multiple data rows
"""
import sqlite3

connection = sqlite3.connect("MyUsers.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS newUsers (idnum, username TEXT, password TEXT, fullname TEXT)")


# insert multiple rows of data 
data = [
    ('gcostanza', 'b0sc0', 'George Costanza'),
    ('newman', 'USMAIL', 'Newman')
]
cursor.executemany("INSERT INTO newUsers (username, password, fullname) VALUES (?,?,?)", data)
connection.commit()
print(cursor.execute("SELECT * FROM newUsers").fetchall())