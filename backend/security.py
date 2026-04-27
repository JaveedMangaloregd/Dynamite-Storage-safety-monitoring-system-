from jose import jwt

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def create_access_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])