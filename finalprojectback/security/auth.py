from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()

USER_CREDENTIALS = {
    "admin": "password123",
    "user": "secret"
}

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username in USER_CREDENTIALS:
        correct_password = USER_CREDENTIALS[credentials.username]
        if secrets.compare_digest(credentials.password, correct_password):
            return {"username": credentials.username}
    raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Basic"})