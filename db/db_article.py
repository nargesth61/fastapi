from sqlalchemy.orm.session import Session
from db.models import Articledb
from schemas import Areticlebase
from fastapi.exceptions import HTTPException
from fastapi import status



def create_article(db:Session,request:Areticlebase):
    article =Articledb (
        title = request.title,
        content = request.content,
        user_id = request.user_id,
        published = request.published,      
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(id,db:Session):
    article = db.query(Articledb).filter(Articledb.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id}not found') 
    return article
