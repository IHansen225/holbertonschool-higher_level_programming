#!/usr/bin/python3
"""
    First approach to ORM
    Script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb as sql

"""
    Execution function
"""
def queryExec():
    """
        Creates a connection to the database and executes a query
    """
    conn = sql.connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    conn.close()

queryExec()
