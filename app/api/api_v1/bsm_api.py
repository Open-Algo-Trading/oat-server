from algos.bsm import bsm
from fastapi import APIRouter
from pydantic import BaseModel

class BsmRequest(BaseModel):
    stock_price: float
    strike_price: float
    rate: float
    time: float
    volatility: float
    dividend: float

class BsmResponse(BaseModel):
    call: str
    put: str

router = APIRouter(
    prefix="/bsm",
    tags=["bsm"],
)

@router.post("/calculate", response_model=BsmResponse)
async def calculate(request: BsmRequest):
    call, put = bsm(
        request.strike_price,
        request.strike_price,
        request.rate,
        request.time,
        request.volatility,
        request.dividend
    )

    return BsmResponse(call=call,put=put)