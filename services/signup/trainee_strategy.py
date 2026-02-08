from sqlalchemy.orm import Session
from app_enums.UserRole import UserRole
from models.Trainee import Trainee
from models.User import User 
from services.signup.base import SignUpStrategy
from utils.hashing import Hashing
from repositories.user_repository import UserRepository
from repositories.trainee_repository import TraineeRepository
from schemas.auth import signup_request

class TraineeSignUp(SignUpStrategy):
    
    @staticmethod
    def execute(data : signup_request):
        existing_user = UserRepository.get_by_email(data.email)
        if existing_user :
            return None
        
        user = User(
            email = data.email,
            password = Hashing.hash_pass(data.password),
            role = UserRole.Trainee
        )
        trainee = Trainee(
            first_name = data.first_name,
            last_name = data.last_name ,
            user = user
        )
        UserRepository.create(user)
        TraineeRepository.create(trainee)
        return user

        
        