import csv

with open('employee.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

hdr =     ['Name', 'Age', 'City']

data = [
    {'Name' : 'John Doe', 'Age' : '30', 'City' : 'New York'},
    {'Name' : 'Jane Smith', 'Age' : '25', 'City' : 'San Francisco'},
    {'Name' : 'Bob Johnson', 'Age' : '35', 'City' : 'Chicago'}
]

with open('output.csv', mode='w', newline='') as out_file:

    writer = csv.DictWriter(out_file, fieldnames=hdr)
    writer.writeheader()
    writer.writerows(data)


