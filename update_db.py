import sqlite3

x = 'nert'

with sqlite3.connect('users.db') as db:
    cur = db.cursor()

    users = cur.execute(f"""UPDATE users set name='fedor' WHERE name == 'nert'""").fetchall()

