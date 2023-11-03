import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Amma@passw0rd")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE university")
mydb.close()

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Amma@passw0rd", database="university"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, gender VARCHAR(10), major VARCHAR(30))"
)

mydb.close()

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Amma@passw0rd", database="university"
)

mycursor = mydb.cursor()

# Insert data to table
sql = "INSERT INTO students (name, age, gender, major) VALUES (%s, %s, %s, %s)"
val1 = ("Selva", 25, "Male", "Science")
val2 = ("Sagar", 21, "Male", "Computer")
val3 = ("Swaroop", 21, "Male", "Maths")
mycursor.execute(sql, val1)
mycursor.execute(sql, val2)
mycursor.execute(sql, val3)
mydb.commit()


def add():
    name = input("Name : ")
    age = int(input("Age : "))
    gender = input("Gender : ")
    major = input("Major : ")

    mycursor.execute(sql, (name, age, gender, major))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def get():
    id = int(input("ID : "))
    # Query the database
    mycursor.execute(f"SELECT * FROM students WHERE id = {id}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def update():
    name = input("Name : ")
    age = int(input("Age : "))
    gender = input("Gender : ")
    major = input("Major : ")
    # Update data in the table
    sql = f"UPDATE students SET name = {name} WHERE age = {age}"
    mycursor.execute(sql)
    sql = f"UPDATE students SET name = {name} WHERE gender = {gender}"
    mycursor.execute(sql)
    sql = f"UPDATE students SET name = {name} WHERE major = {major}"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


def delete():
    name = input("Name : ")
    # Delete data from the table
    sql = f'DELETE FROM students WHERE name = "{name}"'
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")


while True:
    print(
        """
0.	Add a new student.
1.	Retrieve student information by ID.
2.	Update student information.
3.	Delete a student record.
4.	Exit the program.

> 
"""
    )
    choice = int(input())

    if choice == 0:
        add()
    elif choice == 1:
        get()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    else:
        # Close the connection
        mydb.close()
        break
