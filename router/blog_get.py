from fastapi import FastAPI,status,Response,APIRouter
from enum import Enum



router=APIRouter(prefix='/blog',tags=['blog'])


class Massage(str,Enum):
    test1="here"
@router.get("/{id}/comments/{comments}",tags=['comments'])
def blog_test(id:int=2,comments=Massage,valid:bool=True,name:str | None=None):
    return {'massage' : f'your id is {id} and you said {comments} but your vlaid is {valid=}and this is yor name {name=}'}

@router.get("/blog/{id}")
def blog_id(id:int=2,valid:bool=True):
    return {'massage' : f"bliog {id} and {valid=}"}
            

@router.get("/page/{number}")
def blog_test(number:int):
    return {'massage' : f"number od page {number}"}

@router.get("/all")
def blog_test():
    return {'massage' : f"all the pages"}       


