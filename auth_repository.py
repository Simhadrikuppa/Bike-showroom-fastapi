from sqlalchemy.orm import Session

from auth_model import User
from auth_schema import UserRegister


class AuthRepository:

    # Create User
    def create_user(self, db: Session, user: UserRegister, hashed_password: str):

        new_user = User(
            username=user.username,
            password=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    # Get User By Username
    def get_user_by_username(self, db: Session, username: str):

        return db.query(User).filter(
            User.username == username
        ).first()


auth_repository = AuthRepository()