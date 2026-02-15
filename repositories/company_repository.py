from sqlalchemy.orm import Session
from models.Company import Company
from database.data import db


class CompanyRepository:
    
    @staticmethod
    def create( company : Company) -> Company:
        try:
            db.add(company)
            db.commit()
            db.refresh(company)
            return company
        except Exception as e:
            db.rollback()
            raise e
    
    def get_by_id( id : int) -> Company | None:
        return (db.query(Company).filter(Company.user_id == id).first())
    
