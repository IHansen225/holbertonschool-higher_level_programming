#!/usr/bin/python3
"""
    First approach to ORM
    Script that lists all states from the database hbtn_0e_0_usa
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
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM states ORDER BY id ASC")
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
            for j in st.punctuation:
                i = i.replace(j, "")
        return nargv


if __name__ == '__main__':
    query = QueryExec(sys.argv)
