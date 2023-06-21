from sqlalchemy.orm.session import Session
from db.models import Userdb
from db.hash import Hash
from schemas import UserBase
from exceptions import EmailVALID
from emails import *
from fastapi.exceptions import HTTPException
from db import db_article,db_user
from fastapi import status

async def create_user(db:Session,request:UserBase):
    if '@' not in request.email:
        raise EmailVALID('@ not fund')
    user = Userdb(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    await send_email(email=[request.email],instance=user)
    return JSONResponse(status_code=200, content={"message": "email has been sent","user":user})

def verify_token(token:str,db:Session):
    try:
        payload = jwt.decode(token,conf["SECRET"],algorithms=("HS256"))
        user =  db.query(db_user.Userdb).get(db_user.Userdb.id == payload.get('id'))
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid username',
                            headers={"WWW-Athenticate":"Bearer"})
    return user    
    

def read_all_user(db:Session):
    return db.query(Userdb).all()

def get_user_by_username(username:str,db:Session):
    return db.query(Userdb).filter(Userdb.username==username).first()

def read_user(id,db:Session):
    return db.query(Userdb).filter(Userdb.id==id).first()

def delete_user(id,db:Session):
    user=read_user(id,db)
    db.delete(user)
    db.commit()
    return 'ok'

def update_user(id,db:Session,request:UserBase):
    user=db.query(Userdb).filter(Userdb.id==id)
    user.update({
        Userdb.username : request.username,
        Userdb.email : request.email,
        Userdb.password: Hash.bcrypt(request.password),
        })
    db.commit()
    return 'ok'
