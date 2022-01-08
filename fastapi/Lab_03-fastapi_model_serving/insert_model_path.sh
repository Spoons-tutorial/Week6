#!/bin/bash
docker exec -it postgresql\
 psql \
 -U postgres \
 -d postgres \
 -c "INSERT INTO rf_model VALUES ( 'rf_clf_model_0106', 'assets/random_forest.pkl' )"
 # docker로 띄운 postgresDB에 모델 경로를 기록합니다.
 # API에서는 요청에 따라 DB에서 경로를 읽어 그 값으로 모델을 읽어옵니다.