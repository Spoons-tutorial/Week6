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
    country: Optional[str] = Field(None, min_length=1, max_length=100)


    class Config: # swagger에서 보여줄 각 파라미터에 대한 예시를 설정할 수 있습니다.
        schema_extra={
            "example": {
                "name": "eva",
                "age": 41,
                "gender": "female",
                "country": "France"
            }
        }


class IrisInfo(BaseModel):
    """
    들어올 입력값의 범위를 제한하여 잘못된 입력을 막을 수 있습니다.
    ex) pixel range: 0-255
    """
    sepal_length: float = Field(..., ge=4.3, le=7.9)
    sepal_width: float = Field(..., ge=2.0, le=4.4)
    petal_length: float = Field(..., ge=1.0, le=6.9)
    petal_width: float = Field(..., ge=0.1, le=2.5)


    class Config: # swagger에서 보여줄 각 파라미터에 대한 예시를 설정할 수 있습니다.
        schema_extra={
            "example": {
                "sepal_length": 4.8,
                "sepal_width": 4.1,
                "petal_length": 3.3,
                "petal_width": 1.7
            }
        }