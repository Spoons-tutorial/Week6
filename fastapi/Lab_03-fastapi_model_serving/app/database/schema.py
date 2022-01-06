from sqlalchemy.sql.expression import null
from app.database.db import Base
from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    age = Column(Integer, nullable = False)
    gender = Column(String, nullable = False)
    country = Column(String, nullable = True)
    # 데이터베이스 스키마를 생성합니다.
