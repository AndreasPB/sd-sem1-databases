from fastapi import APIRouter

router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("/")
def root():
    return {"data": "mani nais grapf data"}
