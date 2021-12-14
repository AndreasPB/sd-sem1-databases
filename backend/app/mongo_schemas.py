from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class BaseConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


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


class Person(BaseConfig):
    id: Optional[PyObjectId] = Field(alias='_id')    
    name: str
    job: str
    country_id: int


class User(BaseConfig):
    id: Optional[PyObjectId] = Field(alias='_id')    
    username: str
    email: str
    country_id: int


class Country(BaseConfig):
    id: Optional[PyObjectId] = Field(alias='_id')    
    name: str
    country_code: str = Field(..., max_length=2)


class Genre(BaseConfig):
    id: Optional[PyObjectId] = Field(alias='_id')    
    name: str


class Provider(BaseConfig):
    id: Optional[PyObjectId] = Field(alias='_id')    
    name: str
    poster_path: str


class Media(BaseConfig):
    id: Optional[PyObjectId] = Field(alias='_id')    
    name: str
    media_type: str
