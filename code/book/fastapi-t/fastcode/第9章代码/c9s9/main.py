import datetime

import jwt
from jwt import ExpiredSignatureError, PyJWTError


secret_key = "jasijia*(&892345j8"
exp = datetime.datetime.now() + datetime.timedelta(days=1)
data = {"user_id": 20202, "name": "liuxu", "email": "liuxu@as.com", "exp": exp}

# 加密
jwt_token = jwt.encode(payload=data, key=secret_key)

print(jwt_token)

# 解密
try:
    user_info = jwt.decode(jwt_token, key=secret_key, algorithms='HS256')
except ExpiredSignatureError:
    print("invalid jwttoken")

print(user_info)