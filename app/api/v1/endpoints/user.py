from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, User
from app.crud.user import create_user, get_user
from app.database import get_db
from consumers.user_consumer import publish_message

router = APIRouter()

@router.post("/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db=db, user=user)
        publish_message("user.created", {"id": new_user.id, "email": new_user.email})
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
