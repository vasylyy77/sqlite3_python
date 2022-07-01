import sqlite3



with sqlite3.connect('users.db') as db:
    cur = db.cursor()

    users = cur.execute("""SELECT * FROM users""").fetchall()
    print(users)
