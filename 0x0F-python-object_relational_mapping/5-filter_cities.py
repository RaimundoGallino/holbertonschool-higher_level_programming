#!/usr/bin/python3

"""Show the table states from indicated database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    serv = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    c = serv.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %(name)s
                    ORDER BY cities.id""", {'name': argv[4]})
    cl = c.fetchall()
    le = len(cl) - 1
    if le == - 1:
        print()
    else:
        for i in range(le):
            print("{}, ".format(cl[i][1]), end="")
        if cl[le][1]:
            print("{}".format(cl[le][1]))
        else:
            print()

    serv.close()
