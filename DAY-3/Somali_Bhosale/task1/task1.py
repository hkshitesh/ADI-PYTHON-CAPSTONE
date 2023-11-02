import csv

with open('employee.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['ID'],row['Name'], row['Salary'])

data = [
        {'Name':'John Doe', 'Age':'30', 'City':'New York'},
        {'Name':'Jane Smith','Age': '25', 'City': 'San Francisco'},
        {'Name':'Bob Johnson', 'Age':'35', 'City' :'Chicago'},
]

fields = ['Name', 'Age', 'City']

with open('students.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print("Data written success")
