from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas import Provider
from app.db.database import get_db
from app.db.crud import create_provider, get_provider, get_providers


router = APIRouter(prefix="/provider", tags=["provider"])


@router.get("/{provider_id}", response_model=Provider)
async def read_provider(provider_id: int, db: Session = Depends(get_db)):
    db_provider = get_provider(db=db, provider_id=provider_id)
    if db_provider:
        return db_provider
    raise HTTPException(status_code=404, detail="Provider doesn't exist")


@router.get("/", response_model=list[Provider])
async def read_providers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_providers(db=db, skip=skip, limit=limit)


@router.post("/", response_model=Provider)
async def post_provider(provider: Provider, db: Session = Depends(get_db)):
    """Creates a provider to the database"""
    db_provider = get_provider(db=db, provider_id=provider.id)
    if db_provider:
        raise HTTPException(status_code=400, detail="Provider already exists")
    return create_provider(db=db, provider=provider)
