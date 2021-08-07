


# 0x0F. Python - Object-relational mapping


## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

```

With an ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()

```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Resources

**Read or watch**:

-   [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA "Object-relational mappers")
-   [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw "mysqlclient/MySQLdb documentation") (_please don’t pay attention to `_mysql`_)
-   [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/Xvw8zBoWPpVCoDYoS55Ksw "MySQLdb tutorial")
-   [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ "SQLAlchemy tutorial")
-   [SQLAlchemy](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA "SQLAlchemy")
-   [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/QFgtVxz2w-C1y1OB8uls1g "mysqlclient/MySQLdb")
-   [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg "Introduction to SQLAlchemy")
-   [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A "Flask SQLAlchemy")
-   [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw "10 common stumbling blocks for SQLAlchemy newbies")
-   [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw "Python SQLAlchemy Cheatsheet")
-   [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw "SQLAlchemy ORM Tutorial for Python Developers") (_**Warning:** This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL_)
-   [SQLAlchemy Tutorial](https://intranet.hbtn.io/rltoken/cmfi9C_nRXrmnwaJfCPyxA "SQLAlchemy Tutorial")

## Learning Objectives

-   How to connect to a MySQL database from a Python script
-   How to `SELECT` rows in a MySQL table from a Python script
-   How to `INSERT` rows in a MySQL table from a Python script
-   What ORM means
-   How to map a Python Class to a MySQL table
