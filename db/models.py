from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from typing import List
from sqlalchemy.orm import relationship



class Userdb(Base):
    __tablename__ = "user"
    id = Column("id",Integer,index=True,primary_key=True)
    username = Column("name",String(20))
    email =Column("email",String)
    password = Column("password",String(10))
    is_verifayd = Column("is_verifayd",Boolean,default=False)
    item = relationship('Articledb',back_populates='user')

class Articledb(Base):
    __tablename__ = 'article'
    id = Column("id",Integer,index=True,primary_key=True)
    title = Column("title",String(20))
    content =Column("content",String)
    published =Column("published",Boolean)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship('Userdb',back_populates='item')

