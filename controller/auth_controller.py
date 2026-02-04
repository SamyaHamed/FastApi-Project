from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database.data import get_db
from schemas.auth import trainee_signup, company_signup, login_request, token_response,get_profile_response
from services.auth_services import AuthService
from core.dependency import get_current_user


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model= token_response)
def login(data : login_request ,db: Session = Depends(get_db)):
    token = AuthService.login(db,data.email,data.password)

    if not token:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid email or password"
        )
    return {"access_token": token, "token_type": "bearer"}


@router.post("/trainee/signup")
def trainee_sign_up(data : trainee_signup ,db: Session =Depends(get_db)):
    trainee = AuthService.trainee_sign_up(db,data)
    if not trainee :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Email already exists"
        )
    return trainee

@router.post("/signup/company")
def signup_company(data: company_signup, db: Session = Depends(get_db)):
    company = AuthService.company_sign_up(db, data)

    if not company:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    return company

@router.get("/get-profile", response_model= get_profile_response)
def get_profile(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    profile = AuthService.get_profile(db, current_user)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return profile


