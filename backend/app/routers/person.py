from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import Person
from app.db.database import get_db
from app.db.crud import create_person, get_person, get_people


router = APIRouter(prefix="/person", tags=["person"])


@router.get("/{person_id}", response_model=Person)
async def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = get_person(db=db, person_id=person_id)
    if db_person:
        return db_person
    raise HTTPException(status_code=404, detail="Person doesn't exist")


@router.get("/", response_model=list[Person])
async def read_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_people(db=db, skip=skip, limit=limit)


@router.post("/", response_model=Person)
async def post_person(person: Person, db: Session = Depends(get_db)):
    """Creates a person to the database"""
    db_person = get_person(db=db, person_id=person.id)
    if db_person:
        raise HTTPException(status_code=400, detail="Person already exists")
    return create_person(db=db, person=person)
