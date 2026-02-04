from pydantic import EmailStr,BaseModel
from typing import Optional

class login_request(BaseModel):
    email : EmailStr
    password : str

class token_response(BaseModel):
    access_token : str
    token_type : str = "bearer"

class trainee_signup(BaseModel):
    email : EmailStr
    password : str
    first_name : str
    last_name : str

class company_signup(BaseModel):
    email : EmailStr
    password : str
    name : str
    city : str

class get_profile_response(BaseModel):
    name : str
    email : str
    city : Optional [str] = None
    
     