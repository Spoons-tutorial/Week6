GET_USER = """
SELECT * 
FROM users 
WHERE user_id={}
"""


INSERT_USER = """
INSERT INTO users
VALUES ({}, '{}', {}, '{}', '{}')
"""

DELETE_USER = """
DELETE FROM users
WHERE user_id={}
"""


UPDATE_USER = """
UPDATE users
SET
    name = '{}',
    age = {},
    gender = '{}',
    country = '{}'
WHERE
    user_id = {}
"""

SELECT_MODEL = """
SELECT *
FROM rf_model
WHERE model_name = '{}'
"""