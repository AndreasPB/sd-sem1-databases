# import enum
from typing import Optional
from pydantic import BaseModel, validator, Field
from pydantic.types import constr
from sqlalchemy.orm import Query
from sqlalchemy.util.langhelpers import monkeypatch_proxied_specials


### Enums ###
# class MediaType(str, enum.Enum):
#     TV = "tv"
#     MOVIE = "movie"


# class Job(str, enum.Enum):
#     ACTOR = "actor"
#     DIRECTOR = "director"
#     RUNNER = "runner"
#     CAMERA_MAN = "camera man"


class BaseConfig(BaseModel):
    class Config:
        orm_mode = True


class Person(BaseConfig):
    id: int
    name: str
    job: str
    # media: Optional[str]


class User(BaseConfig):
    id: int
    username: str
    email: str
    # media: Optional[str]


class Country(BaseConfig):
    id: int
    name: str
    # country_code: str = Field(..., max_length=2)


class Genre(BaseConfig):
    id: int
    name: str


class Provider(BaseConfig):
    id: int
    name: str
    poster_path: str


class Media(BaseConfig):
    id: int
    name: str
    media_type: str
    # person: Person
    # provider: Provider
