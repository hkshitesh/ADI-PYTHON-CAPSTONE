import pymongo

# Client url connection
myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Create db
mydb=myclient['myadidb']

# Collection like a table
mycol = mydb["students"]

data = [
    {"name": "John Doe", "age": 20, "major": "Computer Science"},
    {"name": "Jane Smith", "age": 21, "major": "Engineering"},
    {"name": "Bob Johnson", "age": 19, "major": "Mathematics"}
]

ids = mycol.insert_many(data)
print(ids.inserted_ids)