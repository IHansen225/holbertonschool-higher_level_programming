#!/usr/bin/python3
"""
    First approach to ORM
    Script that lists and filters all states from the database hbtn_0e_0_usa
    Takes filter from user input safe from SQLinjection
"""
import sys
import string as st
import MySQLdb as sql


class QueryExec():
    """
        Creates a connection to the database
        and executes the query based on
        user input.
    """

    def __init__(self, argv):
        """
            Constructor/Init function
        """
        conn = sql.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3]
        )
        cur = conn.cursor()
        cur.execute("SELECT cities.name FROM cities JOIN states ON states.id\
            = cities.state_id WHERE states.name = %(stname)s\
            ORDER BY cities.id ASC", {'stname': argv[4]})
        result = cur.fetchall()
        rowCount = len(result)
        resString = ""
        for i in range(rowCount):
            resString += result[i][0]
            resString += ", " if i < rowCount else ""
        print(resString)
        cur.close()
        conn.close()


if __name__ == '__main__':
    obj = QueryExec(sys.argv)
