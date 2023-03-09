import sqlite3

# connect to database

# temp_db = sqlite3.connect(':memory:')
# this is a temporary database once the program is terminating it will be deleted

perm_dp = sqlite3.connect('program_db.db')
# this is a permanent database even that the program is terminating it will not be deleted

# create a cursor

cursor = perm_dp.cursor()

# create table

# cursor.execute("""CREATE TABLE customer (
#                    first_name text,
#                    last_name text,
#                    email text)
#                   """)

# data types:
# NULL
# INTEGER
# REAL
# BLOB [files with different extensions]

# Insert data into table

cursor.execute("""INSERT INTO customer VALUES
                  ('Ahmed', 'Hussein', 'ahmed.gmail.com'),
                  ('Hazem', 'Tarek', 'hazem@yahoo.com'),
                  ('Hhmed', 'Rushy', 'rushdy.hotmail.com')
                  """)

# Retrieve values from table

cursor.execute("""SELECT * FROM customer""")

print(cursor.fetchone())  # to get on row only
print(cursor.fetchmany(2))  # to get the number of rows you specify
print(cursor.fetchall())  # to get all rows in tables

# Format the results

cursor.execute("""SELECT * FROM customer""")
items = cursor.fetchall()  # list of tuples
print('First Name\t\tLast Name\t\tEmail')
print('-' * 50)
for item in items:
    print('{}\t\t\t{}\t\t\t{}'.format(item[0], item[1], item[2]))


cursor.execute("""SELECT rowid, * FROM customer""")  # to show row number in printing statement
print(cursor.fetchall())

# Where clause

cursor.execute("""SELECT rowid, * from customer WHERE last_name = 'Rushy'""")
print(cursor.fetchall())

cursor.execute("""SELECT rowid, * FROM customer WHERE email LIKE '%yahoo%' """)
print(cursor.fetchall())

cursor.execute("""SELECT rowid, * FROM customer WHERE first_name LIKE '__m%'""")
print(cursor.fetchall())

# Update records

cursor.execute("""UPDATE customer SET last_name = 'Rushdy' WHERE last_name = 'Rushy'""")
cursor.execute("""UPDATE customer SET first_name = 'Ahmed' WHERE last_name = 'Rushdy'""")
cursor.execute("""SELECT rowid, * FROM customer""")
print(cursor.fetchall())

# Delete record from table

cursor.execute("""DELETE FROM customer WHERE rowid = 3 """)
cursor.execute("""SELECT * FROM customer""")
print(cursor.fetchall())

# Order results by

cursor.execute("""SELECT rowid, * FROM customer ORDER BY rowid ASC""")  # ASCending by default even you don't write it
cursor.execute("""SELECT rowid, * FROM customer ORDER BY rowid DESC""")  # DESCinding order
print(cursor.fetchall())

# And \ Or

cursor.execute("""SELECT rowid, * FROM customer WHERE first_name = 'Ahmed' AND last_name = 'Hussein'""")
cursor.execute("""SELECT rowid, * FROM customer WHERE first_name = 'Ahmed' OR last_name = 'Tarek'""")
print(cursor.fetchall())

# Limiting results

cursor.execute("""SELECT rowid, * FROM customer LIMIT 1""")
print(cursor.fetchall())

# Drop table

cursor.execute("""DROP TABLE customer""")

# commit our command

perm_dp.commit()

# close the connection [it will be closed by default but to apply the best practice write this statement]
perm_dp.close()



