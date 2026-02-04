from sqlalchemy import Column,String,ForeignKey,Integer ,Enum
from sqlalchemy.orm import relationship
from database.data import Base
from app_enums import SkillLevel
from models.associations import trainee_skills


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer,primary_key= True)
    name = Column(String(30), nullable= False)
    #level = Column(Enum(SkillLevel),nullable=False)
    level = Column(
    Enum(SkillLevel, name="skill_level_enum"),
    nullable=False)


    trainees  = relationship("Trainee",secondary= "trainee_skills",back_populates="skills")

