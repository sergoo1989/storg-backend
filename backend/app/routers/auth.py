from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.core.db import engine
from app.core.security import verify_password, create_access_token
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(username: str, password: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        if not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Wrong password")

        token = create_access_token({"sub": username, "role": user.role})
        return {"access_token": token, "token_type": "bearer"}
