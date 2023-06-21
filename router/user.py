from fastapi import FastAPI,status,Response,APIRouter , Query ,Body ,Path ,Depends,Request
from enum import Enum
from pydantic import BaseModel
from typing import Annotated,List
from schemas import UserBase,Userdisplay
from db.database import get_db
from db import db_user
from fastapi.responses import HTMLResponse
from db.db_user import verify_token
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException


router = APIRouter(prefix='/user', tags=['user'])

@router.post('/',response_model=Userdisplay)
def create_user(user:UserBase, db=Depends(get_db)):
    return db_user.create_user(db,user)



@router.get('/verifiction')
def get_verifiction_user(token : str , db=Depends(get_db)):
    user = verify_token(token)
    if user and not user.is_verifayd:
        user.update({
        db_user.Userdb.is_verifayd : True,
        })
        db.commit()
        return "verify compeleted"
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid or expire token',
                            headers={"WWW-Athenticate":"Bearer"})


@router.get('/',response_model=List[Userdisplay])
def read_all_user(db=Depends(get_db)):
    return db_user.read_all_user(db)

@router.get('/{id}',response_model=Userdisplay)
def read_user(id:int, db=Depends(get_db)):
    return db_user.read_user(id,db)

@router.get('/delete/{id}')
def delete_user(id:int, db=Depends(get_db)):
    return db_user.delete_user(id,db)

@router.post('/update/{id}')
def update_user(id:int,user:UserBase,db=Depends(get_db)):
    return db_user.update_user(id,db,user)