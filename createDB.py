import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to sqllite 
    run this first to create the db.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"D:\pytonProjects\tempfiles\db")