from builtins import input

import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin@123',
    database='university'
)

mycursor = mydb.cursor()

# Delete the database if already present
# mycursor.execute("drop database university")
# the below line should only be executed once
# mycursor.execute("Create database university")

# Create a table
# mycursor.execute("Create table student (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30), age INT, gender VARCHAR(10), major VARCHAR(50))")

display_str = """1.	Add a new student.\n\
2.	Retrieve student information by ID.\n\
3.	Update student information.\n\
4.	Delete a student record.\n\
5.	Exit the program.\n\
Enter Input: 
"""

while True:
    input_str = input(display_str)

    if input_str == '1':
        details = input("Give Details in format: Name Age Gender Major: ")
        (name, age, gender, major) = details.split(" ")
        sql = "INSERT INTO student (name, age, gender, major) VALUES (%s, %s, %s, %s)"
        val = details.split(" ")
        mycursor.execute(sql, val)
    elif input_str == '2':
        id = int(input("Give ID:"))
        mycursor.execute("SELECT * FROM student where id = %s", (id,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    elif input_str == '3':
        student_id = int(input("Enter student ID: "))
        attribute = input("Enter attribute to update (name/age/gender/major): ")
        new_value = input("Enter new value: ")
        sql = "UPDATE student SET " + attribute + " = %s WHERE id = %s"
        val = (new_value, student_id)
        mycursor.execute(sql, val)
    elif input_str == '4':
        student_id = int(input("Enter student ID: "))
        sql = "DELETE FROM student WHERE id = %s"
        val = (student_id,)
        mycursor.execute(sql, val)
    elif input_str == '5':
        mydb.close()
        break

    mydb.commit()