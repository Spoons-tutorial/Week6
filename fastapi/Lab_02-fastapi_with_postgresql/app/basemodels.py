from typing import Optional
from pydantic import BaseModel, Field

class UserInfo(BaseModel):
    """
    API로 입력받는 데이터들의 필수 입력 여부, 자료형, 최소-최대길이, 
    최소-최대값 등 여러 제한사항을 지정할 수 있습니다.
    """
    name: str
    age: int = Field(..., ge=0, lt=200) # 0<= age <200, ge: greater than or equal to, lt: less than
    gender: str
    contry: Optional[str] = Field(None, min_length=1, max_length=100)

    class Config: # swagger에서 보여줄 각 파라미터에 대한 예시를 설정할 수 있습니다.
        schema_extra={
            "example": {
                "name": "eva",
                "age": 41,
                "gender": "female",
                "contry": "France"
            }
        }