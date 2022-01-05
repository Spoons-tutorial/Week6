from fastapi import APIRouter
from app.basemodels import UserInfo
from app.database import schema
from app.database.db import engine
from app.database.query import GET_USER, INSERT_USER, DELETE_USER, UPDATE_USER


schema.Base.metadata.create_all(bind=engine)
# app/database/schema.py에서 정의한 테이블이 없으면 생성합니다.


router = APIRouter(prefix="/users")


@router.get("/{user_id}")
def get_user(user_id: int):
    with engine.connect() as conn:
        user = conn.execute(GET_USER.format(user_id)).fetchone()
        # 요청받은 user_id를 가진 유저의 정보를 DB에서 가져옵니다.
        # 만약, 해당 user_id가 DB에 없으면 user변수에는 None이 할당됩니다.

    if user:
        return {"user info": user}
    else:
        return {"error": "해당 id를 가진 유저가 없습니다."}


@router.post("/{user_id}")
def add_user(user_id: int, user_info: UserInfo):
    with engine.connect() as conn:
        check_id = conn.execute(GET_USER.format(user_id)).fetchone()
        # 우선, 요청받은 user_id가 DB에 있는지 조회합니다.

    if check_id: # 만약 있다면 이 조건문에 걸리므로 데이터 저장 없이 리턴합니다.
        return {"error": "해당 id를 가진 유저가 이미 존재합니다."}
    else:
        with engine.connect() as conn:
            conn.execute(
                    INSERT_USER.format(user_id, *user_info.dict().values())
                        )
            get_name = conn.execute(GET_USER.format(user_id)).fetchone()
            # 위의 조건에 걸리지 않았다면 user_id가 없다는 뜻이므로
            # 데이터를 저장하고 확인차 해당 user_id로 조회한 후
            # 해당 유저의 이름과 함께 리턴합니다.

        return {"result": f"{get_name['name']} 유저가 추가되었습니다."} 

# Hands - on
## 주어진 DELETE_USER 쿼리를 활용하여
## 유저의 아이디를 받아 해당 유저를 제거하는 코드를 작성하세요.
@router.delete('/')
def delete_user():
    pass

## 주어진 UPDATE_USER 쿼리를 활용하여
## 유저의 아이디를 받아 해당 유저의 정보를 업데이트하는 코드를 작성하세요.
@router.put('/')
def update_user():
    pass

