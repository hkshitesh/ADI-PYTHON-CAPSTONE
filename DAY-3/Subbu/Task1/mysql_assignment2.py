import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    password = "pwd4MySQL!",
    database = 'university'
)

mycursor = mydb.cursor()

mycursor.execute("drop database university")
mycursor.execute("Create database university")
mycursor.execute("show databases")
for db in mycursor:
    print(db)

# Create a table and insert data
mycursor.execute("CREATE TABLE university (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INTEGER, gender VARCHAR(255), major VARCHAR(255) )")

sql = "INSERT INTO university (id, name, age, gender, major) VALUES (%s, %s, %s, %s, %s)"
val = (1, "Rohit", 21, "Male", "BTech")
mycursor.execute(sql, val)

sql = "INSERT INTO university (id,  name, age, gender, major) VALUES (%s, %s, %s, %s, %s)"
val = (2, "Raju", 26, "Male", "MTech")
mycursor.execute(sql, val)

sql = "INSERT INTO university (id, name, age, gender, major) VALUES (%s, %s, %s, %s, %s)"
val = (3, "Minny", 25, "Female", "MBA")
mycursor.execute(sql, val)

sql = "INSERT INTO university (id, name, age, gender, major) VALUES (%s, %s, %s, %s, %s)"
val = (4, "Sam", 24, "male", "CA")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

# 2. Retrieve all entries
mycursor.execute("SELECT * FROM university")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# 3. Retrieve entry by id
mycursor.execute("SELECT * FROM university where id =3")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# 4. Update student info in the table
sql = "UPDATE university SET major = 'PhD' WHERE id =3"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# 5. Delete student info from the table
sql = "DELETE FROM university WHERE id = 4"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Close the connection
mydb.close()






