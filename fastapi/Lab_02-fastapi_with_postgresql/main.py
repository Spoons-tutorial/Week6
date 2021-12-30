from fastapi import FastAPI
from app.router import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Hello World"}