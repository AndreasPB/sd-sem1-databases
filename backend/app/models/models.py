from sqlalchemy import String, Integer, Enum
from sqlalchemy.sql.schema import Column

# TODO: skal flyttes database.py eller noget
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/mandatory"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Error in {__name__}: {e}")
        db.close()


### Enums ###
class MediaType(str, Enum):
    TV = "tv"
    MOVIE = "movie"


class Job(str, Enum):
    ACTOR = "actor"
    DIRECTOR = "director"
    RUNNER = "runner"
    CAMERA_MAN = "camera man"


### Models ###
class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    media_type = Column(Enum(MediaType))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(15))
    email = Column(String(50))


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    job = Column(Enum(Job))


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))


class Provider(Base):
    __tablename__ = "provider"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    poster_path = Column(String(50))


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country_code = Column(String(2))
