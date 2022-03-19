import numpy as np
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from ..utils import load_rf_clf
from ..basemodels import IrisInfo

router = APIRouter(prefix='/iris')

@router.get('/predict')
async def predict(iris_info: IrisInfo):
    model = None
    try:
        model = load_rf_clf('assets/random_forest.pkl')
    except Exception as e:
        raise HTTPException(detail="model is not loaded", 
              status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    input_data = np.array([*iris_info.dict().values()]).reshape(1,-1)
    result = {'result': model.predict(input_data).tolist()}

    return JSONResponse(content=result)