import uvicorn
from fastapi import *

from api.api_v1 import bsm_api

app = FastAPI()
prefix = "/api/v1/algos"

@app.get("/health")
def health_check():
    return {"status": "up"}

app.include_router(bsm_api.router, prefix=prefix)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=9000)