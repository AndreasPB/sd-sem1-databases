from fastapi import APIRouter

router = APIRouter(prefix="/relational", tags=["relational"])


@router.get("/")
def root():
    return {"data": "mani nais ralationelz data"}
