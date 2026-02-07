from sqlalchemy.orm import Session
from models.Trainee import Trainee 

class TraineeRepository:
    def __init__(self , db : Session):
        self.db = db

    def create(self , trainee : Trainee) -> Trainee:
        try:    
            self.db.add(trainee)
            self.db.commit()
            self.db.refresh(trainee)
            return trainee
        except Exception as e:
                self.db.rollback()
                raise e
    
    def get_by_id(self , id : int) -> Trainee | None:
        return(self.db.query(Trainee).filter(Trainee.user_id == id).first())
        