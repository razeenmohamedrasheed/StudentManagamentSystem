from fastapi import APIRouter,HTTPException,status
from college.schemas import User
from passlib.context import CryptContext
from college.models import UserData
from fastapi.params import Depends
from sqlalchemy.orm import Session
from college.database import get_db



router = APIRouter(
    tags=["Registration"]
)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

@router.post('/signup')
def createUser(payload:User,db:Session = Depends(get_db),status_code=status.HTTP_201_CREATED):
        hashed_password = pwd_context.hash(payload.password)
        new_user = UserData(
             name = payload.username,
             email = payload.email,
             contact = payload.contact,
             password = hashed_password,
             usertype_id = payload.user_type
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "User Created"
