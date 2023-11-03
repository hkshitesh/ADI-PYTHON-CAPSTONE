from flask import Flask, redirect, url_for, request, render_template
import sqlite3 as sql
app =Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    name = request.form['nm']
    addr = request.form['add']
    city = request.form['city']
    pin = request.form['pin']

    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("insert into student values(?,?,?,?)",(name,addr,city,pin))
        con.commit()
        msg = "Record Inserted Successfully"

    return render_template('result.html',msg = msg)

@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur =con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template('list.html', rows= rows)


if __name__ == '__main__':
    app.run()






