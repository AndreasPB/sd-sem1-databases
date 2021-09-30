# import enum
from pydantic import BaseModel, Field


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
    country_id: int


class User(BaseConfig):
    id: int
    username: str
    email: str
    country_id: int


class Country(BaseConfig):
    id: int
    name: str
    country_code: str = Field(..., max_length=2)


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
