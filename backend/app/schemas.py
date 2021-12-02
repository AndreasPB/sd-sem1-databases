# import enum
import strawberry
from pydantic import BaseModel, Field
from strawberry.fastapi.router import GraphQLRouter


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


@strawberry.experimental.pydantic.type(model=Country, all_fields=True)
class CountryType:
    pass
    

@strawberry.experimental.pydantic.type(model=Person)
class PersonType:
    id: strawberry.auto
    name: strawberry.auto
    job: strawberry.auto
    country: CountryType


@strawberry.experimental.pydantic.type(model=User)
class UserType:
    id: strawberry.auto
    username: strawberry.auto
    email: strawberry.auto
    country: CountryType


@strawberry.experimental.pydantic.type(model=Genre, all_fields=True)
class GenreType:
    pass


@strawberry.experimental.pydantic.type(model=Provider, all_fields=True)
class ProviderType:
    pass


@strawberry.experimental.pydantic.type(model=Media, all_fields=True)
class MediaType:
    pass
