from app.mongo_schemas import Person
from pymongo import MongoClient

client = MongoClient('mongodb://root:rootpassword@mongo:27017/')
db = client['loldatabase']
lol_collection = db['lolcollection']

data = {"lol": 1}
data2 = [{"lol": 1}, {"lol": 2}, {"lol": 3}, {"lol": 4}, {"lol": 5}]

# lol_collection.insert_one(data).inserted_id

#lol_collection.insert_many(data2).inserted_ids

lol_collection.insert_one(Person(
    name = 'Jens',
    job = 'arbejdsløs',
    country_id = 1
).dict(by_alias=True))


print(lol_collection.find_one({"lol": 3}))
