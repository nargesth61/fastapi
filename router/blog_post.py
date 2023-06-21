from fastapi import FastAPI,status,Response,APIRouter , Query ,Body ,Path
from enum import Enum
from pydantic import BaseModel
from typing import Annotated,List

router = APIRouter(prefix='/blog',tags=['blog'])

class Post_Model(BaseModel):
    title : str
    content : Annotated[str,Body(max_length=20)] = 'sey your idea'
    nb_comments : int
    published : bool


class test(Enum):
    x="rewew"

class testm(BaseModel):
     title : Annotated[str,Body(title="sey my name!",max_length=100)]
     age: int = Body(gt=10)

@router.post('/test/{id}')
def test1 (blog:testm, id:int = Path(lt=10), comment : List[str] =None):
     return  {'message': f"your post is created {id}",'comment':comment,'data':blog}




@router.post('/create/{id}')
def create_post(blog:Post_Model,id:int=Path(lt=5)):
    return {'message': f"your post is created {id}",'data':blog}

@router.post('/comments')
def create_comments(blog:Post_Model,comments_id:int=Query(default=1,
                                                      title='id comment',
                                                      alias='CommID',
                                                      description='THIS IS COMMENT ID',
                                                      deprecated=False)):
        return {'message': f"your comment {comments_id}",'data':blog}

#def create_post(blog:Post_Model,comments_id:Annotated[int,Query(
#                                                      title='id comment',
#                                                      alias='CommID',
#                                                      description='THIS IS COMMENT ID',
#                                                      deprecated=False)] = 1):
#        return {'message': f"your comment {comments_id}",'data':blog}

