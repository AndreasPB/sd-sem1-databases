from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import Person
from db.database import get_db
from db.crud import create_person


router = APIRouter(prefix="/person", tags=["person"])


@router.get("/")
def root():
    return {"data": "mani nais ralationelz data"}


# @router.post("/", response_model=Media)
# async def post_media(media: Media, db: Session = Depends(get_db)):
#     """Creates a media to the database"""
#     db_media = get_media_by_id(db=db, media_id=media.id)
#     if db_media:
#         raise HTTPException(status_code=400, detail="Media already exists")
#     return create_media(db=db, media=media)


@router.post("/", response_model=Person)
async def post_person(person: Person, db: Session = Depends(get_db)):
    """Creates a person to the database"""
    return create_person(db=db, person=person)
