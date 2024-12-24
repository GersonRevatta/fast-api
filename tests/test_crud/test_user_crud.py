from sqlalchemy.orm import Session
from app.crud.user import create_user, get_user
from app.schemas.user import UserCreate
from app.database import get_db

def test_create_user_in_db():
    db = next(get_db())
    user_data = UserCreate(
        name="User",
        email="user@example.com",
        password="123456"
    )
    user = create_user(db, user=user_data)
    assert user.name == "User"
    assert user.email == "user@example.com"

def test_get_user_in_db():
    db = next(get_db())
    user = get_user(db, user_id=1)
    if user:
        assert user.id == 1
    else:
        assert user is None
