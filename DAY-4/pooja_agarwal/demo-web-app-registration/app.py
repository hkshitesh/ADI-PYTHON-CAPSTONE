from flask import Flask, redirect, url_for, request, render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods = ['POST'])
def register():
    username = request.form['uname']
    password = request.form['pwd']
    gender = request.form['gen']
    department = request.form['dept']
    sql = "insert into users values (%s, %s, %s, %s)"
    val = (username, password, gender, department)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "<h1> user registered successfully </h1>"

if __name__ == '__main__':
    app.run()

