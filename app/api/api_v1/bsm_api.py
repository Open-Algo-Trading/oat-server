from fastapi import APIRouter
from algos.bsm import bsm
from pydantic import BaseModel


router = APIRouter(
    prefix="/bsm",
    tags=["bsm"],
)


class BsmRequest(BaseModel):  #TODO: refactor into schemas directory
    stock_price: float
    strike_price: float
    rate: float
    time: float
    volatility: float
    dividend: float


class BsmResponse(BaseModel):  #TODO: refactor into schemas directory
    call: str
    put: str


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