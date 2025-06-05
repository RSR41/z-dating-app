from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def create_user(db: Session, user_data: UserCreate) -> User:
    db_user = User(
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        name=user_data.name,
        age=user_data.age,
        gender=user_data.gender
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
