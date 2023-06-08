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

    mydb = MySQLdb.connect(host="localhost", user=un,
                           port=3306, db=dbn)
    cur = mydb.cursor()
    no_rows = cur.execute("SELECT cities.id, cities.name, states.name\
                          FROM cities INNER JOIN states ON\
                          cities.state_id = states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mydb.close()
