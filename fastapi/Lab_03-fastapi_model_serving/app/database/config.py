import os
from dotenv import load_dotenv

load_dotenv() # .env파일에 있는 데이터를 환경변수로 로드

class DBconfig:
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    # 환경변수로부터 데이터베이스 접근에 필요한 정보들을 불러옵니다.


    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        + f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    ) # 데이터베이스 접근에 필요한 url을 생성합니다.