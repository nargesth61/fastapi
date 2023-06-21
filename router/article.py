from fastapi import FastAPI,status,Response,APIRouter , Query ,Body ,Path ,Depends
from enum import Enum
from pydantic import BaseModel
from typing import Annotated,List
from schemas import Areticlebase,Articledesplay,UserBase
from db.database import get_db
from db import db_article
from auth.oauth2 import get_tokens

router = APIRouter(prefix='/article',tags=['article'])


@router.post('/', response_model=Articledesplay)
def create_article(article: Areticlebase, db=Depends(get_db)):
    return db_article.create_article(db, article)

@router.get('/{id}')
def get_article(id: int,db = Depends(get_db),curent_user:UserBase=Depends(get_tokens)):
    return {
         'data':db_article.get_article(id,db),
         'user':curent_user
    }