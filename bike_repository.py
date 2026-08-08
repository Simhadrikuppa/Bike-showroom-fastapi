from sqlalchemy.orm import Session

from bike_models import Bike
from bike_schema import BikeCreate, BikeUpdate


class BikeRepository:

    # Create Bike
    def create_bike(self, db: Session, bike: BikeCreate):
        new_bike = Bike(**bike.model_dump())

        db.add(new_bike)
        db.commit()
        db.refresh(new_bike)

        return new_bike


    # Get All Bikes
    def get_all_bikes(self, db: Session):
        return db.query(Bike).all()


    # Get Bike By ID
    def get_bike_by_id(self, db: Session, bike_id: int):
        return db.query(Bike).filter(Bike.bike_id == bike_id).first()


    # Update Bike
    def update_bike(self, db: Session, bike_id: int, bike: BikeUpdate):

        bike_data = db.query(Bike).filter(Bike.bike_id == bike_id).first()

        if not bike_data:
            return None

        update_data = bike.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(bike_data, key, value)

        db.commit()
        db.refresh(bike_data)

        return bike_data


    # Delete Bike
    def delete_bike(self, db: Session, bike_id: int):

        bike = db.query(Bike).filter(Bike.bike_id == bike_id).first()

        if not bike:
            return None

        db.delete(bike)
        db.commit()

        return bike


# Object Creation
bike_repository = BikeRepository()