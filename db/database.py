from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String,INTEGER
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///fastapidb.db",connect_args={'check_same_thread':False})
Base = declarative_base()

Session = sessionmaker(bind=engine,autoflush=False, autocommit=False)
session = Session()

def get_db():
    try:
        yield session
    finally:
        session.close()    