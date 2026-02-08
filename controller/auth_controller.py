from fastapi import Depends,HTTPException,status
from schemas.auth import signup_request,login_request
from services.auth_services import AuthService
from dependencies.auth_dependency import get_current_user
#from dependencies.auth_provider import get_auth_service


class AuthController:
    #def __init__(self):
    #    self.auth_service = auth_service


    def login( self ,data : login_request):
        token = AuthService.login(data.email,data.password)
        if not token:
             raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid email or password"
                )
        return {"access_token": token, "token_type": "bearer"}


    def sign_up(self ,data : signup_request ):
        user = AuthService.sign_up(data)
        if not user :
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = "Email already exists"
            )
        return user

    def get_profile(
        self,
        current_user = Depends(get_current_user)
        ):
        profile = AuthService.get_profile(current_user)
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        return profile
    

