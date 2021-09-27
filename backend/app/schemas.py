import enum
from typing import Optional
from pydantic import BaseModel, validator
from sqlalchemy.orm import Query


class OrmBase(BaseModel):
    # Common properties across orm models
    id: int

    # Pre-processing validator that evaluates lazy relationships before any other validation
    # NOTE: If high throughput/performance is a concern, you can/should probably apply
    #       this validator in a more targeted fashion instead of a wildcard in a base class.
    #       This approach is by no means slow, but adds a minor amount of overhead for every field
    @validator("*", pre=True)
    def evaluate_lazy_columns(cls, v):
        if isinstance(v, Query):
            return v.all()
        return v

    class Config:
        orm_mode = True


### Enums ###
# class MediaType(str, enum.Enum):
#     TV = "tv"
#     MOVIE = "movie"


# class Job(str, enum.Enum):
#     ACTOR = "actor"
#     DIRECTOR = "director"
#     RUNNER = "runner"
#     CAMERA_MAN = "camera man"


class Person(OrmBase):
    id: int
    name: str
    job: str


class User(OrmBase):
    id: int
    username: str
    email: str
    media: Optional[str]


class Country(OrmBase):
    id: int
    name: str
    country_code: str


class Genre(OrmBase):
    id: int
    name: str


class Provider(OrmBase):
    id: int
    name: str
    poster_path: str


class Media(OrmBase):
    id: int
    name: str
    media_type: str
    person: Person
    provider: Provider
