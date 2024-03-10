from fastapi import FastAPI,Response,status ,HTTPException ,Depends ,APIRouter
from sqlalchemy.orm import Session 
from typing import List

from .. import utils
from ..database import get_db
from .. import models,schemas ,oauth2


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


# Users....
@router.post("/",response_model=schemas.UserOut,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    # hash the password - user.pasword
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())

    check_user = db.query(models.User).filter(models.User.email == new_user.email).first()
    if check_user:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail=f" this email is already regestered .")
    
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user 


@router.get("/",response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):

    user_query = db.query(models.User).all()
    return user_query

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.id == id).first()

    if not user_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id: {id} was not found :(")
    return user_query

@router.put("/users/{id}",response_model=schemas.UserOut)
def update_user(id:int,db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.id == id).first()

    if user_query==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found :(")
    
    return user_query