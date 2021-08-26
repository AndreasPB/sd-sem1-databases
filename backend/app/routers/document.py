from fastapi import APIRouter

router = APIRouter(prefix="/document", tags=["document"])


@router.get("/")
def root():
    return {"data": "mani nais dukumant data"}
