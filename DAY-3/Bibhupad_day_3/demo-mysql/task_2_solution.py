
import mysql.connector

# Connect to the MySQL database

mydb = mysql.connector.connect(

    host="localhost",

    user="user",

    password="Pass@1",

    database="university"

)

# Create a cursor to execute SQL queries

mycursor = mydb.cursor()


# Function to add a new student

def add_student():
    name = input("Enter student name: ")

    age = int(input("Enter student age: "))

    gender = input("Enter student gender: ")

    major = input("Enter student major: ")

    sql = "INSERT INTO students (name, age, gender, major) VALUES (%s, %s, %s, %s)"

    val = (name, age, gender, major)

    mycursor.execute(sql, val)

    mydb.commit()

    print("Student added successfully")


# Function to retrieve student information by ID

def retrieve_student():
    student_id = int(input("Enter student ID: "))

    mycursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))

    result = mycursor.fetchone()

    if result:

        print("ID: ", result[0])

        print("Name: ", result[1])

        print("Age: ", result[2])

        print("Gender: ", result[3])

        print("Major: ", result[4])

    else:

        print("Student not found")


# Function to update student information

def update_student():
    student_id = int(input("Enter student ID: "))

    attribute = input("Enter attribute to update (name/age/gender/major): ")

    new_value = input("Enter new value: ")

    sql = "UPDATE students SET " + attribute + " = %s WHERE id = %s"

    val = (new_value, student_id)

    mycursor.execute(sql, val)

    mydb.commit()

    print("Student information updated successfully")


# Function to delete a student record

def delete_student():
    student_id = int(input("Enter student ID: "))

    sql = "DELETE FROM students WHERE id = %s"

    val = (student_id,)

    mycursor.execute(sql, val)

    mydb.commit()

    print("Student record deleted successfully")


# Menu

while True:

    print("\n1. Add a new student")

    print("2. Retrieve student information by ID")

    print("3. Update student information")

    print("4. Delete a student record")

    print("5. Exit the program")

    choice = input("Enter your choice: ")

    if choice == '1':

        add_student()

    elif choice == '2':

        retrieve_student()

    elif choice == '3':

        update_student()

    elif choice == '4':

        delete_student()

    elif choice == '5':

        break

    else:

        print("Invalid choice. Please try again.")

# Close the database connection

mydb.close()
