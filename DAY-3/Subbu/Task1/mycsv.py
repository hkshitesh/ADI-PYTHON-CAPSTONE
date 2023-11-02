import csv
with open('employee.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['Id'],row ['Name'], row['Age'] )

data = [
    {'rno': '1', 'Name': 'Jack', 'Per': '70'},
    {'rno': '2', 'Name': 'John', 'Per': '90'},
    {'rno': '3', 'Name': 'Jill', 'Per': '83'},
    {'rno': '4', 'Name': 'Jim', 'Per': '78'}
]

fields = ['rno', 'Name', 'Per']

with open('student.csv', mode = 'w',  newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("Data Written Successfully")
