from sqlalchemy.orm import Session
from app_enums.UserRole import UserRole
from models.Trainee import Trainee
from models.User import User 
from services.signup.base import SignUpStrategy
from utils.hashing import Hashing
from repositories.user_repository import UserRepository
from repositories.trainee_repository import TraineeRepository

class TraineeSignUp(SignUpStrategy):
    def __init__(
        self,
        user_repo: UserRepository,
        trainee_repo: TraineeRepository
    ):
        self.user_repo = user_repo
        self.trainee_repo = trainee_repo

    def execute(self, data):
        existing_user = self.user_repo.get_by_email(data.email)
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
        self.user_repo.create(user)
        self.trainee_repo.create(trainee)
        return user

        