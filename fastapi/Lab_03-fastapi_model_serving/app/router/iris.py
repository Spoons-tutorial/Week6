from fastapi import APIRouter
import numpy as np

from app.basemodels import IrisInfo
from app.database import schema
from app.database.db import engine
from app.utils import load_rf_clf


schema.Base.metadata.create_all(bind=engine)
# app/database/schema.py에서 정의한 테이블이 없으면 생성합니다.


router = APIRouter(prefix="/iris")


@router.post("/")
def get_user(iris_info: IrisInfo) -> str:
    """iris_info를 입력받아 model prediction 결과를 반환합니다.

    Args:
        iris_info (IrisInfo): sepal_length, sepal_width, petal_length, petal_width 정보

    Returns:
        str: model prediction결과가 포함된 문자열
    """
    iris_target_names = {
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    }

    rf = load_rf_clf('assets/random_forest.pkl')
    test = np.array([*iris_info.dict().values()]).reshape(1,-1)
    result = rf.predict(test)[0]
    
    return {
        "result": f'{iris_target_names[result]}로 예측되었습니다.'
    }