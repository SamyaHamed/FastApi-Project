from sqlalchemy.orm import Session
from models.User import User
from models.Trainee import Trainee
from models.Company import Company
from core.security import  create_access_token
from utils.hashing    import Hashing
from schemas.auth import signup_request
from config import settings
from datetime import timedelta
from app_enums.UserRole import UserRole
from services.signup.factory import SignUpStrategyFactory
from repositories.company_repository import CompanyRepository
from repositories.trainee_repository import TraineeRepository
from repositories.user_repository import UserRepository

class AuthService:
    def __init__(
        self,
        user_repo: UserRepository,
        trainee_repo: TraineeRepository,
        company_repo: CompanyRepository
    ):
        self.user_repo = user_repo
        self.trainee_repo = trainee_repo
        self.company_repo = company_repo


    def login(self, email: str, password: str) -> str | None:
        user = self.user_repo.get_by_email(email)
        if not user:
            return None
        
        if not Hashing.verify_pass(password,user.password):
            return None
        
        access_token = create_access_token(
            user_id = user.id,
            role= user.role,
            expires_delta= timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return access_token
    
    
    def sign_up(self, data: signup_request):
        #strategy = SignUpStrategyFactory.get_strategy(data.role)
        strategy = SignUpStrategyFactory.get_strategy(
        role=data.role,
        user_repo=self.user_repo,
        trainee_repo=self.trainee_repo,
        company_repo=self.company_repo
            )
        user = strategy.execute(data)
        return user
    
    
    def get_profile(self,user: User):
        if user.role == UserRole.Trainee:
            trainee = self.trainee_repo.get_by_id(user.id)
            if not trainee:
                return None

            return {
                "name": f"{trainee.first_name} {trainee.last_name}",
                "email": user.email
            }

        elif user.role == UserRole.Company:
            company = self.company_repo.get_by_id(user.id)
            if not company:
                return None

            return {
                "name": company.name,
                "email": user.email,
                "city": company.city
            }

        return None
    

  
            





