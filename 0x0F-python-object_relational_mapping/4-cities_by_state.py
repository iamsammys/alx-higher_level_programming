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
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cur.execute(query)
    row_query = cur.fetchall()
    for rows in row_query:
        print(rows)
    cur.close()
    db.close()
