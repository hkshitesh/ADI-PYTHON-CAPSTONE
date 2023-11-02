import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    password = "Basith@1805",
    database = "University"
)

mycursor = mydb.cursor()
#mycursor.execute("Create database University")
#mycursor.execute("DROP TABLE Students")
mycursor.execute("CREATE TABLE Students (ID INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255),Age INT,Gender VARCHAR(255),Major VARCHAR(255))")
sql = "INSERT INTO Students (Name, Age, Gender, Major) VALUES (%s ,%s, %s ,%s)"
val = ("John", 21, "Male", "Computer Science")
mycursor.execute(sql,val)
mydb.commit()
val = ("Rosy", 22, "Female","Social")
mycursor.execute(sql,val)

mydb.commit()

mycursor.execute("select * from Students")
#
myresult = mycursor.fetchall()
#
for row in myresult:
    print("ID :", row[0],"Name: ",row[1], "Age: ",row[2], "Gender:",row[3],"Major:",row[4])
print(mycursor.rowcount, "retrieved.")

sql = "UPDATE Students SET Major = 'Physics' WHERE Major = 'Computer Science'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

sql = "DELETE FROM Students WHERE Gender = 'Female'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

mydb.close()