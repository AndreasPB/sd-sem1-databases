from sqlalchemy.orm import Session
import models
import schemas


def create_person(db: Session, person: schemas.Person):
    """Adds a Person-type to the database"""
    db_person = models.Person(id=person.id, name=person.name, job=person.job)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
