import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['myadidb']
mycol = mydb['students']
mydict = {"name": "John Doe", "age": "20", "major": "Computer Science"},
id = mycol.insert_many(mydict)

print(id.inserted_ids)
print(mydb.list_collection_names())

mylist = [
  {"name": "Jane Smith", "age": "21", "major": "Engineering"},
  {"name": "Bob Johnson", "age": "19", "major": "Mathematics"}
]

ids = mycol.insert_many(mylist)
print(ids.inserted_ids)