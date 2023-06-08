#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           db=sys.argv[3], passwd=sys.argv[2])
    pointer = mydb.cursor()
    pointer.execute("SELECT * FROM states WHERE name LIKE BINARY\
                    'N%' ORDER BY states.id ASC")
    rows = pointer.fetchall()
    for row in rows:
        print(row)
    pointer.close()
    mydb.close()
