from pydantic import BaseModel

class User(BaseModel):
    username:str
    email:str
    contact:str
    password:str
    user_type:int
