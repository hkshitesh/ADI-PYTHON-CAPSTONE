import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ram&Jan@ki7",
    database='MySQL'
)

mycursor = mydb.cursor()

# Create a table and insert data
mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT,gender VARCHAR(255), major VARCHAR(255))")

# Adding a new student
sql = "INSERT INTO student (id, name, age, gender, major ) VALUES (%s, %s, %s, %s, %s)"
val = ("1", "Somali", " 25", "Female", "EMB")
mycursor.execute(sql, val)

sql = "INSERT INTO student (id, name, age, gender, major ) VALUES (%s, %s, %s, %s, %s)"
val = ("2", "Nidhi", " 22", "Female", "SCI")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Retrieve student information by id
mycursor.execute("select * from student where id=1")
myresult = mycursor.fetchall()
for row in myresult:
    print("ID:", row[0], "Name:", row[1], "Age:", row[2], "Gender:", row[3], "major:" ,row[4])

# Update data in the table
sql = "UPDATE student SET name = 'Kishor' WHERE  name= 'Somali'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete data from the table
sql = "DELETE FROM student WHERE name = 'Kishor'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Close the connection
mydb.close()


