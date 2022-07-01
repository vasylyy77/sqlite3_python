import sqlite3

db =  sqlite3.connect('cazino.db')
cur = db.cursor()

cur.execute("""CREATE TABLE cazino(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR,
cash INTEGER,

)""")
db.comit()
db.close()

