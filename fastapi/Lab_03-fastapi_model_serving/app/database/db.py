from app.database.config import DBconfig
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    DBconfig.SQLALCHEMY_DATABASE_URL,
    pool_size = 10,
    max_overflow = 20
    )
Base = declarative_base()
