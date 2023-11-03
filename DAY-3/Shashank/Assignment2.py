import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    database = 'university'
)

mycursor = mydb.cursor()

# Create a table and insert data
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, gender VARCHAR(255), major VARCHAR(255))")
sql = "INSERT INTO students (name, age, gender, major) VALUES (%s, %s, %s, %s)"
val = ("Chetan", 23, 'Male', 'Major')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Query the database
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print("ID:",row[0], "Name:", row[1], "Age:", row[2], "Gender:", row[1], "Major:", row[2])

# Update data in the table
sql = "UPDATE students SET age = 22 WHERE age = 23"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete data from the table
sql = "DELETE FROM students WHERE name = 'Chetan'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Close the connection
mydb.close()