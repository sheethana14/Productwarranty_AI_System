from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email:str
    password:str

class userLogin(BaseModel):
    email:str
    password:str