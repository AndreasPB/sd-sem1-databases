from pymongo import MongoClient

from app.db.mongo.mongo_test_data import list_of_media
from app.db.mongo.mongo_test_data import list_of_countries
from app.db.mongo.mongo_test_data import list_of_people
from app.db.mongo.mongo_test_data import list_of_genres
from app.db.mongo.mongo_test_data import list_of_providers
from app.db.mongo.mongo_test_data import list_of_users

DELETE_ST0FF = True

client = MongoClient("mongodb://root:rootpassword@mongo:27017/")
db = client["mandatory"]
media_collection = db["media"]
country_collection = db["country"]
person_collection = db["person"]
genre_collection = db["genre"]
provider_collection = db["provider"]
user_collection = db["user"]

if DELETE_ST0FF:
    media_collection.delete_many({})
    country_collection.delete_many({})
    person_collection.delete_many({})
    genre_collection.delete_many({})
    provider_collection.delete_many({})
    user_collection.delete_many({})

if not media_collection.count_documents({}, limit=1):
    media_collection.insert_many([media.dict() for media in list_of_media])

if not country_collection.count_documents({}, limit=1):
    country_collection.insert_many([country.dict() for country in list_of_countries])

if not person_collection.count_documents({}, limit=1):
    person_collection.insert_many([person.dict() for person in list_of_people])

if not genre_collection.count_documents({}, limit=1):
    genre_collection.insert_many([genre.dict() for genre in list_of_genres])

if not provider_collection.count_documents({}, limit=1):
    provider_collection.insert_many([provider.dict() for provider in list_of_providers])

if not user_collection.count_documents({}, limit=1):
    user_collection.insert_many([user.dict() for user in list_of_users])