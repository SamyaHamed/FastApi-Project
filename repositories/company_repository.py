from sqlalchemy.orm import Session
from models.Company import Company

class CompanyRepository:
    def __init__(self, db : Session):
        self.db = db

    def create(self , company : Company) -> Company:
        try:
            self.db.add(company)
            self.db.commit()
            self.db.refresh(company)
            return company
        except Exception as e:
            self.db.rollback()
            raise e
    
    def get_by_id(self , id : int) -> Company | None:
        return (self.db.query(Company).filter(Company.user_id == id).first())
    
