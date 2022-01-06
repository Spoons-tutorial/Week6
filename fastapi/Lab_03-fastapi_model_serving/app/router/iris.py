from fastapi import APIRouter, HTTPException
import numpy as np

from app.basemodels import IrisInfo
from app.database import schema
from app.database.db import engine
from app.database.query import SELECT_MODEL
from app.utils import load_rf_clf


schema.Base.metadata.create_all(bind=engine)
# app/database/schema.py에서 정의한 테이블이 없으면 생성합니다.


router = APIRouter(prefix="/iris")


@router.post("/")
def predict_iris(iris_info: IrisInfo, model_name:str = 'rf_clf_model_0106') -> str:
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
    try:
        with engine.connect() as conn:
            result = conn.execute(SELECT_MODEL.format(model_name)).fetchone()
            model_name, model_path = result
    except:
        raise HTTPException(status_code=404, detail="insert_model_path.sh를 실행해주세요.")

    try:
        rf = load_rf_clf(model_path)
        test = np.array([*iris_info.dict().values()]).reshape(1,-1)
        result = rf.predict(test)[0]
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail="입력하신 모델명은 존재하지 않습니다.")
        
    return {
        "result": f'{model_name} 모델로 예측한 결과는 {iris_target_names[result]}입니다.'
    }


