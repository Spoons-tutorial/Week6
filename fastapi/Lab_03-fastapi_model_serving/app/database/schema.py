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


class RFModel(Base):
    __tablename__ = 'rf_model'
    model_name = Column(String, primary_key = True)
    model_path = Column(String, nullable = False)
    