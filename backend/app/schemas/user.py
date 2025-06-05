# backend/app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field

# ───────── 입력용 ─────────
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

# ───────── 출력용 ─────────
class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_verified: bool

    class Config:
        orm_mode = True
