from fastapi import APIRouter, Depends
from controller.auth_controller import AuthController
from dependencies.auth_dependency import get_current_user
from schemas.auth import token_response, signup_request, login_request

router = APIRouter(prefix="/auth", tags=["Auth"])

auth_controller = AuthController()

@router.post("/login", response_model=token_response)
def login(
    data: login_request,
):
    return auth_controller.login(data)

@router.post("/signup")
def signup(
    data: signup_request,
):
    return auth_controller.sign_up(data)

@router.get("/get-profile")
def get_profile(
    current_user=Depends(get_current_user),
):
    return auth_controller.get_profile(current_user)
