from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from auth_repository import auth_repository
from auth_schema import UserRegister, UserLogin
from auth import get_password_hash, verify_password, create_access_token


class AuthService:

    # Register User
    def register_user(self, db: Session, user: UserRegister):

        existing_user = auth_repository.get_user_by_username(
            db,
            user.username
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        hashed_password = get_password_hash(user.password)

        return auth_repository.create_user(
            db,
            user,
            hashed_password
        )

    # Login User
    def login_user(self, db: Session, user: UserLogin):

        existing_user = auth_repository.get_user_by_username(
            db,
            user.username
        )

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        if not verify_password(
            user.password,
            existing_user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        access_token = create_access_token(
            data={"sub": existing_user.username}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }


auth_service = AuthService()