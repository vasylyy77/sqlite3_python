import sqlite3

name = input("name: ")
login = input("login:")
password = input("password:")
cash = input("cash:")
age = input("age:")

with sqlite3.connect('users.db') as db:
    cur = db.cursor()

    cur.execute("""INSERT INTO users VALUES ( NULL,?,?,?,?,?)""", ( name, login, password, cash, age))
