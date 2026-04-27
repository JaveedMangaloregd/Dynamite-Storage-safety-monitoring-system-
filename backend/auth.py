from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from security import create_access_token

router = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Login API
@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.username == username).first()

    if user and user.password == password:
        token = create_access_token({"sub": username})
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    
    raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"access_token": token}

    return {"error": "Invalid credentials"}