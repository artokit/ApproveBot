import sqlite3

connect = sqlite3.connect('db.sqlite')
cursor = connect.cursor()


def add_user(user_id):
    try:
        cursor.execute('INSERT INTO USERS VALUES(?)', (user_id, ))
        connect.commit()
    except sqlite3.IntegrityError:
        pass


def get_users():
    return cursor.execute('SELECT * FROM USERS').fetchall()
