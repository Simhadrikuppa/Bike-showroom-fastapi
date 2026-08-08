from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from bike_schema import (
    BikeCreate,
    BikeUpdate,
    BikeResponse
)
from bike_service import bike_service


router = APIRouter(
    prefix="/bikes",
    tags=["Bikes"]
)


# Create Bike
@router.post("/", response_model=BikeResponse)
def create_bike(
    bike: BikeCreate,
    db: Session = Depends(get_db)
):
    return bike_service.create_bike(db, bike)


# Get All Bikes
@router.get("/", response_model=List[BikeResponse])
def get_all_bikes(
    db: Session = Depends(get_db)
):
    return bike_service.get_all_bikes(db)


# Get Bike By ID
@router.get("/{bike_id}", response_model=BikeResponse)
def get_bike_by_id(
    bike_id: int,
    db: Session = Depends(get_db)
):
    return bike_service.get_bike_by_id(db, bike_id)


# Update Bike
@router.put("/{bike_id}", response_model=BikeResponse)
def update_bike(
    bike_id: int,
    bike: BikeUpdate,
    db: Session = Depends(get_db)
):
    return bike_service.update_bike(db, bike_id, bike)


# Delete Bike
@router.delete("/{bike_id}")
def delete_bike(
    bike_id: int,
    db: Session = Depends(get_db)
):
    return bike_service.delete_bike(db, bike_id)