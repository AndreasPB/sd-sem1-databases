from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class BaseConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class Country(BaseConfig):
    _id: Optional[PyObjectId]
    name: str
    country_code: str = Field(..., max_length=2)

class Person(BaseConfig):
    _id: Optional[PyObjectId]
    name: str
    job: str
    country: Country


class Genre(BaseConfig):
    _id: Optional[PyObjectId]
    name: str


class Provider(BaseConfig):
    _id: Optional[PyObjectId]
    name: str
    url: str
    poster_path: str


class Media(BaseConfig):
    _id: Optional[PyObjectId]    
    name: str
    media_type: str
    people: Optional[list[Person]]
    genres: Optional[list[Genre]]
    providers: Optional[list[Provider]]


class User(BaseConfig):
    _id: Optional[PyObjectId]
    username: str
    email: str
    country: Country
    favorites: Optional[list[Media]]
