import sqlite3



with sqlite3.connect('users.db') as db:
    cur = db.cursor()

    users = cur.execute("""DELETE FROM  users WHERE name == 'fedor'""").fetchall()
    print(users)
