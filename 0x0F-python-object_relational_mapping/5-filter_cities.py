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
                    WHERE states.name = %(name)s""", {'name': argv[4]})
    l = c.fetchall()
    le = len(l) - 1
    if le == 0:
        print()
    else:
        for i in range(le):
            print ("{}, ".format(l[i][1]), end="")
        print ("{}".format(l[le][1]))

    serv.close()
