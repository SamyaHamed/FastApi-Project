from fastapi import Depends
from sqlalchemy.orm import Session
from database.data import get_db

from repositories.user_repository import UserRepository
from repositories.trainee_repository import TraineeRepository
from repositories.company_repository import CompanyRepository


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_trainee_repository(db: Session = Depends(get_db)) -> TraineeRepository:
    return TraineeRepository(db)


def get_company_repository(db: Session = Depends(get_db)) -> CompanyRepository:
    return CompanyRepository(db)
