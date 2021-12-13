from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas import Media
from app.db.database import get_db
from app.db.crud import create_media, get_media, get_medias


router = APIRouter(prefix="/media", tags=["media"])


@router.get("/{media_id}", response_model=Media)
async def read_media(media_id: int, db: Session = Depends(get_db)):
    db_media = get_media(db=db, media_id=media_id)
    if db_media:
        return db_media
    raise HTTPException(status_code=404, detail="Media doesn't exist")


@router.get("/", response_model=list[Media])
async def read_medias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_medias(db=db, skip=skip, limit=limit)


@router.post("/", response_model=Media)
async def post_media(media: Media, db: Session = Depends(get_db)):
    """Creates a media to the database"""
    db_media = get_media(db=db, media_id=media.id)
    if db_media:
        raise HTTPException(status_code=400, detail="Media already exists")
    return create_media(db=db, media=media)
