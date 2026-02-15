from app_enums.UserRole import UserRole
from models.Company import Company
from models.User import User
from repositories.company_repository import CompanyRepository
from repositories.user_repository import UserRepository
from schemas.auth import signup_request
from services.signup.base import SignUpStrategy
from utils.hashing import Hashing


class CompanySignUp(SignUpStrategy):
    @staticmethod
    def execute(data: signup_request):
        existing_user = UserRepository.get_by_email(data.email)
        if existing_user:
            return None
        user = User(
            email=data.email,
            password=Hashing.hash_pass(data.password),
            role=UserRole.Company,
        )

        company = Company(name=data.name, city=data.city, user=user)
        UserRepository.create(user)
        CompanyRepository.create(company)
        return user
