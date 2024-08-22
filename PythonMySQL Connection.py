import mysql.connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursorPrepared

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='crud_python',
                                       user='root',
                                       password='mysql')
        records_to_insert = [(2, 'Jon', '2018-01-11', 26),
                             (3, 'Jane', '2017-12-11', 27),
                             (4, 'Bill', '2018-03-23', 26)]
        sql_insert_query = """ INSERT INTO python_users (id, name, birth_date, age) 
                               VALUES (%s,%s,%s,%s) """
        cursor = conn.cursor(cursor_class=MySQLCursorPrepared)
        result = cursor.executemany(sql_insert_query, records_to_insert)
        conn.commit()
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

            print("MySQL connection is closed")
            if __name__ == '__main__':
                connect()

























# Creating a Database


#Create a Table
# id,name,email and age













