from pydantic import EmailStr,BaseModel
from typing import Optional
from app_enums.UserRole import UserRole

class login_request(BaseModel):
    email : EmailStr
    password : str

class token_response(BaseModel):
    access_token : str
    token_type : str = "bearer"

class signup_request(BaseModel):
    role : UserRole
    email : EmailStr
    password : str
    first_name : Optional [str] = None
    last_name : Optional [str] = None
    name : Optional [str] = None
    city : Optional [str] = None

class get_profile_response(BaseModel):
    name : str
    email : str
    city : Optional [str] = None
    
     