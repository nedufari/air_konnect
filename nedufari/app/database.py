from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from datetime import time
import time
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name }'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine= create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal= sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base() 

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close


# we need to introduce an environment variable to hide our vital information
#an environment variable is a variable configured on your local machine 


