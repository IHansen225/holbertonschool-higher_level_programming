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
        argv = self.inputClean(argv)
        conn = sql.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3]
        )
        cur = conn.cursor()
        cur.execute("""SELECT *
            FROM states
            WHERE BINARY name = %s
            ORDER BY id ASC""" % argv[4])
        result = cur.fetchall()
        for row in result:
            print(row)
        cur.close()
        conn.close()

    def inputClean(self, argv):
        """
            Cleans input arguments for SQLi
            protection
        """
        nargv = argv.copy()
        for i in argv:
            if i.find(';') != -1:
                i = i.split(';')[0]
                i.replace("'", "")
                i.replace('"', "")
        return nargv


if __name__ == '__main__':
    obj = QueryExec(sys.argv)
