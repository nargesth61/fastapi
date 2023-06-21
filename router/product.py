from fastapi import FastAPI,status,Response,APIRouter,Header,Form
from fastapi.responses import HTMLResponse , PlainTextResponse
from typing import Annotated

router = APIRouter(prefix='/product', tags=['product'])


products = ['test1','test2','test3']

@router.get('/')
def product():
    item = " ".join(products)
    return Response(content=item,media_type="text/plain")

@router.get('/{id}',responses={
    404:{'content':{'text/plain':{'example':'id not found'}},
         'description':'for error'
         },
    200:{'content':{'text/html':{'example':'<div> id </div>'}},
         'description':'for html ok'
         }
})
def product_all(id:int):
    if id > len(products):
        return PlainTextResponse(content=f"id not found",media_type="text/plain",status_code=status.HTTP_404_NOT_FOUND)
    item = products[id]
    return HTMLResponse(content=f'<div> {item} </div>',media_type="text/html")


@router.get('/whitheader/')
def product_header(user_header:Annotated[str | None , Header()]=None):
    print(user_header)
    return {"header": user_header}

@router.post('/form/')
def login(username:Annotated[str , Form(...)],password:Annotated[str , Form(...)]):
    return {'username':username,'pass':password}