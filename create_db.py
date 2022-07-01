import sqlite3

db =  sqlite3.connect('users.db')
cur = db.cursor()

cur.execute("""CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR,
login VARCHAR,
password VARCHAR,
cash INTEGER,
age INTEGER
)""")
db.comit()
db.close()

