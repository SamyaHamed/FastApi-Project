from database.data import db
from models.Trainee import Trainee


class TraineeRepository:

    @staticmethod
    def create(trainee: Trainee) -> Trainee:
        try:
            db.add(trainee)
            db.commit()
            db.refresh(trainee)
            return trainee
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def get_by_id(trainee_id: int) -> Trainee | None:
        return db.query(Trainee).filter(Trainee.user_id == trainee_id).first()
