#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, db=sys.argv[3], passwd=sys.argv[2])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    row_query = cur.fetchall()
    for rows in row_query:
        print(rows)
    cur.close()
    db.close()
