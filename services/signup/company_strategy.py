from models.Company import Company
from models.Trainee import Trainee
from models.User import User
from utils.hashing import Hashing
from services.signup.base import SignUpStrategy
from app_enums.UserRole import UserRole
from repositories.company_repository import CompanyRepository
from repositories.user_repository import UserRepository

class CompanySignUp (SignUpStrategy):
    
    def __init__(
        self,
        user_repo: UserRepository,
        company_repo: CompanyRepository
    ):
        self.user_repo = user_repo
        self.company_repo = company_repo


    def execute(self, data):
        existing_user = self.user_repo.get_by_email(data.email)
        if existing_user:
            return None
        
    
        user = User(
            email = data.email,
            password = Hashing.hash_pass(data.password),
            role = UserRole.Company
            )
            
        company = Company(
            name = data.name,
            city = data.city,
            user = user
            )
        self.user_repo.create(user)
        self.company_repo.create(company)
        return user

        