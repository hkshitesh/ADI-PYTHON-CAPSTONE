import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('create table student (name text, addr text, city text, pin text)')
print("Table ctreate successfuly")

conn.close()