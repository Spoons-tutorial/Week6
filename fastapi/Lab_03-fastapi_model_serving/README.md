# Lab3

- Lab3는 간단한 ML model을 Fastapi로 서빙하는 내용을 담고있습니다.

- [insert_model_path.sh](./insert_model_path.sh)는 assets폴더에 저장된 random_forest모델을 postgres db에 이름과 경로를 기록하는 역할을 하고있습니다.

- [iris.py](./app/router/iris.py)는 모델을 load하기 위해 아래와 같은 단계를 거칩니다.
  1. db에 모델이 저장된 경로를 조회한다.
  2. db에서 받아온 경로를 바탕으로 모델을 읽어온다.

- 모델을 읽어올 때 [try except](https://wikidocs.net/30) 경우
  - FileNotFoundError 만 캐치하도록 되어있습니다.

- 원하는대로 동작하지 않을 경우
  - HTTPException(https://fastapi.tiangolo.com/tutorial/handling-errors/)의 내용을 토대로 사용자에게 리턴됩니다.