from sqlalchemy.orm import Session
from models.User import User
from models.Trainee import Trainee
from models.Company import Company
from core.security import  create_access_token
from utils.hashing import hash_pass,verify_pass
from schemas.auth import trainee_signup,company_signup
from core.config import settings
from datetime import timedelta
from app_enums.UserRole import UserRole

class AuthService:

    @staticmethod
    def login(db: Session , email: str ,password : str ):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        
        
        if not verify_pass(password,user.password):
            return None
        
        access_token = create_access_token(
            user_id = user.id,
            role= user.role,
            expires_delta= timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return access_token
    
    @staticmethod
    def trainee_sign_up(db:Session , trainee_data: trainee_signup):
        existing_user = db.query(User).filter(User.email == trainee_data.email).first()
        if existing_user: 
            return None
        
        user = User (
            email = trainee_data.email,
            password = hash_pass(trainee_data.password),
            role = UserRole.Trainee
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        trainee = Trainee(
            first_name = trainee_data.first_name,
            last_name = trainee_data.last_name,
            user = user
        )
        db.add(trainee)
        db.commit()
        db.refresh(user)


        return{
            "id" : user.id,
            "email" : user.email,
            "role" : user.role,
            "name" : trainee.first_name +" "+ trainee.last_name

        }
    
    @staticmethod
    def company_sign_up(db:Session , company_sign_up : company_signup):
        existing_user = db.query(User).filter(User.email == company_sign_up.email).first()
        if existing_user :
            return None
        
        user = User (
            email = company_sign_up.email,
            password = hash_pass(company_sign_up.password),
            role = UserRole.Company
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        company = Company(
            city = company_sign_up.city,
            name = company_sign_up.name,
            user = user
        )
        db.add(company)
        db.commit()
        db.refresh(company)

        return {
            "id" : user.id,
            "email" : user.email,
            "name" : company.name,
            "city" : company.city
        }
    

    @staticmethod
    def get_profile(db: Session, user: User):
        if user.role == UserRole.Trainee:
            trainee = db.query(Trainee).filter(Trainee.user_id == user.id).first()
            if not trainee:
                return None

            return {
                "name": f"{trainee.first_name} {trainee.last_name}",
                "email": user.email
            }

        elif user.role == UserRole.Company:
            company = db.query(Company).filter(Company.user_id == user.id).first()
            if not company:
                return None

            return {
                "name": company.name,
                "email": user.email,
                "city": company.city
            }

        return None
    

  
            





