GET_USER = """
SELECT * 
FROM users 
WHERE user_id={}
"""


INSERT_USER = """
INSERT INTO users
VALUES ({}, '{}', {}, '{}', '{}')
"""