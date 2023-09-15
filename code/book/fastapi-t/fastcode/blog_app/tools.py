import datetime

from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError


class Hashing:
    def __init__(self, schemes: str = "bcrypt"):
        self.crypt = CryptContext(schemes=[schemes], deprecated="auto")

    def hash(self, raw_pwd: str) -> str:
        return self.crypt.hash(raw_pwd)

    def verify(self, raw_pwd: str, hashed_pwd: str) -> bool:
        return self.crypt.verify(raw_pwd, hashed_pwd)


class Jwt:
    JWT_KEY = "ASDN*^n23^$:_};pYz7I"
    ALGORITHMS = "HS256"

    def set_token(self, data: dict) -> str:
        if "exp" not in data:
            data["exp"] = datetime.datetime.now() + datetime.timedelta(days=1)
        return jwt.encode(data, key=self.JWT_KEY)

    def get_token(self, jwt_token: str):
        try:
            return jwt.decode(jwt_token, self.JWT_KEY, self.ALGORITHMS)
        except JWTError as e:
            raise HTTPException(detail=e, status_code=403)


hash_obj = Hashing()
jwt_obj = Jwt()
