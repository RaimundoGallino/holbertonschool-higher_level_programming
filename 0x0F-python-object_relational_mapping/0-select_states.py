#!/usr/bin/python3
import MySQLdb

serv = MySQLdb.connect(host = "localhost", user = "root", passwd = "root")

c = serv.cursor()
c.execute("SHOW DATABASES")
l = c.fetchall()
print l
l = [ i[0] for i in l ]
print l
