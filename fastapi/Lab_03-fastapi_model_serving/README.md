# Lab3

- Lab3는 간단한 ML model을 Fastapi로 서빙하는 내용을 담고있습니다.

- [insert_model_path.sh](./insert_model_path.sh)는 assets폴더에 저장된 random_forest모델을 postgres db에 이름과 경로를 기록하는 역할을 하고있습니다.

- [iris.py](./app/router/iris.py)는 모델을 load하기 위해 아래와 같은 단계를 거칩니다.
  1. db에 모델이 저장된 경로를 조회한다.
  2. db에서 받아온 경로를 바탕으로 모델을 읽어온다.

- 모델을 load에서 [try except](https://docs.python.org/3/tutorial/errors.html) 경우
  - FileNotFoundError 만 캐치하도록 되어있습니다. (다른 오류가 일어날 경우 catch하지 않습니다.)

- `return {"error": "~~"}` 를 HTTPException으로 수정하였습니다.
  - HTTPException(https://fastapi.tiangolo.com/tutorial/handling-errors/)에 작성된 내용을 토대로 사용자에게 리턴됩니다.
  - 이를 통해 상황에 맞는 HTTP code를 전달할 수 있습니다.