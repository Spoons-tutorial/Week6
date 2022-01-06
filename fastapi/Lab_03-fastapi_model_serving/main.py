from fastapi import FastAPI
from app.router import users, iris

app = FastAPI()

app.include_router(users.router)
app.include_router(iris.router)

@app.get("/")
def root():
    return {"message": "Hello World"}