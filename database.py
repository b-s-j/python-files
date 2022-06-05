import sqlite3

connection = sqlite3.connect('customer.db')
#create a cursor 
c = connection.cursor()
# create a table
c.execute("SELECT * FROM customers")
#c.fetchone()
print(c.fetchone())
connection.commit()

#close our connection
connection.close()
