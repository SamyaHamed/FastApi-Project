from models.Trainee import Trainee
from database.data import db

class TraineeRepository:
    
    @staticmethod
    def create( trainee : Trainee) -> Trainee:
        try:    
            db.add(trainee)
            db.commit()
            db.refresh(trainee)
            return trainee
        except Exception as e:
                db.rollback()
                raise e
    
    def get_by_id(self , id : int) -> Trainee | None:
        return(self.db.query(Trainee).filter(Trainee.user_id == id).first())
        