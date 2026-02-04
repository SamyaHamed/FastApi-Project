from  sqlalchemy import Integer,Column,String,ForeignKey
from sqlalchemy.orm import relationship
from  database.data import Base


class TraineeProfile(Base):
    __tablename__ = "trainee_profiles"

    id = Column(Integer,primary_key=True)
    university_name = Column(String(30),nullable= False)
    bio = Column(String(255),nullable=False)

    trainee_id = Column(Integer,ForeignKey("trainees.id"),unique=True,nullable=False)
    
    trainee = relationship("Trainee",back_populates="profile")