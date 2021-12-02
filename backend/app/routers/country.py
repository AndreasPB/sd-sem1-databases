from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas import Country
from app.db.database import get_db
from app.db.crud import create_country, get_country, get_countries


router = APIRouter(prefix="/country", tags=["country"])


@router.get("/{country_id}", response_model=Country)
async def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = get_country(db=db, country_id=country_id)
    if db_country:
        return db_country
    raise HTTPException(status_code=404, detail="Country doesn't exist")


@router.get("/", response_model=list[Country])
async def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_countries(db=db, skip=skip, limit=limit)


@router.post("/", response_model=Country)
async def post_country(country: Country, db: Session = Depends(get_db)):
    """Creates a country to the database"""
    return create_country(db=db, country=country)
