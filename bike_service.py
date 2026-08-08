from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from bike_repository import bike_repository
from bike_schema import BikeCreate, BikeUpdate


class BikeService:

    # Create Bike
    def create_bike(self, db: Session, bike: BikeCreate):

        if bike.price <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be greater than zero."
            )

        if bike.stock < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Stock cannot be negative."
            )

        return bike_repository.create_bike(db, bike)

    # Get All Bikes
    def get_all_bikes(self, db: Session):
        return bike_repository.get_all_bikes(db)

    # Get Bike By ID
    def get_bike_by_id(self, db: Session, bike_id: int):

        bike = bike_repository.get_bike_by_id(db, bike_id)

        if not bike:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bike not found."
            )

        return bike

    # Update Bike
    def update_bike(self, db: Session, bike_id: int, bike: BikeUpdate):

        bike_data = bike_repository.update_bike(db, bike_id, bike)

        if not bike_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bike not found."
            )

        return bike_data

    # Delete Bike
    def delete_bike(self, db: Session, bike_id: int):

        bike = bike_repository.delete_bike(db, bike_id)

        if not bike:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bike not found."
            )

        return {"message": "Bike deleted successfully."}


# Object Creation
bike_service = BikeService()