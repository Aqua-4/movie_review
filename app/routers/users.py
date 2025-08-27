from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, status
from ..schemas.users import UserCreate, UserInDB, UserResponse, User
router = APIRouter()


fake_db = [User("testuser", "testuser@example.com")] 

@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    """
    Registers a new user.
    """
    # In a real app, you would hash the password before storing it.
    # This is a simplified example.
    
    # Check if user already exists
    if any(db_user.email == user.email for db_user in fake_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create the user and save it to the "database"
    user_in_db = UserInDB(username=user.username, email=user.email, is_active=True)
    fake_db.append(user_in_db)
    
    # Create a response model to exclude the password
    return UserResponse(username=user_in_db.username, email=user_in_db.email)
