from fastapi import FastAPI,status,Response
from router import blog_get,blog_post
from router import user
from router import file
from router import article
from router import product
from db import models
from db.database import engine
from fastapi.requests import Request
from exceptions import EmailVALID
from fastapi.responses import JSONResponse
from auth import authentication
from fastapi.routing import APIRoute



app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)
models.Base.metadata.create_all(bind=engine)


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'

use_route_names_as_operation_ids(app)


@app.exception_handler(EmailVALID)
def email_validtion(exc:EmailVALID,request :Request):
    return JSONResponse(content=str(exc),status_code=status.HTTP_400_BAD_REQUEST)
