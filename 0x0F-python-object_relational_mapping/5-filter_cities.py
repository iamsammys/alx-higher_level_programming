#!/usr/bin/python3
"""
A script that takes in arguments and displays all values
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    un = argv[1]
    pw = argv[2]
    dbn = argv[3]
    search = argv[4]

    mydb = MySQLdb.connect(host="localhost", user=un,
                           port=3306, db=dbn, passwd=pw)
    cur = mydb.cursor()
    no_rows = cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                          ON cities.state_id = states.id\
                          WHERE states.name = '{:s}'".format(search))
    rows = cur.fetchall()
    i = 1
    for row in rows:
        print(row[0], end="")
        if i < no_rows:
            print(end=", ")
        i += 1
    print()
    cur.close()
    mydb.close()
