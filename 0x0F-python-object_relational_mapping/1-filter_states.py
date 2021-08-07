#!/usr/bin/python3

"""Show the table states from indicated database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    serv = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    c = serv.cursor()
    c.execute("SELECT * FROM states")
    l = c.fetchall()
    for i in l:
        le = len(i[1]) - 1
        state = i[1]
        if state[0:-le] == 'N':
            print (i)