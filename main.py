from fastapi import FastAPI

from database import Base, engine
from bike_models import Bike
from auth_model import User

from bike_router import router as bike_router
from auth_router import router as auth_router


app = FastAPI(
    title="Bike Store Room API"
)

Base.metadata.create_all(bind=engine)

app.include_router(bike_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Bike Store Room API"
    }