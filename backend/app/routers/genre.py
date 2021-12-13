from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas import Genre
from app.db.database import get_db
from app.db.crud import create_genre, get_genre, get_genres


router = APIRouter(prefix="/genre", tags=["genre"])


@router.get("/{genre_id}", response_model=Genre)
async def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = get_genre(db=db, genre_id=genre_id)
    if db_genre:
        return db_genre
    raise HTTPException(status_code=404, detail="Country doesn't exist")


@router.get("/", response_model=list[Genre])
async def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_genres(db=db, skip=skip, limit=limit)


@router.post("/", response_model=Genre)
async def post_genre(genre: Genre, db: Session = Depends(get_db)):
    """Creates a genre to the database"""
    db_genre = get_genre(db=db, genre_id=genre.id)
    if db_genre:
        raise HTTPException(status_code=400, detail="Genre already exists")
    return create_genre(db=db, genre=genre)
