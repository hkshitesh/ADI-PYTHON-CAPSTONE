import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['myadidb']
mycol = mydb["students"]

data = [
    {"name": "John Doe", "age": 20, "major": "Computer Science"},
    {"name": "Jane Smith", "age": 21, "major": "Engineering"},
    {"name": "Bob Johnson", "age": 19, "major": "Mathematics"}
]


ids = mycol.insert_many(data)

for row in mycol.find():
    print(row)
