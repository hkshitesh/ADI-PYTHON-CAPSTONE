import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="Vishnu11@mysql",
    database = 'university'
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE students")
# Create a table and insert data
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, gender VARCHAR(255), major VARCHAR(255))")

while 1:

    menu = """
    1.	Add a new student.
    2.	Retrieve student information by ID.
    3.	Update student information.
    4.	Delete a student record.
    5.	Exit the program.
    """
    option = input("Select the action to perform from the menu \n "+menu)

    if option == '1':
        details = input("Enter id, name, age, gender, major to Add\n")
        details = details.split(" ")
        sql_data = "insert into students (id, name, age, gender, major) values (%s,%s,%s,%s,%s)"
        val = (int(details[0]), details[1], int(details[2]), details[3], details[4])

        mycursor.execute(sql_data, val)
        mydb.commit()

    elif option == '2':
        id = input("Enter student id to retrieve \n")
        mycursor.execute("SELECT * FROM students")
        myresult = mycursor.fetchall()
        for res in myresult:
            print(res)
            if res[0] == int(id):
                print(res)

    elif option == '3':
        id = input("Enter student id to update \n")
        # Update data in the table
        sql = f"UPDATE students SET name = 'Replacement' WHERE id = {id}"
        mycursor.execute(sql)
        mydb.commit()

    elif option == '4':
        id = input("Enter student id to delete \n")

        # Delete data from the table
        sql = f"DELETE FROM students WHERE id = {id}"
        mycursor.execute(sql)
        mydb.commit()

    elif option == 5:
        exit(0)
