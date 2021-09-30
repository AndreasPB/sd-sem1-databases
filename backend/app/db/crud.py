from typing import List
from sqlalchemy.orm import Session
import db.models as models
import schemas


### Person ###
def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.Person):
    """Adds a Person-type to the database"""
    db_person = models.Person(id=person.id, name=person.name, job=person.job)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


### User ###
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    """Adds a user-type to the database"""
    db_user = models.User(id=user.id, username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


### Country ###
def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


def create_country(db: Session, country: schemas.Country):
    """Adds a country-type to the database"""
    db_country = models.Country(
        id=country.id, name=country.name, country_code=country.country_code
    )
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


### Genre ###
def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()


def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Genre).offset(skip).limit(limit).all()


def create_genre(db: Session, genre: schemas.Genre):
    """Adds a genre-type to the database"""
    db_genre = models.Genre(id=genre.id, name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


### Provider ###
def get_provider(db: Session, provider_id: int):
    return db.query(models.Provider).filter(models.Provider.id == provider_id).first()


def get_providers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Provider).offset(skip).limit(limit).all()


def create_provider(db: Session, provider: schemas.Provider):
    """Adds a provider-type to the database"""
    db_provider = models.Provider(
        id=provider.id, name=provider.name, poster_path=provider.poster_path
    )
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider


### Media ###
def get_media(db: Session, media_id: int) -> models.Media:
    return db.query(models.Media).filter(models.Media.id == media_id).first()


def get_medias(db: Session, skip: int = 0, limit: int = 100) -> List[models.Media]:
    return db.query(models.Media).offset(skip).limit(limit).all()


def create_media(db: Session, media: schemas.Media) -> models.Media:
    """Adds a media-type to the database"""
    db_media = models.Media(id=media.id, name=media.name, media_type=media.media_type)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media
