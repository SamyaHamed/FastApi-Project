from sqlalchemy.orm import Session
from models.User import User
from database.data import db

class UserRepository:
    
    @staticmethod
    def get_by_id( user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_email(email : str) -> User | None:
        return(
            db.query(User)
            .filter(User.email == email)
            .first()
        )
    
    @staticmethod
    def create(user : User) -> User:
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            raise e
    



