# Lab1

- Lab1은 Fastapi입니다.
- `user_list`라는 dictionary에 HTTP request를 보내 정보를 업데이트하고 조회하는 것을 실습합니다.
  - [HTTP request methods documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- post request를 통해 정보를 업데이트 합니다.
  - request를 보냈을 때 user_id가 이미 dictionary에 존재할 경우 `error`로 접근가능한 json에 문자열을 담아 리턴합니다.
  - request를 보냈을 때 user_id가 존재하지 않는 경우 user_id를 key값으로 사용해서 [request body](https://fastapi.tiangolo.com/tutorial/body/) 로 들어온 user_info를 dictionary에 추가합니다.


- get request를 통해 정보를 조회합니다.
  - request를 보냈을 때 [path parameter](https://fastapi.tiangolo.com/tutorial/path-params/)로 들어온 user_id가 dictionary에 존재할 경우 해당 유저의 정보를 반환합니다.