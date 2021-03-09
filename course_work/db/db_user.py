import sqlite3 as lite

database = r'..\db\database.sqlite3'

sql = """CREATE TABLE IF NOT EXISTS users(
    userid INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE, 
    password TEXT);
"""

users_data = [
    (1, 'Bekzod', 'Fayzikulov', 'test123@gmail.com', 'testpassword'),
    (2, 'Shaw', 'Tschiersch', 'stschiersch1@webmd.com', 'XRGhjYaV'),
    (3, 'Lebbie', 'Bulpitt', 'lbulpitt2@intel.com', '3WGugG1Uxgd'),
    (4, 'Sander', 'Giller', 'sgiller3@businessweek.com', 'zhCVi3FE'),
    (5, 'Doria', 'Corben', 'dcorben4@miibeian.gov.cn', 'Jme6jtN'),
    (6, 'Valentino', 'Klassmann', 'vklassmann5@va.gov', 'MowL6CC7'),
    (7, 'Crystie', 'Thomassen', 'cthomassen6@google.com.au', 'cvP1h8'),
    (8, 'Michele', 'Fittall', 'mfittall7@usa.gov', 'fKJQVqPkVlkF'),
    (9, 'Dickie', 'Copes', 'dcopes8@seesaa.net', 'EAPotTJH'),
    (10, 'Wright', 'Faire', 'wfaire9@i2i.jp', 'kSXgKuSI0VDx'),
    (11, 'Lyn', 'Bras', 'lbrasa@jalbum.net', 'g45uvAwoK0e'),
    (12, 'Oren', 'Beverstock', 'obeverstockb@ed.gov', 'sNTo6NNPS'),
    (13, 'Guy', 'Jensen', 'gjensenc@tuttocitta.it', 'cLfs3r'),
    (14, 'Cacilie', 'Eckhard', 'ceckhardd@blogspot.com', 'ObAgXlp'),
    (15, 'Pavla', 'Loxley', 'ploxleye@live.com', 'FL2euggDW'),
    (16, 'Nichol', 'McAmish', 'nmcamishf@mysql.com', 'nBuaat7Xk'),
    (17, 'Les', 'Boatwright', 'lboatwrightg@booking.com', 'LQV7ErF'),
    (18, 'Karlan', 'Stegers', 'kstegersh@nyu.edu', 'XVgMKH'),
    (19, 'Becki', 'Atherley', 'batherleyi@amazon.de', 'CHqeuGhvm'),
    (20, 'Franz', 'Moore', 'fmoorej@wunderground.com', 'nJTnpI')
]


class DataBaseSQLite3:

    def __init__(self, db_name='database.sqlite3'):
        self._db_name = db_name
        self.connect_ = None

    def connect(self):
        self.connect_ = lite.connect(self._db_name)
        print('successful connection ...\n-------------------------')
        return self.connect_

    def cursor(self):
        if self.connect_:
            return self.connect_.cursor()
        else:
            print('Your need using connect method')

    def close(self):
        if self.connect_:
            self.connect_.close()
            print('-------------------------\nclosing the connection was successful')
        else:
            print('Your need using connect method')

    def commit(self):
        if self.connect_:
            self.connect_.commit()
        else:
            print('Your need using connect method')


def pk():
    db = DataBaseSQLite3(database)
    db.connect()
    cursor = db.cursor()
    cursor.execute(f'SELECT userid from users')
    users = cursor.fetchall()
    return int(users[-1][0]) + 1


def add_user_to_db(user_id, user_first_name, user_last_name, user_email, user_password):
    db = DataBaseSQLite3(database)
    db.connect()
    cursor = db.cursor()
    data = tuple([user_id, user_first_name, user_last_name, user_email, user_password])
    sql_ = """INSERT INTO users (userid, first_name, last_name, email, password) VALUES (?, ?, ?, ?, ?);"""
    cursor.execute(sql_, data)
    db.commit()
    db.close()


def drop_table(conn_cursor, table_name):
    sql_ = f'''DROP TABLE {table_name};'''
    conn_cursor.execute(sql_)


def user_auth(conn_cursor, email, password):
    conn_cursor.execute('SELECT userid FROM users WHERE email=? AND password=?', (email, password))
    user = conn_cursor.fetchall()
    print(user)


def email_is_valid(email_):
    if '@' not in email_:
        return False
    db = DataBaseSQLite3(database)
    db.connect()

    cursor = db.cursor()
    sql_ = """ SELECT userid FROM users WHERE email=? """
    cursor.execute(sql_, (email_,))
    user = cursor.fetchone()
    db.commit()
    db.close()
    if user:
        return True, user[0]
    return False


def password_id_valid(user_id, password):
    if password is None or len(password) < 8:
        return False
    db = DataBaseSQLite3(database)
    db.connect()
    cursor = db.cursor()
    sql_ = """ SELECT password FROM users WHERE userid=? """
    cursor.execute(sql_, (user_id,))
    user_password = cursor.fetchone()
    db.commit()
    db.close()
    if password == user_password[0]:
        return True
    return False


if __name__ == '__main__':
    ''''''
    # db = DataBaseSQLite3('database.sqlite3')
    # db.connect()
    # cursor = db.cursor()
    # cursor.execute(f'SELECT * from users')
    # users = cursor.fetchall()
    # for user in users:
    #     print(user)
    # db.commit()
    # db.close()
