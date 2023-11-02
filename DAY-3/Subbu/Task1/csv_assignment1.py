import csv
with open('input.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['ID'],row ['Name'], row['Salary'] )

data = [
    {'Name': 'John Doe', 'Age': '30', 'City': 'New York'},
    {'Name': 'Jane Smith', 'Age': '25', 'City': 'San Francisco'},
    {'Name': 'Bob Johnson', 'Age': '35', 'City': 'Chicago'}
]

fields = ['Name', 'Age', 'City']

with open('output.csv', mode = 'w',  newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("Data Written Successfully")