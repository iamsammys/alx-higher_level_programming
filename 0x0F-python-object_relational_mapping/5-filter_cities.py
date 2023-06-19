#!/usr/bin/python3
"""python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    userName = sys.argv[1]
    dataBase = sys.argv[3]
    paswd = sys.argv[2]
    db = MySQLdb.connect(host="localhost", user=userName,
                         port=3306, db=dataBase, passwd=paswd)
    cur = db.cursor()
    nameMatch = sys.argv[4]
    query = "SELECT cities.name\
            FROM cities\
            WHERE cities.state_id = (SELECT states.id\
            FROM states\
            WHERE states.name = %s)\
            ORDER BY cities.id ASC"
    numRows = cur.execute(query, (nameMatch,))
    row_query = cur.fetchall()
    i = 1
    for rows in row_query:
        if i == (numRows - 1):
            print(rows[0], end="")
            print()
        else:
            print("{}, ".format(rows[0]), end="")
        i += 1
    cur.close()
    db.close()
