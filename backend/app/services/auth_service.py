from typing import Optional, Tuple

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
)


def create_user(db: Session, user_data: UserCreate) -> User:
    """Persist a new user and return it."""
    db_user = User(
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        name=user_data.name,
        age=user_data.age,
        gender=user_data.gender,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """Validate user credentials and return user if valid."""
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def generate_tokens(user_id: int) -> Tuple[str, str]:
    """Return access and refresh JWT tokens for the given user."""
    access = create_access_token({"sub": str(user_id)})
    refresh = create_refresh_token({"sub": str(user_id)})
    return access, refresh
