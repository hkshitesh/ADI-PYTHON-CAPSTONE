import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'Precision@1',
    database = 'mydatabase'
)

# print(mydb)

# newcursor = mydb.cursor()
# newcursor.execute("drop database mydatabase")
# newcursor.execute("Create database mydatabase")
#
# newcursor.execute("show database")

mycursor = mydb.cursor()
# Create a table and insert data
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John Doe", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Query the database
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Update data in the table
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Highway 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete data from the table
sql = "DELETE FROM customers WHERE address = 'Canyon 123'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
