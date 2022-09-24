# import sqlite3
# # creates a databse if not existed otherwise modify it
# conn = sqlite3.connect('lunch.db')
# c = conn.cursor()  # use to access the database edit and stuff to database
# # c.execute('''create table meals(sandw text, fruit text, tablenum int)''')  # creates a table and make columns protip is run it only once then comment cuz it will give error of already exists
# sandwitch = "pasta"
# fruit = "mango"
# tablenum = 7

# # c.execute('''insert into meals values(?,?,?)''', (sandwitch, fruit,
# #           tablenum))  # insert values inside a table columns we specified
# # conn.commit()  # commits everything to the table actually inserts into table

# # c.execute('''drop table meals''')  # will delete the whole table of meals

# c.execute('''select * from meals''')
# # c.execute('''select fruit from meals''')
# output = c.fetchall()
# print(output)


# copied from john watson rooby

import sqlite3

conn = sqlite3.connect('dinner.db')
c = conn.cursor()

# delete table
#c.execute('''DROP TABLE meal''')

# create a table
c.execute('''CREATE TABLE meal(sandwich TEXT, fruit TEXT, tablenumber INT)''')

# data to insert
sandwich = 'chicken'
fruit = 'orange'
tablenum = 22

# insert and commit to database
c.execute('''INSERT INTO meal VALUES(?,?,?)''', (sandwich, fruit, tablenum))
conn.commit()

# select all data from table and print
c.execute('''SELECT * FROM meal''')
results = c.fetchall()
print(results)

# close database connection
conn.close()
