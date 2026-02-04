from sqlalchemy import Column,String,ForeignKey,Nullable,Integer
from sqlalchemy.orm import relationship
from database.data import Base
from models.TraineeProfile import TraineeProfile
from models.Skill import Skill
from models.Application import Application

class Trainee(Base):
    __tablename__ = "trainees"
    id = Column(Integer,primary_key=True)
    first_name = Column(String(30),nullable=False)
    last_name = Column(String(30),nullable=False)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    user = relationship("User", back_populates="trainee")


    profile = relationship("TraineeProfile",back_populates="trainee",cascade="all, delete-orphan")

    skills = relationship("Skill",secondary="trainee_skills", back_populates="trainees")
    applications = relationship("Application", back_populates= "trainee")

