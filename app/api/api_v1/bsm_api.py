from fastapi import APIRouter

router = APIRouter(
    prefix="/bsm",
    tags=["bsm"],
)

@router.get("/test")
def health_check():
    return {"status": "test"}