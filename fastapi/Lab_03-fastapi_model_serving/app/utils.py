import joblib
from sklearn.ensemble import RandomForestClassifier

def load_rf_clf(model_path: str) -> RandomForestClassifier:
    """경로를 읽어 RandomForestClassifier모델을 반환합니다.

    Args:
        model_path (str): 모델이 위치한 경로

    Returns:
        RandomForestClassifier: joblib.load를 통해 읽어온 RandomForestClassifier모델
    """
    model = joblib.load(model_path)

    return model