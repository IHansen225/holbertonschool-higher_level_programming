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
        cur.execute("SELECT states.name, cities.name FROM\
            states JOIN cities ON states.id = cities.state_id\
            ORDER BY id ASC")
        result = cur.fetchall()
        cityCount = 1
        for row in result:
            print((cityCount,) + row)
            cityCount += 1
        cur.close()
        conn.close()


if __name__ == '__main__':
    obj = QueryExec(sys.argv)
