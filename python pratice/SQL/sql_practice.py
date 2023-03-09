import sqlite3 as sql
import pandas as pd

data = pd.read_csv("E:\\python codes\\python pratice\\t.csv")
db = sql.connect('simple_db.db')

cursor = db.cursor()

# Generally, in SQLite the AUTOINCREMENT is not necessary
# because the same functionality can be achieved by ROWID and it will
# impose extra CPU, memory, disk space and disk I/O overhead.

# cursor.execute("""CREATE TABLE Test (
#                   date DATE,
#                   value INTEGER)
#                   """)
#
# data.to_sql(name='Test', con=db, if_exists='append', index=False)
# db.commit()
# db.close()
cursor.execute("""SELECT * FROM Test""")
r = cursor.fetchall()
for i in r:
    print(i)
db.commit()
db.close()
# for i in data:
#     cursor.executemany("""INSERT INTO Test VALUES(?)""", i)
#
# cursor.execute("""SELECT * FROM Test""")
# records = cursor.fetchall()
#
# # because of the output will be a list of tuples we will cust the output as below
#
# print('-' * 100)
# for record in records:
#     print('{}\t\t\t{}'.format(record[0], record[1]))
#
# db.commit()
# db.close()
#
# # 1. Primary Key
# # Primary Key is a field that can be used to identify all the tuples uniquely in the database.
# # Only one of the columns can be declared as a primary key. A Primary Key can not have a NULL value.
#
# # 7. Foreign Key
# # A foreign key is a column which is known as Primary Key in the other table i.e.
# # A Primary Key in a table can be referred to as a Foreign Key in another table.
# # Foreign Key may have duplicate & NULL values if it is defined to accept NULL values.
#
# # 2. Unique Key
# # Unique Key can be a field or set of fields that can be used to uniquely identify the tuple from the database.
# # One or more fields can be declared as a unique Key. The unique Key column can also hold the NULL value.
# # Use of Unique Key improves the performance of data retrieval.
# # It makes searching for records from the database much more faster & efficient.
#
#
# # 3. Candidate Key
# # Candidate Key can be a column or group of columns that can qualify for the Unique Key.
# # Every table has at least one Candidate Key. A table may have one or more Candidate Key.
# # Each Candidate Key can work as a Primary Key if required in certain scenarios.
#
#
# #  4. Alternate Key
# # Alternate Key is that Key which can be used as a Primary Key if required.
# # Alternate Key also qualifies to be a Primary Key but for the time being, It is not the Primary Key.
#
#
# # 5. Composite Key
# # Composite Key is also known as Compound Key / Concatenated Key.
# # Composite Key refers to a group of two or more columns that can be used to identify a tuple from the table uniquely.
# # A group of the column in combination with each other can identify a row uniquely but a single column of that group
# # does not promise to identify the row uniquely.
#
#
# # 6. Super Key
# # Super Key is a combination of columns, each column of the table remains dependent on it.
# # Super Key may have some more columns in the group which may or may not be necessary to identify the tuple uniquely
# # from the table. Candidate Key is the subset of the Super Key. Candidate Key is also known as minimal Super Key.
