from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth_schema import UserRegister, UserLogin, Token
from auth_service import auth_service


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return auth_service.register_user(db, user)


@router.post("/login", response_model=Token)
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return auth_service.login_user(db, user)