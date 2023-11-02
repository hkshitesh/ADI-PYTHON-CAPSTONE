import csv

with open('employee.csv','r') as file:
    csv_reader= csv.DictReader(file)
    for row in csv_reader:
        print(row['Id'], row['Name'], row ['Age'])

data = [
    {'rno': '1', 'Name':'Kapil', 'per': '80'},
    {'rno': '2', 'Name':'Sachin', 'per': '90'},
    {'rno': '3', 'Name':'Dhoni', 'per': '95'},
    {'rno': '4', 'Name':'Rohit', 'per': '85'},
    ]

fields = ['rno','Name','per']

with open('student.csv', mode ='w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("data written successfully")