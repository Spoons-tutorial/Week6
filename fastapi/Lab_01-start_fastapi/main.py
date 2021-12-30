from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserInfo(BaseModel):
    """
    API로 입력받는 데이터들의 필수 입력 여부, 자료형, 최소-최대길이, 
    최소-최대값 등 여러 제한사항을 지정할 수 있습니다.
    """
    name: str
    address: Optional[str] = Field(None, min_length=1, max_length=100)
    # 자료형을 명시하는 자리에 Optional을 추가하면 해당 파라미터를
    # 필수적으로 요구하지 않게 할 수 있습니다.
    # Optional을 설정하지 않고 Field의 첫번째 파라미터로 
    # None을 입력해도 동일하게 작동합니다.

user_list = {}


@app.get("/") # 해당 엔드포인트로 get 요청을 받으면 아래의 함수를 실행합니다.
def root():
    return {"message": "Hello World"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in user_list.keys(): # 요청받은 유저의 id가 user_list에 있으면 해당 유저의 정보를 반환해 줍니다.
        return {"user info": user_list[user_id]}
    else:
        return {"error": "해당 id를 가진 유저가 없습니다."}


@app.post("/users/{user_id}")
def add_user(user_id: int, user_info: UserInfo):
    if user_id in user_list.keys():
        return {"error": "해당 id를 가진 유저가 이미 존재합니다."} # 중복된 id 삽입을 허용하지 않습니다.
    else:
        user_list[user_id] = user_info.dict() # id가 고유하다면 해당 유저의 정보를 user_list에 저장합니다.
        return {"result": f"{user_list[user_id]['name']} 유저가 추가되었습니다."} 
        # 결과로 요청받은 user_id를 가진 유저의 이름을 user_list에서 찾아 반환해 줍니다.