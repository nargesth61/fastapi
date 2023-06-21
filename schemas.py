from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username : str
    email : str
    password : str
    is_verifayd : bool

#کلاسی که برای نشان دادن مقاله های یوزر است
class Article(BaseModel):
    title :str
    content : str
    class Config:
        orm_mode = True

class Userdisplay(BaseModel):
    username : str
    email : str
    item :List[Article]
    class Config:
        orm_mode = True

class Areticlebase(BaseModel):
    title: str
    content: str
    published: bool
    user_id: int

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
class Articledesplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True        