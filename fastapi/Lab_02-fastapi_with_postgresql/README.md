# Lab2

- Lab2는 [Fastapi Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)에 대한 내용을 담고있습니다.

- [basemodels.py](./app/basemodels.py)은 [pydantic](https://pydantic-docs.helpmanual.io/)을 이용해서 Data validation 및 type annotation을 진행합니다.
  ```python
  class UserInfo(BaseModel):
    name: str
    age: int = Field(..., ge=0, lt=200)
    gender: str
    country: Optional[str] = Field(None, min_length=1, max_length=100)


    class Config:
        schema_extra={
            "example": {
                "name": "eva",
                "age": 41,
                "gender": "female",
                "country": "France"
            }
        }
  ```


- [database/config.py](./app/database/config.py)은 postgresql database연결을 위한 값을 .env에서 읽어오는 역할을 하고있습니다.
- [database/db.py](./app/database/db.py)은 postgresql database를 사용하기 위한 [engine](https://docs.sqlalchemy.org/en/14/core/engines.html)을 실제적으로 만드는 부분입니다.
- [database/query.py](./app/database/query.py)는 db와 상호작용하기 위한 query문이 저장되어 있습니다.
- [database/schema.py](./app/database/schema.py)에서는 declarative_baes(https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html#sqlalchemy.ext.declarative.declarative_base)를 상속받아 명시적으로 table 내용을 적어주고 있습니다.