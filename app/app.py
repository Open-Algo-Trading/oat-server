import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1 import bsm_api

app = FastAPI()
prefix = "/api/v1/algos"

origins = [
    "https://localhost:3000",
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "up"}

app.include_router(bsm_api.router, prefix=prefix)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000)