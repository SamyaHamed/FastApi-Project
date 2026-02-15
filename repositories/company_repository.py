from database.data import db
from models.Company import Company


class CompanyRepository:

    @staticmethod
    def create(company: Company) -> Company:
        try:
            db.add(company)
            db.commit()
            db.refresh(company)
            return company
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def get_by_id(company_id: int) -> Company | None:
        return db.query(Company).filter(Company.user_id == company_id).first()
