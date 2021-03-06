from sqlalchemy import String, Integer, Enum, Table
from sqlalchemy.sql.schema import Column, ForeignKey
from app.db.database import Base, engine
from sqlalchemy.orm import joinedload, relationship
from sqlalchemy_utils import create_view
from sqlalchemy import select, func
from sqlalchemy.orm import Session


### Enums ###
# class MediaType(str, enum.Enum):
#     TV = "tv"
#     MOVIE = "movie"


# class Job(str, enum.Enum):
#     ACTOR = "actor"
#     DIRECTOR = "director"
#     RUNNER = "runner"
#     CAMERA_MAN = "camera man"


### Association table models ###
person_media_association_table = Table(
    "person_media",
    Base.metadata,
    Column("person_id", ForeignKey("person.id")),
    Column("media_id", ForeignKey("media.id")),
)

user_media_association_table = Table(
    "user_media",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("media_id", ForeignKey("media.id")),
)

genre_media_association_table = Table(
    "genre_media",
    Base.metadata,
    Column("genre_id", ForeignKey("genre.id")),
    Column("media_id", ForeignKey("media.id")),
)

provider_media_association_table = Table(
    "provider_media",
    Base.metadata,
    Column("provider_id", ForeignKey("provider.id")),
    Column("media_id", ForeignKey("media.id")),
)


### Main models ###
class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    media_type = Column(String(25))
    person = relationship("Person", secondary=person_media_association_table)
    provider = relationship("Provider", secondary=provider_media_association_table)
    genre = relationship("Genre", secondary=genre_media_association_table)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(15))
    email = Column(String(50))
    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="users")
    media = relationship("Media", secondary=user_media_association_table)


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    job = Column(String(25))
    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="people")
    media = relationship("Media", secondary=person_media_association_table)


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    media = relationship("Media", secondary=genre_media_association_table)


class Provider(Base):
    __tablename__ = "provider"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    poster_path = Column(String(50))
    media = relationship("Media", secondary=provider_media_association_table)


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country_code = Column(String(2))
    people = relationship("Person", back_populates="country")
    users = relationship("User", back_populates="country")


def get_users(db: Session, limit: int = 250):
    query = (
        select(User)
        .options(joinedload(User.country), joinedload(User.media))
        .order_by(User.username.desc())
        .limit(limit)
    )

    result = db.execute(query).unique()
    return result.scalars()


# ### Views ###
# stmt = (
#     select(
#         [
#             User.id.label("user_id"),
#             User.username,
#             Media.id.label("media_id"),
#             Media.name,
#         ]
#     )
#     .select_from(
#         User.__table__.join(
#             user_media_association_table, User.id == user_media_association_table.c.user_id
#         )
#     )
#     .select_from(
#         User.__table__.join(Media, Media.id == user_media_association_table.c.user_id)
#     )
# )
# 
# view = create_view("user_media_view", stmt, Base.metadata)
# 
# 
# class UserMediaView(Base):
#     __table__ = view
