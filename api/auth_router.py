from fastapi import APIRouter, Depends
from controller.auth_controller import AuthController
from dependencies.auth_provider import get_auth_service
from dependencies.auth_dependency import get_current_user
from schemas.auth import token_response, signup_request, login_request

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_auth_controller(
    auth_service=Depends(get_auth_service)
):
    return AuthController(auth_service)

@router.post("/login", response_model=token_response)
def login(
    data: login_request,
    controller: AuthController = Depends(get_auth_controller)
):
    return controller.login(data)

@router.post("/signup")
def signup(
    data: signup_request,
    controller: AuthController = Depends(get_auth_controller)
):
    return controller.sign_up(data)

@router.get("/get-profile")
def get_profile(
    current_user=Depends(get_current_user),
    controller: AuthController = Depends(get_auth_controller)
):
    return controller.get_profile(current_user)
