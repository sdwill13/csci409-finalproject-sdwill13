from pydantic_settings import BaseSettings
from pydantic import BaseModel

class ServerSettings(BaseSettings):
    api_key:str = '1b5adc3ceba14db1a3291dc0f66c9baf'
    endpoint:str = 'http://api.wmata.com/Rail.svc'

class Message(BaseModel):
    message: str