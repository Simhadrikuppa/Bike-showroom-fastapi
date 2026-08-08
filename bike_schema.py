from pydantic import BaseModel
from typing import Optional


# Create Bike Schema
class BikeCreate(BaseModel):
    brand: str
    model: str
    color: str
    engine_cc: int
    fuel_type: str
    price: float
    stock: int


# Update Bike Schema
class BikeUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    engine_cc: Optional[int] = None
    fuel_type: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


# Response Schema
class BikeResponse(BaseModel):
    bike_id: int
    brand: str
    model: str
    color: str
    engine_cc: int
    fuel_type: str
    price: float
    stock: int

    class Config:
        from_attributes = True