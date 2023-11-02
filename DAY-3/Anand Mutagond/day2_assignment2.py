import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="304ec07002",
    database = 'university'
)

# Create the Database
mycursor = mydb.cursor()
# mycursor.execute("Create database university")

# Create a table and insert data
# mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age Integer, "
#                  "gender VARCHAR(255), major VARCHAR(255))")
sql = "INSERT INTO students (name, age, gender, major) VALUES (%s, %s, %s, %s)"
val = ("Anand Mutagond", "32", "Male", "Yes")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Update data in the table
sql = "UPDATE students SET name = 'Anand Mutagond ADI' WHERE name = 'Anand Mutagond'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete data from the table
sql = "DELETE FROM students WHERE name = 'Anand Mutagond ADI'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Close the connection
mydb.close()