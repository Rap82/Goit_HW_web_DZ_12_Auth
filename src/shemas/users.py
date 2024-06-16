from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


from src.database.models import Role


class UserModel(BaseModel):
    username: str = Field(min_length=3, max_length=54)
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)


class NewUserResponse(BaseModel):
    username: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    avatar: str | None
    role: Role

    class Config:
        from_attributes = True
