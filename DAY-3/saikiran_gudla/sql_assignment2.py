import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    password = "@Infobee2001",
    database = 'myadidb'
)

#Create DB
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age Integer, gender VARCHAR(255), major VARCHAR(255))")

# Add
sql = "INSERT INTO students (name, age, gender, major) VALUES (%s, %s, %s, %s)"
val = ("Kiran", "22", "Male", "Economics")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Retrieve
mycursor.execute("select * from students where id=1")
myresult = mycursor.fetchall()
for row in myresult:
    print("ID: ", row[0], "name: ", row[1], "Age: ",row[2])

# Update data in the table
sql = "UPDATE students SET major = 'Computers' WHERE major = 'Economics'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete data from the table
sql = "DELETE FROM customers WHERE name = 'Kiran"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Close the connection
mydb.close()

