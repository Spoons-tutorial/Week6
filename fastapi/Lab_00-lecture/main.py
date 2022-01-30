from fastapi import FastAPI
from app.router import predict

app = FastAPI()

app.include_router(predict.router)