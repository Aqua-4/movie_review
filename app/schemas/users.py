from pydantic import BaseModel, EmailStr, Field


class User:

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class UserCreate(BaseModel):
    """
    Pydantic model for user registration data.
    This is what the client sends to the server.
    """
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserInDB(BaseModel):
    """
    Pydantic model for a user stored in the database.
    It should not include the plaintext password.
    """
    username: str
    email: EmailStr
    is_active: bool = True


class UserResponse(BaseModel):
    """Pydantic model for the data returned to the client."""
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
